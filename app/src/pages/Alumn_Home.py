# import logging
# logger = logging.getLogger(__name__)
# import streamlit as st
# from streamlit_extras.app_logo import add_logo
# import numpy as np
# import random
# import time
# from modules.nav import SideBarLinks

import logging

import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()
import requests
import streamlit as st

# # Example Streamlit page
# st.title("Filter Postings by Location")

# # Input field for location
# location = st.text_input("Enter location (city, state, or country):")

# # Button to trigger API call
# if st.button("Search"):
#     if location:
#         try:
#             # Make the API call
#             response = requests.get(
#                 "http://api:4000/s/postings/by_location",
#                 params={"location": location},
#             )
            
#             # Raise error for bad status codes
#             response.raise_for_status()
            
#             # Parse and display the data
#             data = response.json()
#             st.write(f"Results for location: {location}")
#             st.dataframe(data)
#         except requests.RequestException as e:
#             st.error(f"Error fetching data: {e}")
#     else:
#         st.error("Please enter a location before searching.")


# st.title(f"Welcome Alumni , {st.session_state['first_name']}.")
# st.write('')
# st.write('')
# st.write('### What would you like to do today?')

# data = {} 
# try:
#   data = requests.get('http://api:4000/s/get_all').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)

# st.title(f"Welcome Alumni , {st.session_state['first_name']}.")

# # Placeholder for student ID (replace with dynamic value in real implementation)
# student_id = st.session_state.get("student_id", 1)  # Replace '1' with actual student ID

# st.write('')
# st.write('')
# st.write('### Your Applications')

# # Fetch applications from the API
# try:
#     # Make API call to fetch applications for the student
#     response = requests.get(f"http://api:4000/s/applications/{student_id}")
#     response.raise_for_status()  # Raise an exception for HTTP errors
#     applications = response.json()

#     # Display the applications in a table
#     if applications:
#         st.dataframe(applications)
#     else:
#         st.write("No applications found.")
# except requests.RequestException as e:
#     st.error(f"Error fetching applications: {e}")


# st.title("Get Student by ID")

# # Input field for Student ID
# student_id = st.number_input("Enter Student ID:", min_value=1, step=1)

# # Fetch student details when button is clicked
# if st.button("Get Student Details"):
#     try:
#         response = requests.get(f"http://api:4000/s/profile/{student_id}")
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         student = response.json()

#         # Display student details
#         st.write("### Student Details")
#         st.json(student)
#     except requests.RequestException as e:
#         st.error(f"Failed to fetch student details: {e}")

# st.title("Job Postings")

# try:
#     response = requests.get("http://api:4000/s/getJobPostings")
#     response.raise_for_status()
#     job_postings = response.json()
#     st.write("Available Job Postings")
#     st.dataframe(job_postings)
# except requests.RequestException as e:
#     st.error(f"Failed to fetch job postings: {e}")



# Streamlit App Configuration
# st.title("Job Postings")
# st.write("Search and filter job postings with optional location and salary filters.")

# # Input fields for filters
# location = st.text_input("Location (City, State, or Country):")
# min_pay = st.number_input("Minimum Pay:", min_value=0, step=1000)

# # Button to trigger the API call
# if st.button("Search Jobs"):
#     try:
#         # Prepare query parameters
#         params = {}
#         if location:
#             params["location"] = location
#         if min_pay > 0:
#             params["min_pay"] = min_pay

#         # API Request
#         response = requests.get("http://api:4000/s/jobs", params=params)
#         response.raise_for_status()  # Raise exception for HTTP errors
#         job_postings = response.json()

#         # Check if results are returned
#         if job_postings:
#             st.success(f"Found {len(job_postings)} job postings.")
#             # Convert results to DataFrame and display
#             st.dataframe(job_postings)
#         else:
#             st.warning("No job postings match your criteria.")
#     except requests.RequestException as e:
#         st.error(f"An error occurred while fetching job postings: {e}")







# Company testing!


# Define the base API URL
# BASE_URL = "http://api:4000/cp"

# st.title("Test Create Company Profile")

