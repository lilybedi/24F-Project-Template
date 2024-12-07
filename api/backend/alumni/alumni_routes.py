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
alumni = Blueprint('alumni', __name__) 


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

@alumni.route('/<int:alumni_id>/previous_positions', methods=['GET'])
def get_alumni_previous_positions(alumni_id):
    """
    Get all previous positions held by an alumni with detailed information
    about the company, location, and required skills.
    """
    query = '''
        SELECT 
            p.ID as Position_ID,
            p.Title,
            p.Description as Position_Description,
            p.Pay,
            p.Date_Start,
            p.Date_End,
            c.Name as Company_Name,
            c.Industry,
            c.Description as Company_Description,
            pl.City,
            pl.State,
            pl.Country,
            GROUP_CONCAT(DISTINCT s.Name) as Required_Skills
        FROM Alumni_Position ap
        JOIN Posting p ON ap.Position_ID = p.ID
        JOIN Company c ON p.Company_ID = c.ID
        JOIN Posting_Location pl ON p.Location = pl.ID
        LEFT JOIN Posting_Skills ps ON p.ID = ps.Position_ID
        LEFT JOIN Skill s ON ps.Skill_ID = s.ID
        WHERE ap.Alumni_ID = %s
        GROUP BY p.ID
        ORDER BY p.Date_Start DESC
    '''
    
    try:
        cursor = db.get_db().cursor()
        cursor.execute(query, (alumni_id,))
        positions = cursor.fetchall()
        
        if not positions:
            return jsonify({
                "message": "No previous positions found for this alumni",
                "positions": []
            }), 200
            
        # Format dates for JSON response
        for position in positions:
            if position['Date_Start']:
                position['Date_Start'] = position['Date_Start'].strftime('%Y-%m-%d')
            if position['Date_End']:
                position['Date_End'] = position['Date_End'].strftime('%Y-%m-%d')
            
            # Convert skills string to list if not None
            if position['Required_Skills']:
                position['Required_Skills'] = position['Required_Skills'].split(',')
            else:
                position['Required_Skills'] = []
        
        return jsonify({
            "positions": positions,
            "count": len(positions)
        }), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching alumni positions: {str(e)}")
        return jsonify({
            "error": "An error occurred while fetching positions",
            "details": str(e)
        }), 500

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


@alumni.route('/<int:alumni_id>/students', methods=['GET'])
def get_alumni_students(alumni_id):
    """
    Get all students related to an alumni (via Alumni_Student table)
    """
    try:
        query = '''
            SELECT 
                s.ID as Student_ID,
                s.First_Name,
                s.Last_Name,
                s.GPA,
                c.Name as College_Name,
                GROUP_CONCAT(DISTINCT f.Name) as Majors
            FROM Alumni_Student al
            JOIN Student s ON al.Student_ID = s.ID
            JOIN College c ON s.College_ID = c.ID
            LEFT JOIN Student_Majors sm ON s.ID = sm.Student_ID
            LEFT JOIN FieldOfStudy f ON sm.FieldOfStudy_ID = f.ID
            WHERE al.Alumni_ID = %s
            GROUP BY s.ID
        '''
        cursor = db.get_db().cursor()
        cursor.execute(query, (alumni_id,))
        results = cursor.fetchall()
        
        if not results:
            return jsonify({"message": "No related students found for this alumni"}), 404
        
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": f"Error occurred: {str(e)}"}), 500
    
@alumni.route('/<int:alumni_id>/positions', methods=['POST'])
def add_alumni_position(alumni_id):
    """
    Add a new position to an alumni's profile. The position can either be:
    1. An existing posting (using posting_id)
    2. A new position entry (requiring full position details)
    """
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        logging.info(f"Payload received: {data}")

        # First verify the alumni exists
        cursor.execute('SELECT ID FROM Alumni WHERE ID = %s', (alumni_id,))
        if not cursor.fetchone():
            return jsonify({"error": "Alumni not found"}), 404
            
        position_id = None
        
        # If posting_id is provided, use existing posting
        if 'posting_id' in data:
            cursor.execute('SELECT ID FROM Posting WHERE ID = %s', (data['posting_id'],))
            if not cursor.fetchone():
                return jsonify({"error": "Posting not found"}), 404
            position_id = data['posting_id']
            
        # Otherwise, create new posting
        else:
            # Validate required fields
            required_fields = ['title', 'company_name', 'date_start', 'pay']
            if not all(field in data for field in required_fields):
                return jsonify({"error": "Missing required fields"}), 400
                
            # Get or create company
            cursor.execute('SELECT ID FROM Company WHERE Name = %s', (data['company_name'],))
            company_result = cursor.fetchone()
            
            if company_result:
                company_id = company_result['ID']
            else:
                # Create new company
                cursor.execute(
                    'INSERT INTO Company (Name, Industry, Description) VALUES (%s, %s, %s)',
                    (data['company_name'], data.get('industry'), data.get('company_description'))
                )
                company_id = cursor.lastrowid
                
            # Create or get location
            location_query = '''
                INSERT INTO Posting_Location (City, State, Country)
                VALUES (%s, %s, %s)
            '''
            cursor.execute(location_query, (
                data.get('city'),
                data.get('state'),
                data.get('country')
            ))
            location_id = cursor.lastrowid
            
            # Create new posting
            posting_query = '''
                INSERT INTO Posting (
                    Title, Company_ID, Location, Date_Start, Date_End,
                    Description, Pay
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            '''
            cursor.execute(posting_query, (
                data['title'],
                company_id,
                location_id,
                data['date_start'],
                data.get('date_end'),
                data.get('description'),
                data['pay']
            ))
            position_id = cursor.lastrowid
            
            # Add skills if provided
            if 'skills' in data:
                for skill_name in data['skills']:
                    # Get or create skill
                    cursor.execute('SELECT ID FROM Skill WHERE Name = %s', (skill_name,))
                    skill_result = cursor.fetchone()
                    
                    if not skill_result:
                        cursor.execute('INSERT INTO Skill (Name) VALUES (%s)', (skill_name,))
                        skill_id = cursor.lastrowid
                    else:
                        skill_id = skill_result['ID']
                        
                    # Add to posting_skills
                    cursor.execute(
                        'INSERT INTO Posting_Skills (Position_ID, Skill_ID) VALUES (%s, %s)',
                        (position_id, skill_id)
                    )
        
        # Add position to alumni's profile
        cursor.execute(
            'INSERT INTO Alumni_Position (Position_ID, Alumni_ID) VALUES (%s, %s)',
            (position_id, alumni_id)
        )
        
        db.get_db().commit()
        return jsonify({
            "message": "Position added successfully",
            "position_id": position_id
        }), 201
        
    except Exception as e:
        current_app.logger.error(f"Error adding alumni position: {str(e)}")
        db.get_db().rollback()
        return jsonify({
            "error": "An error occurred while adding the position",
            "details": str(e)
        }), 500