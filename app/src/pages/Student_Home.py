import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

BASE_URL = "http://web-api:4000/st"
BASE_URL = "http://web-api:4000/st/postings"

# Function to fetch job data by location
def fetch_jobs_by_location(location):
    response = requests.get(f"{BASE_URL}/by_location?location={location}")
    return response.json() if response.status_code == 200 else []

# Function to fetch job data by minimum pay
def fetch_jobs_by_pay(min_pay):
    response = requests.get(f"{BASE_URL}/by_pay?min_pay={min_pay}")
    return response.json() if response.status_code == 200 else []

# Function to fetch a specific job by ID
def fetch_job_by_id(job_id):
    response = requests.get(f"{BASE_URL}/{job_id}")
    return response.json() if response.status_code == 200 else {}

# # Initialize session state
# if "locations" not in st.session_state:
#     st.session_state["locations"] = []  # Initialize with an empty list

# Streamlit UI
st.title("Career Compass")

# Job search by ID
st.header("Search for a Specific Job")
job_id = st.text_input("Enter Job ID:")
if job_id:
    job_details = fetch_job_by_id(job_id)
    if job_details:
        st.subheader(f"Job Details for ID {job_id}")
        st.write(job_details)
    else:
        st.error("No job found with this ID.")

st.header("Filter Jobs")

# Filter by city
city_filter = st.text_input("Filter by City (press Enter):")
if city_filter:
    jobs = fetch_jobs_by_location(city_filter)
    if jobs:
        st.subheader(f"Jobs in {city_filter}")
        for job in jobs:
            if st.button(f"{job['Title']} | {job['Company_Name']}"):
                st.write(job)
    else:
        st.error("No jobs found in this location.")

# Filter by minimum pay
pay_filter = st.text_input("Filter by Minimum Pay:")
if pay_filter:
    try:
        pay_filter = float(pay_filter)
        jobs = fetch_jobs_by_pay(pay_filter)
        if jobs:
            st.subheader(f"Jobs with Minimum Pay of ${pay_filter}")
            for job in jobs:
                if st.button(f"{job['Title']} | {job['Company_Name']}"):
                    st.write(job)
        else:
            st.error("No jobs found with this pay range.")
    except ValueError:
        st.error("Please enter a valid pay amount.")

job_col, details_col = st.columns([2, 3])

with job_col:
    st.markdown("### Job Postings")
    for job in jobs:
        if st.button(job["Title"] + " | " + job["Company_Name"], key=job["ID"]):
            st.session_state["selected_job"] = job  # Update session state with the selected job
            st.rerun()

# Job Details Column
with details_col:
    selected_job = st.session_state.get("selected_job", {})
    if selected_job:
        st.markdown("### Job Details")
        st.markdown(f"**Job Title:** {selected_job.get('Title', 'N/A')}")
        st.write(f"**Company Name:** {selected_job.get('Company_Name', 'N/A')}")
        st.write(f"**Job Description:** {selected_job.get('Description', 'N/A')}")
        st.write(f"**City:** {selected_job.get('City', 'N/A')}")
    else:
        st.markdown("### Select a Job to View Details")