# # Input fields for the company profile
# name = st.text_input("Company Name")
# industry = st.text_input("Industry")
# description = st.text_area("Description (Optional)")

# # Button to trigger the API call
# if st.button("Create Company Profile"):
#     # Prepare the payload
#     payload = {
#         "name": name,
#         "industry": industry,
#         "description": description if description.strip() else None
#     }
    
#     try:
#         # Send the POST request
#         response = requests.post(BASE_URL, json=payload)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         # Parse and display the response
#         st.success("Company profile created successfully!")
#         st.json(response.json())
#     except requests.RequestException as e:
#         # Display error message
#         st.error(f"Failed to create company profile: {e}")



# For this, we should be able to get the id of the current company to pass into the request.
# import requests
# import streamlit as st

# st.title("Test Update Company Profile")

# # Input fields for the company update
# company_id = st.number_input("Company ID", min_value=1, step=1, key="update_company_id")
# name = st.text_input("New Company Name")
# industry = st.text_input("New Industry")
# description = st.text_area("New Description (Optional)")

# # Button to trigger the API call
# if st.button("Update Company Profile"):
#     # Prepare the payload
#     payload = {
#         "name": name,
#         "industry": industry,
#         "description": description if description.strip() else None
#     }
    
#     try:
#         # Send the PUT request
#         response = requests.put(f"{BASE_URL}/{company_id}", json=payload)
#         response.raise_for_status()  # Raise an exception for HTTP errors

#         # Parse and display the response
#         st.success("Company profile updated successfully!")
#         st.json(response.json())
#     except requests.RequestException as e:
#         # Display error message
#         st.error(f"Failed to update company profile: {e}")


# st.title("Test Job Posting Endpoints")

# # Tabs for the two endpoints
# tabs = st.tabs(["Create Job Posting", "Update Job Posting"])

# # -------- Create Job Posting -------- #
# with tabs[0]:
#     st.header("Create Job Posting")

#     # Input fields for job posting
#     name = st.text_input("Job Name")
#     company_id = st.number_input("Company ID", min_value=1, step=1, key="create_company_id")
#     industry = st.text_input("Industry")
#     date_start = st.date_input("Start Date")
#     date_end = st.date_input("End Date")
#     minimum_gpa = st.number_input("Minimum GPA", min_value=0.0, max_value=4.0, step=0.1, key="create_min_gpa")
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     pay = st.number_input("Pay", min_value=0, step=1, key="create_pay")

#     # Location fields
#     location = {
#         "region": st.text_input("Region"),
#         "state": st.text_input("State"),
#         "zip_code": st.text_input("ZIP Code"),
#         "address_number": st.number_input("Address Number", min_value=0, step=1, key="create_address_number"),
#         "street": st.text_input("Street"),
#         "city": st.text_input("City"),
#         "country": st.text_input("Country")
#     }

#     # Skills
#     skills = st.text_input("Skills (comma-separated IDs)", key="create_skills")

#     if st.button("Create Job Posting"):
#         # Prepare the payload
#         payload = {
#             "name": name,
#             "company_id": company_id,
#             "industry": industry,
#             "date_start": str(date_start),
#             "date_end": str(date_end),
#             "minimum_gpa": minimum_gpa,
#             "title": title,
#             "description": description,
#             "pay": pay,
#             "location": location,
#             "skills": [int(skill.strip()) for skill in skills.split(",") if skill.strip()]
#         }

#         # Send the POST request
#         try:
#             response = requests.post(BASE_URL, json=payload)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#             st.success("Job posting created successfully!")
#             st.json(response.json())
#         except requests.RequestException as e:
#             st.error(f"Failed to create job posting: {e}")

# # -------- Update Job Posting -------- #
# with tabs[1]:
#     st.header("Update Job Posting")

