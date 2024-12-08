import streamlit as st
from modules.nav import SideBarLinks
import requests
st.set_page_config(layout="wide")

# Sidebar navigation
SideBarLinks()

BASE_URL = "http://web-api:4000"

# Function to retrieve job postings from the API
def get_job_postings():
    try:
        response = requests.get(f"{BASE_URL}/c/company/")
        response.raise_for_status()
        return response.json()  # Return the job postings as JSON
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching job postings: {e}")
        return []
    
job_postings = get_job_postings()

# Function to update a job posting
def update_job_posting(job_data):
    try: 
        response = requests.post(f"{BASE_URL}/postings/{job_data['id']}", json=job_data)
        response.raise_for_status()
        return response.json()  # Assuming the API returns the updated data as JSON
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

# UI Header Section
st.markdown("## Manage Job Postings")
st.divider()

# Display each job posting with fields defaulted to closed (unopened)
for idx, job in enumerate(job_postings):
    # Each job's details are hidden by default until the user clicks to open
    with st.expander(job['job_title'], expanded=False):  # Default as closed
        # Editable fields for each job posting
        new_id = st.text_input(
            "Job ID",
            value=job["id"],
            key=f"id_{idx}"
        )
        new_description = st.text_area(
            "Job Description",
            value=job["job_description"],
            key=f"description_{idx}"
        )
        new_min_gpa = st.number_input(
            "Minimum GPA Requirement",
            min_value=0.0,
            max_value=4.0,
            step=0.1,
            value=float(job["min_gpa"]),
            key=f"gpa_{idx}"
        )
        new_grad_year = st.selectbox(
            "Graduation Year Requirement",
            options=["2023", "2024", "2025", "2026"],
            index=["2023", "2024", "2025", "2026"].index(job["grad_year"]),
            key=f"grad_year_{idx}"
        )
        new_college = st.text_input(
            "College Requirement",
            value=job["college"],
            key=f"college_{idx}"
        )
        new_skills = st.text_area(
            "Skills Required (comma-separated)",
            value=job["skills"],
            key=f"skills_{idx}"
        )

        # Save Changes Button
        if st.button("Save Changes", key=f"save_{idx}"):
            job["id"] = new_id
            job["job_description"] = new_description
            job["min_gpa"] = str(new_min_gpa)
            job["grad_year"] = new_grad_year
            job["college"] = new_college
            job["skills"] = new_skills
            st.success(f"Changes saved for: {job['job_title']}")
