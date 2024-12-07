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
advisor = Blueprint('advisor', __name__) 

@advisor.route('/allStudents',methods=['GET'])
def get_all_students():
    query = '''
        SELECT *
        FROM Student
        WHERE eligibility = TRUE
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query,)
    return jsonify(cursor.fetchall()), 200

# @alumni.route('/postings', methods=['GET'])
# def view_postings():
#     query = '''
#         SELECT p.*, c.Name as Company_Name,
#             pl.City, pl.State, pl.Country,
#             c.Industry, c.Description as Company_Description
#         FROM Posting p
#         JOIN Company c ON p.Company_ID = c.ID
#         JOIN Posting_Location pl ON p.Location = pl.ID
#         ORDER BY p.Date_Start DESC
#     '''
#     cursor = db.get_db().cursor()
#     cursor.execute(query)
#     return jsonify(cursor.fetchall()), 200