#     # Input fields for updating job posting
#     posting_id = st.number_input("Posting ID", min_value=1, step=1, key="update_posting_id")
#     name = st.text_input("New Job Name", key="update_name")
#     industry = st.text_input("New Industry", key="update_industry")
#     date_start = st.date_input("New Start Date", key="update_start_date")
#     date_end = st.date_input("New End Date", key="update_end_date")
#     minimum_gpa = st.number_input("New Minimum GPA", min_value=0.0, max_value=4.0, step=0.1, key="update_min_gpa")
#     title = st.text_input("New Title", key="update_title")
#     description = st.text_area("New Description", key="update_description")
#     pay = st.number_input("New Pay", min_value=0, step=1, key="update_pay")
#     skills = st.text_input("New Skills (comma-separated IDs)", key="update_skills")

#     if st.button("Update Job Posting"):
#         # Prepare the payload
#         payload = {
#             "name": name,
#             "industry": industry,
#             "date_start": str(date_start),
#             "date_end": str(date_end),
#             "minimum_gpa": minimum_gpa,
#             "title": title,
#             "description": description,
#             "pay": pay,
#             "skills": [int(skill.strip()) for skill in skills.split(",") if skill.strip()]
#         }

#         # Send the PUT request
#         try:
#             response = requests.put(f"{BASE_URL}/{posting_id}", json=payload)
#             response.raise_for_status()  # Raise an exception for HTTP errors
#             st.success("Job posting updated successfully!")
#             st.json(response.json())
#         except requests.RequestException as e:
#             st.error(f"Failed to update job posting: {e}")



# st.title("Test View Applications Endpoint")

# # Input for Posting ID
# posting_id = st.number_input("Enter Posting ID:", min_value=1, step=1)

# # Button to trigger the API call
# if st.button("View Applications"):
#     if posting_id:
#         try:
#             # Make the GET request to the endpoint
#             response = requests.get(f"http://api:4000/cp/posting/{posting_id}/applications")
#             response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            
#             # Parse the response
#             data = response.json()

#             # Display the results
#             if data:
#                 st.write(f"Applications for Posting ID: {posting_id}")
#                 st.dataframe(data)
#             else:
#                 st.warning(f"No applications found for Posting ID: {posting_id}")
#         except requests.RequestException as e:
#             st.error(f"Failed to fetch applications: {e}")
#     else:
#         st.error("Please enter a valid Posting ID.")





# st.title("Test Get Company Profile Endpoint")

# # Input for Company ID
# company_id = st.number_input("Enter Company ID:", min_value=1, step=1)

# # Button to trigger the API call
# if st.button("Get Company Profile"):
#     if company_id:
#         try:
#             # Make the GET request to the endpoint
#             response = requests.get(f"http://api:4000/cp/profile/{company_id}")
#             response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            
#             # Parse the response
#             data = response.json()

#             # Check if there is an error in the response
#             if "error" in data:
#                 st.error(f"Error: {data['error']}")
#             else:
#                 # Display the company profile
#                 st.write("Company Profile:")
#                 st.json(data)  # Nicely formats the JSON response
#         except requests.RequestException as e:
#             st.error(f"Failed to fetch company profile: {e}")
#     else:
#         st.error("Please enter a valid Company ID.")















# # ------- Company test time!
# # This was tryna test all at once. I will come back to this maybe?

# # Define the base API URL
# BASE_URL = "http://api:4000/cp"

# st.title("API Testing for Companies Blueprint")

# # Tabs for different API functionalities
# tabs = st.tabs([
#     "Create Company Profile", "Update Company Profile", "Get Company Profile",
#     "Create Job Posting", "Update Job Posting", "Mark Posting as Filled",
#     "Delete Job Posting", "View Applications", "Get Student Contact"
# ])

# # -------- Create Company Profile -------- #
# with tabs[0]:
#     st.header("Create Company Profile")
#     name = st.text_input("Company Name")
#     industry = st.text_input("Industry")
#     description = st.text_area("Description")

#     if st.button("Create Company"):
#         try:
#             payload = {"name": name, "industry": industry, "description": description}
#             response = requests.post(f"{BASE_URL}/profile", json=payload)
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Update Company Profile -------- #
# with tabs[1]:
#     st.header("Update Company Profile")
#     company_id = st.number_input("Company ID", min_value=1, step=1, key='update_company')
#     name = st.text_input("New Company Name")
#     industry = st.text_input("New Industry")
#     description = st.text_area("New Description")

