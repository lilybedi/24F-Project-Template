import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

BASE_URL = "http://web-api:4000"

# Function to create a job posting
def create_job_posting(job_data):
    response = requests.post(f"{BASE_URL}/postings/create", json=job_data)
    if response.status_code == 201:
        st.success("Job added to profile!")
    else:
        st.error(f"Failed to add to profile: {response.status_code} - {response.json().get('error', 'Unknown error')}")

# Initialize session state for position data
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Position Name"

if "description" not in st.session_state:
    st.session_state["description"] = ""

if "pay" not in st.session_state:
    st.session_state["pay"] = 0

if "location" not in st.session_state:
    st.session_state["location"] = "City, State"

# Header Section
st.markdown("## List a co-op position")
st.divider()

# Job Posting Form
st.markdown("### Job Details")

# Title and Pay
st.text_input("Position Title", key="position_title")
st.number_input("Pay (in USD)", min_value=0, step=1, key="pay")
st.text_input("Location (City, State)", key="location")

# Job Description
st.text_area("Job Description", value=st.session_state["description"], key="description")

# # Job review
# st.text_area("Job review (what did you think?)", value=st.session_state["review"], key="review")

def add_alumni_position(alumn_id, position_data): 
    response = requests.post(f"{BASE_URL}/alumni/{alumn_id}/add_position", json=position_data) 
    if response.status_code == 200: 
        st.success("Position added to alumnus profile!") 
    else: 
        st.error(f"Failed to add position: {response.status_code} - {response.json().get('error', 'Unknown error')}")

# Submit Button
if st.button("Add to profile"):
    job_data = {
        "alumn_ID": st.session_state["alumnID"],
        "title": st.session_state["position_title"],
        "pay": st.session_state["pay"],
        "location": st.session_state["location"],
        "required_skills": st.session_state["required_skills"],
        "description": st.session_state["description"],
    }
    add_alumni_position(job_data)

# Divider
st.divider()
