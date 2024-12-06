import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Student, {st.session_state['first_name']}.")
import streamlit as st


BASE_URL = "http://web-api:4000"

# Function to fetch job postings from the backend
def fetch_jobs():
    params = {}
    response = requests.get(f"{BASE_URL}/postings/by_pay", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching jobs: {response.status_code}")
        return []

# Fetch initial job postings (default)
job_postings = fetch_jobs()
# TODO: Figure out why job_postings is yielding no results

job_postings = [{"id": 0, "title": "Software developer", "company": "Streamlit", "description": "Fix our company"}]

# Header Section: Navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #d3d3d3; /* Light gray background for the navbar */
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
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="navbar">
        <div>Career Compass</div>
        <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.divider()

sort_col = st.container()

with sort_col:
    st.markdown("**Sort By**")
    sort_by = st.selectbox("Sort By", ["Relevance", "Date Applied", "Company"], key="sort_by")

st.divider()

# Tab Navigation
tabs = st.tabs(["Job Search", "Job Applications", "Alumni Network"])

with tabs[0]:
    # Get first job
    if "selected_job" not in st.session_state:
        st.session_state["selected_job"] = job_postings[0] 

    job_col, details_col = st.columns([2, 3])
    # Job Postings
    with job_col:
        st.markdown("### Job Postings")
        for job in job_postings:
            if st.button(job["title"], key=job["id"]):  # Each job title is a button
                st.session_state["selected_job"] = job  # Update session state with the selected job

    # Right Column: Job Details
    with details_col:
        selected_job = st.session_state["selected_job"]  # Get the selected job from session state
        st.markdown("### Job Details")
        st.markdown(f"**Job Title:** {selected_job['title']}")
        st.write(f"**Company Name:** {selected_job['company']}")
        st.write(f"**Job Description:** {selected_job['description']}")
