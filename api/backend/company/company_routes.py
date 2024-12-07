########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
companies = Blueprint('companies', __name__)

@companies.route('/profile', methods=['POST'])
def create_company_profile():
    """Create a new company profile (User Story 2)"""
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        query = '''
            INSERT INTO Company (Name, Industry, Description)
            VALUES (%s, %s, %s)
        '''
        cursor.execute(query, (
            data['name'],
            data['industry'],
            data.get('description')
        ))
        company_id = cursor.lastrowid
        db.get_db().commit()
        
        return jsonify({
            "message": "Company profile created successfully",
            "company_id": company_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@companies.route('/profile/<int:company_id>', methods=['PUT'])
def update_company_profile(company_id):
    """Update company profile """
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        query = '''
            UPDATE Company
            SET Name = %s, Industry = %s, Description = %s
            WHERE ID = %s
        '''
        cursor.execute(query, (
            data['name'],
            data['industry'],
            data.get('description'),
            company_id
        ))
        db.get_db().commit()
        
        return jsonify({"message": "Company profile updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@companies.route('/posting', methods=['POST'])
def create_posting():
    """Create a new job posting with skills (User Story 1, 4, 9)"""
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        # Create the posting location entity first.
        location_query = '''
            INSERT INTO Posting_Location (Region, State, Zip_Code, Address_Number, 
                                        Street, City, Country)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(location_query, (
            data['location']['region'],
            data['location']['state'],
            data['location']['zip_code'],
            data['location']['address_number'],
            data['location']['street'],
            data['location']['city'],
            data['location']['country']
        ))
        location_id = cursor.lastrowid
        
        # Create the posting itself now.
        posting_query = '''
            INSERT INTO Posting (Name, Company_ID, Industry, Location, Date_Start,
                               Date_End, Filled, Minimum_GPA, Title, Description, Pay)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        cursor.execute(posting_query, (
            data['name'],
            data['company_id'],
            data['industry'],
            location_id,
            data['date_start'],
            data['date_end'],
            False, # Setting False because position can't be filled if its not even posted yet.
            data['minimum_gpa'],
            data['title'],
            data['description'],
            data['pay']
        ))
        posting_id = cursor.lastrowid
        
        # Add skills if provided
        if 'skills' in data:
            skills_query = '''
                INSERT INTO Posting_Skills (Position_ID, Skill_ID)
                VALUES (%s, %s)
            '''
            for skill_id in data['skills']:
                cursor.execute(skills_query, (posting_id, skill_id))
        
        db.get_db().commit()
        return jsonify({
            "message": "Posting created successfully",
            "posting_id": posting_id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400



@companies.route('/posting/<int:posting_id>', methods=['PUT'])
def update_posting(posting_id):
    """Update job posting details and skills (User Story 9)"""
    try:
        data = request.get_json()
        cursor = db.get_db().cursor()
        
        # Fetch existing values
        fetch_query = '''
            SELECT Name, Industry, Date_Start, Date_End, Minimum_GPA, Title, Description, Pay
            FROM Posting
            WHERE ID = %s
        '''
        cursor.execute(fetch_query, (posting_id,))
        existing_posting = cursor.fetchone()
        
        if not existing_posting:
            return jsonify({"error": "Posting not found"}), 404
        
        # Merge existing values with updates
        updated_posting = {
            "name": data.get("name", existing_posting["Name"]),
            "industry": data.get("industry", existing_posting["Industry"]),
            "date_start": data.get("date_start", existing_posting["Date_Start"]),
            "date_end": data.get("date_end", existing_posting["Date_End"]),
            "minimum_gpa": data.get("minimum_gpa", existing_posting["Minimum_GPA"]),
            "title": data.get("title", existing_posting["Title"]),
            "description": data.get("description", existing_posting["Description"]),
            "pay": data.get("pay", existing_posting["Pay"]),
        }
        
        # Update posting
        posting_query = '''
            UPDATE Posting
            SET Name = %s, Industry = %s, Date_Start = %s, Date_End = %s,
                Minimum_GPA = %s, Title = %s, Description = %s, Pay = %s
            WHERE ID = %s
        '''
        cursor.execute(posting_query, (
            updated_posting["name"],
            updated_posting["industry"],
            updated_posting["date_start"],
            updated_posting["date_end"],
            updated_posting["minimum_gpa"],
            updated_posting["title"],
            updated_posting["description"],
            updated_posting["pay"],
            posting_id
        ))
        
        # Update skills if provided
        if "skills" in data:
            # Remove existing skills
            cursor.execute('DELETE FROM Posting_Skills WHERE Position_ID = %s', (posting_id,))
            
            # Add new skills
            skills_query = 'INSERT INTO Posting_Skills (Position_ID, Skill_ID) VALUES (%s, %s)'
            for skill_id in data["skills"]:
                cursor.execute(skills_query, (posting_id, skill_id))
        
        db.get_db().commit()
        return jsonify({"message": "Posting updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    

@companies.route('/posting/<int:posting_id>/filled', methods=['PUT'])
def mark_posting_filled(posting_id):
    """Mark a position as filled """
    try:
        cursor = db.get_db().cursor()
        query = '''
            UPDATE Posting
            SET Filled = TRUE
            WHERE ID = %s
        '''
        cursor.execute(query, (posting_id,))
        db.get_db().commit()
        return jsonify({"message": "Posting marked as filled"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@companies.route('/posting/<int:posting_id>', methods=['DELETE'])
def delete_posting(posting_id):
    """Remove a job posting"""
    try:
        cursor = db.get_db().cursor()
        
        # Delete related records first
        cursor.execute('DELETE FROM Posting_Skills WHERE Position_ID = %s', (posting_id,))
        cursor.execute('DELETE FROM Application WHERE Position_ID = %s', (posting_id,))
        
        # Delete the posting
        cursor.execute('DELETE FROM Posting WHERE ID = %s', (posting_id,))
        
        db.get_db().commit()
        return jsonify({"message": "Posting deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@companies.route('/posting/<int:posting_id>/applications', methods=['GET'])
def view_applications(posting_id):
    """View applications for a posting"""
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT a.*, s.First_Name, s.Last_Name, s.Email, s.Phone_Number,
                   s.GPA, s.Resume_Link, st.Status_Description,
                   GROUP_CONCAT(DISTINCT sk.Name) as Skills
            FROM Application a
            JOIN Student s ON a.Student_ID = s.ID
            JOIN Status st ON a.Status_ID = st.ID
            LEFT JOIN Student_Skills ss ON s.ID = ss.Student_ID
            LEFT JOIN Skill sk ON ss.Skill_ID = sk.ID
            WHERE a.Position_ID = %s
            GROUP BY a.ID
            ORDER BY a.submittedDate DESC
        '''
        cursor.execute(query, (posting_id,))
        return jsonify(cursor.fetchall()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@companies.route('/student/<int:student_id>/contact', methods=['GET'])
def get_student_contact(student_id):
    """Get student contact information"""
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT Email, Phone_Number, Resume_Link
            FROM Student
            WHERE ID = %s
        '''
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        return jsonify({"error": "Student not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@companies.route('/profile/<int:company_id>', methods=['GET'])
def get_company_profile(company_id):
    """Get a company's profile information"""
    try:
        cursor = db.get_db().cursor()
        query = '''
            SELECT c.ID, c.Name, c.Industry, c.Description,
                   COUNT(DISTINCT p.ID) as Active_Postings
            FROM Company c
            LEFT JOIN Posting p ON c.ID = p.Company_ID
            WHERE c.ID = %s
            GROUP BY c.ID
        '''
        cursor.execute(query, (company_id,))
        result = cursor.fetchone()
        
        if not result:
            return jsonify({"error": "Company not found"}), 404
            
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400