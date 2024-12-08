import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Define the base URL for the API
BASE_URL = "http://api:4000/s"  # Updated to use '/s' prefix for student routes

# Function to fetch job postings from the backend
def fetch_jobs(location=None, min_pay=None):
    params = {}
    if location:
        params["location"] = location
    if min_pay is not None:
        params["min_pay"] = min_pay

    try:
        response = requests.get(f"{BASE_URL}/postings/by_pay", params=params)
        st.write(f"Attempting to fetch from: {BASE_URL}/postings/by_pay")  # Debug line
        st.write(f"With params: {params}")  # Debug line

        response.raise_for_status()  # Raise exception for HTTP errors

        st.write(f"Response status code: {response.status_code}")  # Debug line
        if response.status_code != 200:
            st.write(f"Response text: {response.text}")  # Debug line
            response.raise_for_status()
        return response.json()  # Return the job postings
    except requests.RequestException as e:
        st.error(f"Failed to fetch job postings: {e}")
        return []

# Fetch initial job postings without filters
job_postings = fetch_jobs()

# Header Section: Navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #d3d3d3;
        padding: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 18px;
        font-weight: bold;
    }
    .navbar div {
        display: inline-block;
    }

    .search-bar {
        flex-grow: 1;
        margin: 0 20px;
        display: flex;
        align-items: center;
    }

    .button-row {
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    .button-row button {
        border: none;
        margin: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>

    <div class="navbar">
        <div>Career Compass</div>
        <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

filter_col, sort_col = st.columns([2, 1])

# Filter Options
with filter_col:
    st.markdown("**Filter**")
    with st.expander("Filter by"):
        selected_filter = st.selectbox("Choose a filter", ["Pay", "Location"], key="filter_select")

        if selected_filter == "Pay":
            min_pay = st.number_input("Minimum Pay", min_value=0, step=1, key="pay_filter")
        elif selected_filter == "Location":
            location = st.text_input("Enter Location (City, State, or Country)", key="location_filter")

        if st.button("Apply Filter"):
            # Fetch filtered jobs
            job_postings = fetch_jobs(
                location=st.session_state.get("location_filter"),
                min_pay=st.session_state.get("pay_filter"),
            )

st.divider()

# Initialize session state for the selected job
if "selected_job" not in st.session_state and job_postings:
    st.session_state["selected_job"] = job_postings[0]

job_col, details_col = st.columns([2, 3])

# Job Postings Column
with job_col:
    st.markdown("### Job Postings")
    for job in job_postings:
        if st.button(job["Job_Title"], key=job["Posting_ID"]):
            st.session_state["selected_job"] = job  # Update session state with the selected job

# Job Details Column
with details_col:
    selected_job = st.session_state.get("selected_job")
    if selected_job:
        st.markdown("### Job Details")
        st.markdown(f"**Job Title:** {selected_job['Job_Title']}")
        st.markdown(f"**Company Name:** {selected_job['Company_Name']}")
        st.markdown(f"**Job Description:** {selected_job['Job_Description']}")
        st.markdown(f"**Location:** {selected_job['City']}, {selected_job['State']}, {selected_job['Country']}")
        st.markdown(f"**Salary:** ${selected_job['Salary']}")
        st.markdown(f"**Start Date:** {selected_job['Start_Date']}")
        st.markdown(f"**End Date:** {selected_job['End_Date']}")
    else:
        st.write("No job selected.")
