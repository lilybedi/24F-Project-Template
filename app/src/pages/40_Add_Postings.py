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
        st.success("Job posting created successfully!")
    else:
        st.error(f"Failed to create job posting: {response.status_code} - {response.json().get('error', 'Unknown error')}")

# Initialize session state for job data
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Position Name"

if "required_skills" not in st.session_state:
    st.session_state["required_skills"] = []

if "description" not in st.session_state:
    st.session_state["description"] = ""

if "pay" not in st.session_state:
    st.session_state["pay"] = 0

if "location" not in st.session_state:
    st.session_state["location"] = "City, State"

if "minimum_gpa" not in st.session_state:
    st.session_state["minimum_gpa"] = 3.0  # Default minimum GPA value

# Header Section
st.markdown("## Create Job Posting")
st.divider()

# Job Posting Form
st.markdown("### Job Details")

# Title and Pay
st.text_input("Position Title", key="position_title")
st.number_input("Pay (in USD)", min_value=0, step=1, key="pay")
st.text_input("Location (City, State)", key="location")

# Minimum GPA Requirement
st.number_input(
    "Minimum GPA Requirement", min_value=0.0, max_value=4.0, step=0.1, key="minimum_gpa"
)

# Required Skills
st.markdown("**Required Skills:**")

# Display each skill with a remove button
skills_to_remove = []
for i, skill in enumerate(st.session_state["required_skills"]):
    cols = st.columns([4, 1])  # Create two columns: one for skill, one for the button
    cols[0].write(f"- {skill}")
    if cols[1].button(f"Remove", key=f"remove_skill_{i}"):
        skills_to_remove.append(skill)

# Remove selected skills
if skills_to_remove:
    for skill in skills_to_remove:
        st.session_state["required_skills"].remove(skill)
    st.rerun()

# Add new skill using dynamic key
skill_input_key = f"new_skill_{len(st.session_state['required_skills'])}"  # Dynamic key for text input
new_skill = st.text_input("Add Required Skill", key=skill_input_key)
if st.button("Add Skill"):
    if new_skill:  # Check if the input is not empty
        st.session_state["required_skills"].append(new_skill)
        st.rerun()

# Job Description
st.text_area("Job Description", value=st.session_state["description"], key="description")

# Submit Button
if st.button("Submit Job Posting"):
    job_data = {
        "title": st.session_state["position_title"],
        "pay": st.session_state["pay"],
        "location": st.session_state["location"],
        "required_skills": st.session_state["required_skills"],
        "description": st.session_state["description"],
        "minimum_gpa": st.session_state["minimum_gpa"],  # Added Minimum GPA Requirement
    }
    create_job_posting(job_data)

# Divider
st.divider()
