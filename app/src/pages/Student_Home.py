import streamlit as st
import requests

from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

BASE_URL = "http://web-api:4000/st"

# Initialize session state for locations, pay threshold, and selected parameters
if "locations" not in st.session_state:
    st.session_state["locations"] = []  # Initialize with an empty list

if "pay_threshold" not in st.session_state:
    st.session_state["pay_threshold"] = 15  # Default minimum pay

if "selected_location" not in st.session_state:
    st.session_state["selected_location"] = "All Locations"  # Default location

# Fetch existing locations from API
try:
    response = requests.get(f"{BASE_URL}/postings/by_location")
    response.raise_for_status()
    st.session_state["locations"] = list(set(st.session_state["locations"] + response.json()))
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch locations: {e}")

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
    </style>

    <div class="navbar">
        <div>Career Compass</div>
        <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# Filters Section
with st.container():
    st.header("Filters")

    # Dropdown for filtering locations
    selected_location = st.selectbox(
        "Select a Location",
        ["All Locations"] + st.session_state["locations"],  # Sorted locations
        index=0 if st.session_state["selected_location"] == "All Locations"
        else st.session_state["locations"].index(st.session_state["selected_location"]) + 1,
        key="location_filter",
    )

    # Update session state if location changes
    if selected_location != st.session_state["selected_location"]:
        st.session_state["selected_location"] = selected_location
        st.rerun()

    # Input field for adding a new location
    new_location = st.text_input("Add a New Location", key="new_location_input")
    if new_location:
        if new_location not in st.session_state["locations"]:
            st.session_state["locations"].append(new_location)
            st.session_state["locations"].sort()  # Keep locations sorted
            st.success(f"Added new location: {new_location}")
            st.rerun()


# Fetch existing locations (cities) from API
try:
    response = requests.get(f"{BASE_URL}/postings/by_location")
    response.raise_for_status()
    # Extract and deduplicate cities from the API response
    locs = []
    for job in response.json():
        if (job["City"] == st.session_state["locations"]):
            locs.append(job)
    st.session_state["locations"] = locs

except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch locations: {e}")


# Fetch job postings based on filters
try:
    query_params = f"?min_pay={st.session_state['pay_threshold']}"
    if st.session_state["selected_location"] != "All Locations":
        query_params += f"&location={st.session_state['selected_location']}"
    response = requests.get(f"{BASE_URL}/postings/by_pay{query_params}")
    response.raise_for_status()
    job_postings = response.json()
except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch filtered jobs: {e}")
    job_postings = []

# Display Job Postings
job_col, details_col = st.columns([2, 3])

with job_col:
    st.markdown("### Job Postings")
    for job in job_postings:
        if st.button(job["Title"] + " | " + job["Company_Name"], key=job["ID"]):
            st.session_state["selected_job"] = job  # Update session state with the selected job
            st.rerun()  # Refresh to show job details immediately

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