#     if st.button("Update Company"):
#         try:
#             payload = {"name": name, "industry": industry, "description": description}
#             response = requests.put(f"{BASE_URL}/profile/{company_id}", json=payload)
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Get Company Profile -------- #
# with tabs[2]:
#     st.header("Get Company Profile")
#     company_id = st.number_input("Company ID", min_value=1, step=1, key='get_company')

#     if st.button("Fetch Company Profile"):
#         try:
#             response = requests.get(f"{BASE_URL}/profile/{company_id}")
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Create Job Posting -------- #
# with tabs[3]:
#     st.header("Create Job Posting")
#     name = st.text_input("Job Name")
#     industry = st.text_input("Industry")
#     location = {
#         "region": st.text_input("Region"),
#         "state": st.text_input("State"),
#         "zip_code": st.text_input("ZIP Code"),
#         "address_number": st.number_input("Address Number", step=1, key='address_number'),
#         "street": st.text_input("Street"),
#         "city": st.text_input("City"),
#         "country": st.text_input("Country")
#     }
#     date_start = st.date_input("Start Date")
#     date_end = st.date_input("End Date")
#     minimum_gpa = st.number_input("Minimum GPA", min_value=0.0, max_value=4.0, step=0.1, key='gpa')
#     title = st.text_input("Title")
#     description = st.text_area("Description")
#     pay = st.number_input("Pay", step=1, key='pay')
#     skills = st.text_input("Skills (comma-separated)")

#     if st.button("Create Posting"):
#         try:
#             payload = {
#                 "company_id": company_id,
#                 "name": name,
#                 "industry": industry,
#                 "location": location,
#                 "date_start": str(date_start),
#                 "date_end": str(date_end),
#                 "minimum_gpa": minimum_gpa,
#                 "title": title,
#                 "description": description,
#                 "pay": pay,
#                 "skills": [int(skill.strip()) for skill in skills.split(",") if skill.strip()]
#             }
#             response = requests.post(f"{BASE_URL}/posting", json=payload)
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Update Job Posting -------- #
# with tabs[4]:
#     st.header("Update Job Posting")
#     posting_id = st.number_input("Posting ID", min_value=1, step=1, key='postingID')
#     name = st.text_input("New Job Name")
#     industry = st.text_input("New Industry")
#     date_start = st.date_input("New Start Date")
#     date_end = st.date_input("New End Date")
#     minimum_gpa = st.number_input("New Minimum GPA", min_value=0.0, max_value=4.0, step=0.1, key='GPA2')
#     title = st.text_input("New Title")
#     description = st.text_area("New Description")
#     pay = st.number_input("New Pay", step=1, key='PAY2')
#     skills = st.text_input("New Skills (comma-separated)")

#     if st.button("Update Posting"):
#         try:
#             payload = {
#                 "name": name,
#                 "industry": industry,
#                 "date_start": str(date_start),
#                 "date_end": str(date_end),
#                 "minimum_gpa": minimum_gpa,
#                 "title": title,
#                 "description": description,
#                 "pay": pay,
#                 "skills": [int(skill.strip()) for skill in skills.split(",") if skill.strip()]
#             }
#             response = requests.put(f"{BASE_URL}/posting/{posting_id}", json=payload)
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Mark Posting as Filled -------- #
# with tabs[5]:
#     st.header("Mark Posting as Filled")
#     posting_id = st.number_input("Posting ID", min_value=1, step=1, key='POSTINGID2')

#     if st.button("Mark as Filled"):
#         try:
#             response = requests.put(f"{BASE_URL}/posting/{posting_id}/filled")
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Delete Job Posting -------- #
# with tabs[6]:
#     st.header("Delete Job Posting")
#     posting_id = st.number_input("Posting ID", min_value=1, step=1, key='DeleteJob')

#     if st.button("Delete Posting"):
#         try:
#             response = requests.delete(f"{BASE_URL}/posting/{posting_id}")
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- View Applications for a Posting -------- #
# with tabs[7]:
#     st.header("View Applications")
#     posting_id = st.number_input("Posting ID", min_value=1, step=1, key='POSTINGID3')

