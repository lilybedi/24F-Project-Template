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
    


@advisors.route('/positions/filled/<int:advisor_id>', methods=['GET'])
def get_filled_positions(advisor_id):
    """Get information about filled positions (Story 4)"""
    try:
        query = '''
            SELECT 
                p.ID, 
                p.Name, 
                p.Title, 
                c.Name AS Company_Name,
                p.Filled, 
                p.Date_Start, 
                p.Date_End,
                COUNT(DISTINCT a.ID) AS Total_Applications,
                COUNT(DISTINCT CASE WHEN st.Status_Description = 'Accepted' 
                    THEN a.ID END) AS Accepted_Applications
            FROM Posting p
            JOIN Company c ON p.Company_ID = c.ID
            LEFT JOIN Application a ON p.ID = a.Position_ID
            LEFT JOIN Status st ON a.Status_ID = st.ID
            WHERE p.Filled = TRUE
            GROUP BY p.ID
            ORDER BY p.Date_End DESC;
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query)
        return jsonify(cursor.fetchall()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    



@advisors.route('/students/<int:advisor_id>/filter', methods=['GET'])
def filter_students_by_status(advisor_id):
    """Filter advisees based on co-op status (Story 5)"""
    try:
        hired = request.args.get('hired')
        if hired is not None:
            hired = hired.lower() == 'true'

        current_app.logger.info(f"Advisor ID: {advisor_id}, Hired Filter: {hired}")

        query = '''
            SELECT 
                s.ID, s.First_Name, s.Last_Name, s.GPA,
                c.Name as College_Name,
                GROUP_CONCAT(DISTINCT f.Name) as Majors
            FROM Student s
            JOIN College c ON s.College_ID = c.ID
            LEFT JOIN Student_Majors sm ON s.ID = sm.Student_ID
            LEFT JOIN FieldOfStudy f ON sm.FieldOfStudy_ID = f.ID
            WHERE s.Advisor_ID = %s AND s.Hired = %s AND s.Eligibility = TRUE
            GROUP BY s.ID
        '''
        current_app.logger.info(f"Executing query: {query} with parameters: {(advisor_id, hired)}")

        cursor = db.get_db().cursor()
        cursor.execute(query, (advisor_id, hired))
        results = cursor.fetchall()
        current_app.logger.info(f"Query Results: {results}")
        return jsonify(results), 200
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 400


@advisors.route('/term-summary/<int:advisor_id>', methods=['GET'])
def get_term_summary(advisor_id):
    """Get end-of-term summary data (Story 6)"""
    try:
        cursor = db.get_db().cursor()
        
        # Get placement statistics
        placement_query = '''
            SELECT 
                cy.cycle,
                COUNT(DISTINCT s.ID) as Total_Students,
                SUM(CASE WHEN s.Hired = TRUE THEN 1 ELSE 0 END) as Placed_Students,
                AVG(s.GPA) as Average_GPA,
                COUNT(DISTINCT a.ID) as Total_Applications,
                AVG(p.Pay) as Average_Salary
            FROM Student s
            JOIN Cycle cy ON s.Cycle = cy.ID
            LEFT JOIN Application a ON s.ID = a.Student_ID
            LEFT JOIN Posting p ON a.Position_ID = p.ID
            WHERE s.Advisor_ID = %s AND s.Eligibility = TRUE
            GROUP BY cy.cycle
        '''
        cursor.execute(placement_query, (advisor_id,))
        placement_stats = cursor.fetchall()
        
        # Get industry distribution
        industry_query = '''
            SELECT 
                p.Industry,
                COUNT(DISTINCT s.ID) as Placed_Students
            FROM Student s
            JOIN Application a ON s.ID = a.Student_ID
            JOIN Posting p ON a.Position_ID = p.ID
            WHERE s.Advisor_ID = %s AND s.Hired = TRUE
            GROUP BY p.Industry
        '''
        cursor.execute(industry_query, (advisor_id,))
        industry_stats = cursor.fetchall()
        
        return jsonify({
            "placement_statistics": placement_stats,
            "industry_distribution": industry_stats
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400