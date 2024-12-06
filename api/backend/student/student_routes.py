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
students = Blueprint('students', __name__) 


@students.route('/', methods=['GET'])
def test_db_connection():
    try:
        cursor = db.get_db().cursor()
        cursor.execute("SELECT 1")
        return jsonify({"message": "Database connected"}), 200
    except Exception as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500
    

@students.route('/get_all', methods=['GET'])
def get_students():
    query = '''
        SELECT s.ID, s.First_Name, s.Last_Name, s.Email, s.GPA, s.Grad_Year,
               c.Name as College_Name, cy.cycle,
               GROUP_CONCAT(DISTINCT f1.Name) as Majors,
               GROUP_CONCAT(DISTINCT f2.Name) as Minors
        FROM Student s
        JOIN College c ON s.College_ID = c.ID
        JOIN Cycle cy ON s.Cycle = cy.ID
        LEFT JOIN Student_Majors sm ON s.ID = sm.Student_ID
        LEFT JOIN Student_Minors sn ON s.ID = sn.Student_ID
        LEFT JOIN FieldOfStudy f1 ON sm.FieldOfStudy_ID = f1.ID
        LEFT JOIN FieldOfStudy f2 ON sn.FieldOfStudy_ID = f2.ID
        GROUP BY s.ID
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    return make_response(jsonify(cursor.fetchall()), 200)

@students.route('/create_profile', methods=['POST'])
def create_student_profile():
    data = request.get_json()
    cursor = db.get_db().cursor()
    
    # Get College ID from name
    college_query = 'SELECT ID FROM College WHERE Name = %s'
    cursor.execute(college_query, (data['College'],))
    college_result = cursor.fetchone()
    
    if not college_result:
        return jsonify({"error": "College not found"}), 404
    
    college_id = college_result['ID']
    
    # Insert student base info
    student_query = '''
        INSERT INTO Student (First_Name, Last_Name, Preferred_Name, Email, 
                           Phone_Number, GPA, College_ID, Grad_Year, Cycle, 
                           Advisor_ID, Resume_Link, Description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(student_query, (
        data['First_Name'], data['Last_Name'], data.get('Preferred_Name'),
        data['Email'], data['Phone_Number'], data['GPA'], college_id,
        data['Grad_Year'], data['Cycle'], data['Advisor_ID'],
        data.get('Resume_Link'), data.get('Description')
    ))
    student_id = cursor.lastrowid
    
    # Handle majors and minors (assuming they're passed as names)
    if 'Majors' in data:
        for major_name in data['Majors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (major_name,))
            major_result = cursor.fetchone()
            if major_result:
                cursor.execute('INSERT INTO Student_Majors VALUES (%s, %s)', 
                             (student_id, major_result['ID']))
    
    if 'Minors' in data:
        for minor_name in data['Minors']:
            cursor.execute('SELECT ID FROM FieldOfStudy WHERE Name = %s', (minor_name,))
            minor_result = cursor.fetchone()
            if minor_result:
                cursor.execute('INSERT INTO Student_Minors VALUES (%s, %s)', 
                             (student_id, minor_result['ID']))
            
    db.get_db().commit()
    return jsonify({"message": "Student profile created", "id": student_id}), 201


@students.route('/edit_profile/<int:student_id>', methods=['PUT'])
def edit_student_profile(student_id):
    data = request.get_json()
    cursor = db.get_db().cursor()
    
    update_query = '''
        UPDATE Student
        SET First_Name = %s, Last_Name = %s, Preferred_Name = %s,
            Email = %s, Phone_Number = %s, GPA = %s, Grad_Year = %s,
            Resume_Link = %s, Description = %s
        WHERE ID = %s
    '''
    cursor.execute(update_query, (
        data['First_Name'], data['Last_Name'], data.get('Preferred_Name'),
        data['Email'], data['Phone_Number'], data['GPA'], data['Grad_Year'],
        data.get('Resume_Link'), data.get('Description'), student_id
    ))
    
    if 'Majors' in data:
        cursor.execute('DELETE FROM Student_Majors WHERE Student_ID = %s', (student_id,))
        for major_id in data['Majors']:
            cursor.execute('INSERT INTO Student_Majors VALUES (%s, %s)', 
                         (student_id, major_id))
            
    if 'Minors' in data:
        cursor.execute('DELETE FROM Student_Minors WHERE Student_ID = %s', (student_id,))
        for minor_id in data['Minors']:
            cursor.execute('INSERT INTO Student_Minors VALUES (%s, %s)', 
                         (student_id, minor_id))
    
    db.get_db().commit()
    return jsonify({"message": "Profile updated successfully"}), 200

@students.route('/postings/by_pay', methods=['GET'])
def filter_postings_by_pay():
    min_pay = request.args.get('min_pay', type=int)
    query = '''
        SELECT p.*, c.Name as Company_Name, pl.City, pl.State, pl.Country
        FROM Posting p
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Posting_Location pl ON p.Location = pl.ID
        WHERE p.Pay >= %s AND p.Filled = FALSE
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (min_pay,))
    return jsonify(cursor.fetchall()), 200

@students.route('/postings/by_location', methods=['GET'])
def filter_postings_by_location():
    location = request.args.get('location')
    query = '''
        SELECT p.*, c.Name as Company_Name, pl.City, pl.State, pl.Country
        FROM Posting p
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Posting_Location pl ON p.Location = pl.ID
        WHERE (pl.City LIKE %s OR pl.State LIKE %s OR pl.Country LIKE %s)
        AND p.Filled = FALSE
    '''
    search = f"%{location}%"
    cursor = db.get_db().cursor()
    cursor.execute(query, (search, search, search))
    return jsonify(cursor.fetchall()), 200

@students.route('/applications/<int:student_id>', methods=['GET'])
def view_applications(student_id):
    query = '''
        SELECT a.*, p.Name as Position_Name, c.Name as Company_Name,
               s.Status_Description
        FROM Application a
        JOIN Posting p ON a.Position_ID = p.ID
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Status s ON a.Status_ID = s.ID
        WHERE a.Student_ID = %s
        ORDER BY a.submittedDate DESC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (student_id,))
    return jsonify(cursor.fetchall()), 200

@students.route('/resume/upload', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file provided"}), 400
        
    file = request.files['resume']
    student_id = request.form['student_id']
    filename = secure_filename(file.filename)
    filepath = f'resumes/{filename}'
    file.save(filepath)
    
    query = '''
        UPDATE Student
        SET Resume_Link = %s
        WHERE ID = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (filepath, student_id))
    db.get_db().commit()
    return jsonify({"message": "Resume uploaded successfully"}), 200


@students.route('/profile/<int:student_id>', methods=['GET'])
def get_student_profile(student_id):
    query = '''
        SELECT s.ID, s.First_Name, s.Last_Name, s.Preferred_Name, s.Email, 
               s.Phone_Number, s.GPA, s.Grad_Year, s.Resume_Link, s.Description,
               c.Name as College_Name, cy.cycle,
               GROUP_CONCAT(DISTINCT f1.Name) as Majors,
               GROUP_CONCAT(DISTINCT f2.Name) as Minors,
               a.First_Name as Advisor_First_Name,
               a.Last_Name as Advisor_Last_Name
        FROM Student s
        JOIN College c ON s.College_ID = c.ID
        JOIN Cycle cy ON s.Cycle = cy.ID
        LEFT JOIN Student_Majors sm ON s.ID = sm.Student_ID
        LEFT JOIN Student_Minors sn ON s.ID = sn.Student_ID
        LEFT JOIN FieldOfStudy f1 ON sm.FieldOfStudy_ID = f1.ID
        LEFT JOIN FieldOfStudy f2 ON sn.FieldOfStudy_ID = f2.ID
        LEFT JOIN Advisor a ON s.Advisor_ID = a.ID
        WHERE s.ID = %s
        GROUP BY s.ID
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    
    if not result:
        return jsonify({"error": "Student not found"}), 404
        
    return jsonify(result), 200