#     if st.button("View Applications"):
#         try:
#             response = requests.get(f"{BASE_URL}/posting/{posting_id}/applications")
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")

# # -------- Get Student Contact -------- #
# with tabs[8]:
#     st.header("Get Student Contact")
#     student_id = st.number_input("Student ID", min_value=1, step=1, key='student_contact')

#     if st.button("Get Contact Info"):
#         try:
#             response = requests.get(f"{BASE_URL}/student/{student_id}/contact")
#             st.json(response.json())
#         except Exception as e:
#             st.error(f"Error: {e}")







# Tests for advisors

# st.title("Test Get Advisor's Students Endpoint")

# # Input for Advisor ID
# advisor_id = st.number_input("Enter Advisor ID:", min_value=1, step=1)

# # Button to trigger the API call
# if st.button("Get Students for Advisor"):
#     if advisor_id:
#         try:
#             # Make the GET request to the endpoint
#             response = requests.get(f"http://api:4000/ad/students/{advisor_id}")
#             response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            
#             # Parse the response
#             data = response.json()

#             # Check if data is empty or contains an error
#             if "error" in data:
#                 st.error(f"Error: {data['error']}")
#             elif not data:
#                 st.warning(f"No students found for Advisor ID: {advisor_id}")
#             else:
#                 # Display the results in a nicely formatted DataFrame
#                 st.write(f"Students under Advisor ID: {advisor_id}")
#                 st.dataframe(data)
#         except requests.RequestException as e:
#             st.error(f"Failed to fetch students: {e}")
#     else:
#         st.error("Please enter a valid Advisor ID.")



# Set the Streamlit page title
# st.title("Test Advisor Statistics Route")

# # Input field for advisor_id
# advisor_id = st.number_input("Enter Advisor ID:", min_value=1, step=1, value=1)

# # Button to trigger API request
# if st.button("Get Advisor Statistics"):
#     try:
#         # Define the API URL for the route
#         url = f"http://api:4000/ad/statistics/{advisor_id}"
        
#         # Make the GET request
#         response = requests.get(url)
        
#         # Check the response status code
#         if response.status_code == 200:
#             # Parse the JSON response
#             data = response.json()
            
#             # Display status statistics
#             st.subheader("Status Statistics")
#             status_stats = data.get("status_statistics", {})
#             st.write(f"Total Students: {status_stats.get('Total_Students', 'N/A')}")
#             st.write(f"Placed Students: {status_stats.get('Placed_Students', 'N/A')}")
#             st.write(f"Searching Students: {status_stats.get('Searching_Students', 'N/A')}")
            
#             # Display application statistics
#             st.subheader("Application Statistics")
#             app_stats = data.get("application_statistics", [])
#             if app_stats:
#                 st.write(f"Total Applications: {sum([row['Applications_Count'] for row in app_stats])}")
#                 st.write(f"Students Applied: {sum([row['Students_Applied'] for row in app_stats])}")
#                 st.write(f"Avg Applications Per Student: {app_stats[0].get('Avg_Applications_Per_Student', 'N/A')}")
#             else:
#                 st.write("No application statistics available.")
        
#         else:
#             # Display error message if the request fails
#             st.error(f"Failed to fetch statistics: {response.status_code} {response.reason}")
#             st.write(response.text)
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")



# Set the Streamlit page title
st.title("Test Filled Positions Route")

# Button to trigger API request
if st.button("Get Filled Positions"):
    try:
        # Define the API URL for the route
        url = f"http://api:4000/ad/positions/filled/25"
        
        # Make the GET request
        response = requests.get(url)
        
        # Check the response status code
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Display the results
            st.subheader("Filled Positions")
            if data:
                # Create a data table
                st.dataframe(data)
            else:
                st.write("No filled positions found.")
        
        else:
            # Display error message if the request fails
            st.error(f"Failed to fetch filled positions: {response.status_code} {response.reason}")
            st.write(response.text)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")