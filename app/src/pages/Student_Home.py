import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar
SideBarLinks()

BASE_URL = "http://web-api:4000/st/postings"

#  Data by loc
def fetch_jobs_by_location(location):
    response = requests.get(f"{BASE_URL}/by_location?location={location}")
    if response.status_code == 200:
        return response.json()
    else:
        return []

# Data by pay
def fetch_jobs_by_pay(min_pay):
    response = requests.get(f"{BASE_URL}/by_pay?min_pay={min_pay}")
    if response.status_code == 200:
        return response.json()
    else:
        return []

st.title("Career Compass")
st.header("Filter Jobs")

# All jobs
all_jobs = fetch_jobs_by_pay(0)

# City
city_filter = st.text_input("Filter by City (press Enter):")
filtered_by_city = all_jobs
if city_filter:
    filtered_by_city = fetch_jobs_by_location(city_filter)

# Minimum pay
pay_filter = st.text_input("Filter by Minimum Pay:")
filtered_jobs = filtered_by_city
if pay_filter:
    try:
        pay_filter = float(pay_filter)
        filtered_jobs = [job for job in filtered_by_city if job["Pay"] >= pay_filter]
    except ValueError:
        st.error("Please enter a valid pay amount.")

job_col, details_col = st.columns([2, 3])

with job_col:
    st.markdown("### Job Postings")
    for job in filtered_jobs:
        if st.button(job["Title"] + " | " + job["Company_Name"], key=job["ID"]):
            st.session_state["selected_job"] = job  # Update session state with the selected job
            st.rerun()

# Job details
with details_col:
    selected_job = st.session_state.get("selected_job", {})
    if selected_job:
        st.markdown("### Job Details")
        st.markdown(f"**Job Title:** {selected_job.get('Title', 'N/A')}")
        st.write(f"**Company Name:** {selected_job.get('Company_Name', 'N/A')}")
        st.write(f"**Job Description:** {selected_job.get('Description', 'N/A')}")
        st.write(f"**City:** {selected_job.get('City', 'N/A')}")
        st.write(f"**Pay:** ${selected_job.get('Pay', 'N/A')}")
    else:
        st.markdown("### Select a Job to View Details")