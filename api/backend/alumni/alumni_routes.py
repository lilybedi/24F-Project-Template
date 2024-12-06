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
students = Blueprint('alumni', __name__) 


@alumni.route('/<int:alumni_id>', methods=['GET'])
def get_alumni_profile(alumni_id):
    query = '''
        SELECT a.ID, a.First_Name, a.Last_Name, a.Email, a.Grad_Year,
               c.Name as College,
               GROUP_CONCAT(DISTINCT f1.Name) as Majors,
               GROUP_CONCAT(DISTINCT f2.Name) as Minors
        FROM Alumni a
        JOIN College c ON a.College_ID = c.ID
        LEFT JOIN Alumni_Majors am ON a.ID = am.Alumni_ID
        LEFT JOIN Alumni_Minors an ON a.ID = an.Alumni_ID
        LEFT JOIN FieldOfStudy f1 ON am.FieldOfStudy_ID = f1.ID
        LEFT JOIN FieldOfStudy f2 ON an.FieldOfStudy_ID = f2.ID
        WHERE a.ID = %s
        GROUP BY a.ID
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (alumni_id,))
    result = cursor.fetchone()
    
    if not result:
        return jsonify({"error": "Alumni not found"}), 404
        
    return jsonify(result), 200



@alumni.route('/<int:alumni_id>', methods=['PUT'])
def update_alumni_profile(alumni_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    
    # Get College ID if college is being updated
    college_id = None
    if 'College' in data:
        cursor.execute('SELECT ID FROM College WHERE Name = %s', (data['College'],))
        college_result = cursor.fetchone()
        if not college_result:
            return jsonify({"error": "College not found"}), 404
        college_id = college_result['ID']
    
    # Update basic info
    update_query = '''
        UPDATE Alumni
        SET First_Name = %s,
            Last_Name = %s,
            Email = %s,
            Grad_Year = %s
    '''
    params = [
        data['First_Name'],
        data['Last_Name'],
        data['Email'],
        data['Grad_Year']
    ]
    
    if college_id:
        update_query += ', College_ID = %s'
        params.append(college_id)
    
    update_query += ' WHERE ID = %s'
    params.append(alumni_id)
    
    cursor.execute(update_query, tuple(params))
    
    # Update majors if provided
    if 'Majors' in data:
        cursor.execute('DELETE FROM Alumni_Majors WHERE Alumni_ID = %s', (alumni_id,))
        for major_name in data['Majors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (major_name,))
            major_result = cursor.fetchone()
            if major_result:
                cursor.execute('INSERT INTO Alumni_Majors VALUES (%s, %s)', 
                             (alumni_id, major_result['ID']))
    
    # Update minors if provided
    if 'Minors' in data:
        cursor.execute('DELETE FROM Alumni_Minors WHERE Alumni_ID = %s', (alumni_id,))
        for minor_name in data['Minors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (minor_name,))
            minor_result = cursor.fetchone()
            if minor_result:
                cursor.execute('INSERT INTO Alumni_Minors VALUES (%s, %s)', 
                             (alumni_id, minor_result['ID']))
    
    db.get_db().commit()
    return jsonify({"message": "Profile updated successfully"}), 200

@alumni.route('/<int:alumni_id>/positions', methods=['GET'])
def get_alumni_positions(alumni_id):
    query = '''
        SELECT p.*, c.Name as Company_Name, pl.City, pl.State, pl.Country
        FROM Alumni_Position ap
        JOIN Posting p ON ap.Position_ID = p.ID
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Posting_Location pl ON p.Location = pl.ID
        WHERE ap.Alumni_ID = %s
        ORDER BY p.Date_Start DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (alumni_id,))
    return jsonify(cursor.fetchall()), 200

@alumni.route('/messages/send', methods=['POST'])
def send_message():
    data = request.get_json()
    query = '''
        INSERT INTO Message (Student_ID, Alumni_ID, Message, RE)
        VALUES (%s, %s, %s, %s)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (
        data['Student_ID'],
        data['Alumni_ID'],
        data['Message'],
        data.get('RE')  # Reply to message ID if it's a reply
    ))
    db.get_db().commit()
    return jsonify({"message": "Message sent successfully"}), 201

@alumni.route('/messages/<int:alumni_id>', methods=['GET'])
def get_messages(alumni_id):
    query = '''
        SELECT m.*, 
               s.First_Name as Student_First_Name,
               s.Last_Name as Student_Last_Name
        FROM Message m
        JOIN Student s ON m.Student_ID = s.ID
        WHERE m.Alumni_ID = %s
        ORDER BY m.ID DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (alumni_id,))
    return jsonify(cursor.fetchall()), 200

@alumni.route('/postings', methods=['GET'])
def view_postings():
    query = '''
        SELECT p.*, c.Name as Company_Name,
               pl.City, pl.State, pl.Country,
               c.Industry, c.Description as Company_Description
        FROM Posting p
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Posting_Location pl ON p.Location = pl.ID
        WHERE p.Date_End >= CURRENT_DATE()
        ORDER BY p.Date_Start DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    return jsonify(cursor.fetchall()), 200

@alumni.route('/<int:alumni_id>/cv', methods=['POST'])
def upload_cv(alumni_id):
    if 'cv' not in request.files:
        return jsonify({"error": "No CV file provided"}), 400
    
    file = request.files['cv']
    filename = secure_filename(f"cv_alumni_{alumni_id}_{file.filename}")
    filepath = f'cv/{filename}'
    file.save(filepath)
    
    # You might want to store this in a new column in the Alumni table
    # or create a new table for alumni CVs if you want to maintain history
    query = '''
        UPDATE Alumni 
        SET CV_Link = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (filepath, alumni_id))
    db.get_db().commit()
    
    return jsonify({"message": "CV uploaded successfully"}), 200

@alumni.route('/create_profile', methods=['POST'])
def create_alumni_profile():
    data = request.get_json()
    cursor = db.get_db().cursor()
    
    # Get College ID from name
    college_query = 'SELECT ID FROM College WHERE Name = %s'
    cursor.execute(college_query, (data['College'],))
    college_result = cursor.fetchone()
    
    if not college_result:
        return jsonify({"error": "College not found"}), 404
    
    alumni_query = '''
        INSERT INTO Alumni (First_Name, Last_Name, Email, College_ID, Grad_Year)
        VALUES (%s, %s, %s, %s, %s)
    '''
    cursor.execute(alumni_query, (
        data['First_Name'],
        data['Last_Name'],
        data['Email'],
        college_result['ID'],
        data['Grad_Year']
    ))
    alumni_id = cursor.lastrowid
    
    # Handle majors and minors
    if 'Majors' in data:
        for major_name in data['Majors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (major_name,))
            major_result = cursor.fetchone()
            if major_result:
                cursor.execute('INSERT INTO Alumni_Majors VALUES (%s, %s)', 
                             (alumni_id, major_result['ID']))
    
    if 'Minors' in data:
        for minor_name in data['Minors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (minor_name,))
            minor_result = cursor.fetchone()
            if minor_result:
                cursor.execute('INSERT INTO Alumni_Minors VALUES (%s, %s)', 
                             (alumni_id, minor_result['ID']))
    
    db.get_db().commit()
    return jsonify({"message": "Alumni profile created", "id": alumni_id}), 201