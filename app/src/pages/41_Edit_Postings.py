import streamlit as st
from modules.nav import SideBarLinks
import requests
st.set_page_config(layout="wide")

# Sidebar navigation
SideBarLinks()

# Sample job postings data
job_postings = [
    {"id": "#001", "job_title": "Data Analyst", "job_description": "Analyze data trends and insights", "min_gpa": "3.5", "grad_year": "2024", "college": "Engineering", "skills": "Python, SQL, Data Analysis"},
    {"id": "#002", "job_title": "HR Coordinator", "job_description": "Coordinate HR processes and hiring", "min_gpa": "3.0", "grad_year": "2023", "college": "Business", "skills": "Communication, Recruitment, Leadership"},
    {"id": "#003", "job_title": "CEO", "job_description": "Lead the organization strategically", "min_gpa": "3.7", "grad_year": "2025", "college": "Science", "skills": "Management, Strategy, Decision Making"},
    {"id": "#004", "job_title": "CFO", "job_description": "Manage corporate financials", "min_gpa": "3.8", "grad_year": "2024", "college": "Engineering", "skills": "Accounting, Finance, Leadership"},
]

# UI Header Section
st.markdown("## Manage Job Postings")
st.divider()

# Display each job posting with fields defaulted to closed (unopened)
for idx, job in enumerate(st.session_state.job_postings):
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

        # Remove Job Posting Button
        if st.button("Close posting", key=f"remove_{idx}"):
            # Remove the job posting from the list
            st.session_state.job_postings = [j for j in st.session_state.job_postings if j['id'] != job['id']]
            st.success(f"Posting closed: {job['job_title']}")

