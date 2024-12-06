from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
students = Blueprint('students', __name__)  # Changed from 'products' to 'students'

@students.route('/', methods=['GET'])       # Changed route to '/' since we're using url_prefix='/s' in rest_entry.py
def get_students():                         # Changed function name to match purpose
    query = '''
        SELECT First_Name, Last_Name
        FROM Student
    '''
    
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of products
    cursor.execute(query)

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # Create a HTTP Response object
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response