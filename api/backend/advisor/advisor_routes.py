from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from werkzeug.utils import secure_filename
import logging
#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
advisors = Blueprint('advisors', __name__) 



@advisors.route('/students/<int:advisor_id>', methods=['GET'])
def get_advisor_students(advisor_id):
    """Get all students for an advisor with their progress status (Story 1)"""
    try:
        query = '''
            SELECT
                s.ID,
                s.First_Name,
                s.Last_Name,
                s.GPA,
                CASE
                    WHEN s.Eligibility = 1 THEN 'TRUE'
                    ELSE 'FALSE'
                END as Eligibility,
                CASE
                    WHEN s.Hired = 1 THEN 'TRUE'
                    ELSE 'FALSE'
                END as Hired,
                COUNT(DISTINCT a.ID) as Total_Applications,
                MAX(a.submittedDate) as Latest_Application,
                (
                    SELECT st.Status_Description
                    FROM Application a2
                    JOIN Status st ON a2.Status_ID = st.ID
                    WHERE a2.Student_ID = s.ID
                    ORDER BY a2.submittedDate DESC
                    LIMIT 1
                ) as Latest_Status
            FROM Student s
            LEFT JOIN Application a ON s.ID = a.Student_ID
            WHERE s.Advisor_ID = %s
            GROUP BY s.ID;
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (advisor_id,))
        return jsonify(cursor.fetchall()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@advisors.route('/statistics/<int:advisor_id>', methods=['GET'])
def get_advisor_statistics(advisor_id):
    """Get summary statistics for an advisor's students (Story 3)"""
    try:
        cursor = db.get_db().cursor()
        
        # Get total students and their status
        status_query = '''
            SELECT 
                COUNT(*) as Total_Students,
                SUM(CASE WHEN Hired = TRUE THEN 1 ELSE 0 END) as Placed_Students,
                SUM(CASE WHEN Hired = FALSE THEN 1 ELSE 0 END) as Searching_Students
            FROM Student
            WHERE Advisor_ID = %s AND Eligibility = TRUE
        '''
        cursor.execute(status_query, (advisor_id,))
        status_stats = cursor.fetchone()
        
        # Get application distribution
        apps_query = '''
            SELECT 
                COUNT(a.ID) as Applications_Count,
                COUNT(DISTINCT a.Student_ID) as Students_Applied,
                AVG(COUNT(a.ID)) OVER () as Avg_Applications_Per_Student
            FROM Student s
            LEFT JOIN Application a ON s.ID = a.Student_ID
            WHERE s.Advisor_ID = %s AND s.Eligibility = TRUE
            GROUP BY a.Student_ID
        '''
        cursor.execute(apps_query, (advisor_id,))
        app_stats = cursor.fetchall()
        
        return jsonify({
            "status_statistics": status_stats,
            "application_statistics": app_stats
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400