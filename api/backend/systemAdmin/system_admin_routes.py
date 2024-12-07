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