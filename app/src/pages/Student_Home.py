import streamlit as st
import requests

from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()
BASE_URL = "http://web-api:4000/st"

# Initialize session state for locations and pay thresholds
if "locations" not in st.session_state:
    st.session_state["locations"] = []  # Initialize with an empty list

if "pay_threshold" not in st.session_state:
    st.session_state["pay_threshold"] = 15  # Default minimum pay

# Default minimum pay
DEFAULT_MIN_PAY = 15
min_pay = DEFAULT_MIN_PAY  # Initialize to default value

# Fetch existing locations and job postings
try:
    response = requests.get(f"{BASE_URL}/postings/by_location")
    response.raise_for_status()
    locations = response.json()  # Assuming the API returns a list of locations

    # Fetch job postings with default minimum pay
    response = requests.get(f"{BASE_URL}/postings/by_pay?min_pay={min_pay}")
    response.raise_for_status()
    job_postings = response.json()

except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch data: {e}")
    locations = []
    job_postings = []

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

    # Dropdown for filtering and adding new locations
    with st.expander("Filter by Location"):
        selected_location = st.selectbox(
            "Select a Location",
            ["All Locations"] + st.session_state["locations"],
            key="location_filter",
        )
        # Input field for adding a new location
        new_location = st.text_input("Add a New Location")
        if new_location:
            if new_location not in st.session_state["locations"]:
                st.session_state["locations"].append(new_location)
                st.success(f"Added new location: {new_location}")
            else:
                st.warning(f"Location '{new_location}' already exists.")

    # Dropdown for filtering and adding a pay threshold
    with st.expander("Filter by Minimum Pay"):
        min_pay = st.number_input(
            "Set Minimum Pay Threshold",
            value=st.session_state["pay_threshold"],
            step=1,
            min_value=0,
            key="min_pay_filter",
        )
        # Update session state for pay threshold
        st.session_state["pay_threshold"] = min_pay

st.divider()

# Update job postings based on filters
try:
    query_params = f"?min_pay={min_pay}"
    if selected_location and selected_location != "All Locations":
        query_params += f"&location={selected_location}"

    response = requests.get(f"{BASE_URL}/postings/by_pay{query_params}")
    response.raise_for_status()
    job_postings = response.json()

except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch filtered jobs: {e}")
    job_postings = []

# Display Job Postings and Details
job_col, details_col = st.columns([2, 3])

# Job Postings Column
with job_col:
    st.markdown("### Job Postings")
    for job in job_postings:
        if st.button(job["Title"] + " | " + job["Company_Name"], key=job["ID"]):  # Each job title is a button
            st.session_state["selected_job"] = job  # Update session state with the selected job

# Job Details Column
with details_col:
    selected_job = st.session_state.get("selected_job", {})
    if selected_job:
        st.markdown("### Job Details")
        st.markdown(f"**Job Title:** {selected_job.get('Title', 'N/A')}")
        st.write(f"**Company Name:** {selected_job.get('Company_Name', 'N/A')}")
        st.write(f"**Job Description:** {selected_job.get('Description', 'N/A')}")
    else:
        st.markdown("### Select a Job to View Details")