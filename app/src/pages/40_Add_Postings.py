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

# Initialize session state for position data
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Position Name"

if "required_skills" not in st.session_state:
    st.session_state["required_skills"] = ["Skill 1", "Skill 2", "Skill 3"]

if "description" not in st.session_state:
    st.session_state["description"] = ""

if "pay" not in st.session_state:
    st.session_state["pay"] = 0

if "location" not in st.session_state:
    st.session_state["location"] = "City, State"

# Header Section
st.markdown("## Create Job Posting")
st.divider()

# Job Posting Form
st.markdown("### Job Details")

# Title and Pay
st.text_input("Position Title", key="position_title")
st.number_input("Pay (in USD)", min_value=0, step=1, key="pay")
st.text_input("Location (City, State)", key="location")

# Required Skills
st.markdown("**Required Skills:**")
for skill in st.session_state["required_skills"]:
    st.write(f"- {skill}")

new_skill = st.text_input("Add Required Skill +", key="new_skill_input")
if st.button("Add Skill"):
    if new_skill:
        st.session_state["required_skills"].append(new_skill)
        st.experimental_rerun()

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
    }
    create_job_posting(job_data)

# Divider
st.divider()
