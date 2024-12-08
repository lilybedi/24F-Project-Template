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
system_admin = Blueprint('system_admin', __name__) 

@system_admin.route('/advisors/add', methods=['POST'])
def add_advisor():
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        query = '''
            INSERT INTO Advisor (First_Name, Last_Name, Preferred_Name, College_ID)
            VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(query, (
            data['First_Name'],
            data['Last_Name'],
            data.get('Preferred_Name'),
            data['College_ID']
        ))
        advisor_id = cursor.lastrowid
        db.get_db().commit()
        
        return jsonify({"message": "Advisor added successfully", "id": advisor_id}), 201
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500
    

@system_admin.route('/advisors/<int:advisor_id>', methods=['DELETE'])
def remove_advisor(advisor_id):
    try:
        cursor = db.get_db().cursor()
        
        # Check if advisor exists
        cursor.execute('SELECT ID FROM Advisor WHERE ID = %s', (advisor_id,))
        if not cursor.fetchone():
            return jsonify({"error": "Advisor not found"}), 404
            
        cursor.execute('DELETE FROM Advisor WHERE ID = %s', (advisor_id,))
        db.get_db().commit()
        
        return jsonify({"message": "Advisor removed successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500
    


@system_admin.route('/students/<int:student_id>/override', methods=['PUT'])
def override_student_restrictions(student_id):
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        # Update student eligibility
        update_query = '''
            UPDATE Student
            SET Eligibility = %s
            WHERE ID = %s
        '''
        cursor.execute(update_query, (data['eligibility'], student_id))
        
        # Add special application if provided
        if 'position_id' in data:
            app_query = '''
                INSERT INTO Application (Student_ID, Position_ID, submittedDate, Status_ID)
                VALUES (%s, %s, NOW(), %s)
            '''
            cursor.execute(app_query, (
                student_id,
                data['position_id'],
                data.get('status_id', 1)  # Default to initial status
            ))
            
        db.get_db().commit()
        return jsonify({"message": "Student restrictions overridden successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500




@system_admin.route('/activity/applications', methods=['GET'])
def get_application_activity():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT 
                a.ID as Application_ID,
                a.Student_ID,
                s.First_Name as Student_First_Name,
                s.Last_Name as Student_Last_Name,
                p.Name as Position_Name,
                c.Name as Company_Name,
                a.submittedDate,
                st.Status_Description
            FROM Application a
            JOIN Student s ON a.Student_ID = s.ID
            JOIN Posting p ON a.Position_ID = p.ID
            JOIN Company c ON p.Company_ID = c.ID
            JOIN Status st ON a.Status_ID = st.ID
            ORDER BY a.submittedDate DESC
            LIMIT 100
        '''
        cursor.execute(query)
        return make_response(jsonify(cursor.fetchall()), 200)
    except Exception as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500




@system_admin.route('/tickets', methods=['GET'])
def get_tickets():
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT 
                t.ID,
                t.Message,
                t.Completed,
                sa.First_Name as Reporter_First_Name,
                sa.Last_Name as Reporter_Last_Name
            FROM Ticket t
            JOIN System_Admin sa ON t.Reporter_ID = sa.ID
            ORDER BY t.ID DESC
        '''
        cursor.execute(query)
        return make_response(jsonify(cursor.fetchall()), 200)
    except Exception as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500




@system_admin.route('/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        query = '''
            UPDATE Ticket
            SET Completed = %s
            WHERE ID = %s
        '''
        cursor.execute(query, (data['completed'], ticket_id))
        db.get_db().commit()

        return jsonify({"message": "Ticket updated successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500
    


@system_admin.route('/accounts/<string:account_type>/<int:account_id>', methods=['DELETE'])
def delete_account(account_type, account_id):
    try:
        cursor = db.get_db().cursor()
        
        # Determine the table based on the account type
        if account_type == 'student':
            table = 'Student'
        elif account_type == 'advisor':
            table = 'Advisor'
        elif account_type == 'alumni':
            table = 'Alumni'
        else:
            return jsonify({"error": "Invalid account type"}), 400
            
        # Check if the account exists
        cursor.execute(f'SELECT ID FROM {table} WHERE ID = %s', (account_id,))
        if not cursor.fetchone():
            return jsonify({"error": f"{account_type} not found"}), 404
        
        # Attempt to delete the account
        cursor.execute(f'DELETE FROM {table} WHERE ID = %s', (account_id,))
        db.get_db().commit()
        
        return jsonify({"message": f"{account_type} account deleted successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        
        # Add detailed logging for debugging
        logging.error(f"Error occurred during account deletion: {str(e)}")
        
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500



@system_admin.route('/accounts/<string:account_type>/<int:account_id>/restrict', methods=['POST'])
def restrict_account(account_type, account_id):
    try:
        cursor = db.get_db().cursor()
        
        if account_type == 'student':
            query = '''
                UPDATE Student
                SET Eligibility = FALSE
                WHERE ID = %s
            '''
            cursor.execute(query, (account_id,))
        else:
            return jsonify({"error": "Account type not supported for restriction"}), 400
            
        db.get_db().commit()
        return jsonify({"message": f"{account_type} account restricted successfully"}), 200
    except Exception as e:
        db.get_db().rollback()
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500


@system_admin.route('/<int:admin_id>', methods=['GET'])
def get_system_admin(admin_id):
    try:
        cursor = db.get_db().cursor()
        
        query = '''
            SELECT 
                ID,
                First_Name,
                Last_Name,
                Preferred_Name
            FROM System_Admin
            WHERE ID = %s
        '''
        cursor.execute(query, (admin_id,))
        result = cursor.fetchone()
        
        if not result:
            return jsonify({"error": "System admin not found"}), 404
            
        return jsonify(result), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching system admin: {str(e)}")
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500