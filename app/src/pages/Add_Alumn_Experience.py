import datetime
import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar navigation
SideBarLinks()

# Base API URL
BASE_URL = "http://api:4000"

# Function to add a position to the alumni's profile
def add_alumni_position(alumni_id, position_data):
    """Make a POST request to add a position to an alumni's profile."""
    try:
        st.write("Payload being sent to the backend:", position_data)
        response = requests.post(f"{BASE_URL}/a/{alumni_id}/positions", json=position_data)
        if response.status_code == 201:
            st.success("Position added to alumni profile!")
        else:
            error_message = response.json().get("error", "Unknown error")
            st.error(f"Failed to add position: {response.status_code} - {error_message}")
    except requests.RequestException as e:
        st.error(f"An error occurred: {e}")

# Retrieve the alumni ID from session state
if "alumni_id" not in st.session_state:
    st.session_state["alumni_id"] = 1  # Replace with dynamic alumni ID retrieval

alumni_id = st.session_state["alumni_id"]

# Initialize session state for job data
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Position Title"

if "company_name" not in st.session_state:
    st.session_state["company_name"] = "Company Name"

if "pay" not in st.session_state:
    st.session_state["pay"] = 0

if "date_start" not in st.session_state:
    st.session_state["date_start"] = None

if "date_end" not in st.session_state:
    st.session_state["date_end"] = None

if "city" not in st.session_state:
    st.session_state["city"] = ""

if "state" not in st.session_state:
    st.session_state["state"] = ""

if "country" not in st.session_state:
    st.session_state["country"] = ""

if "description" not in st.session_state:
    st.session_state["description"] = ""

if "skills" not in st.session_state:
    st.session_state["skills"] = ""

# Header Section
st.markdown("## Add a Position to Your Profile")
st.divider()

# Job Posting Form
st.markdown("### Position Details")

# Input Fields
st.text_input("Position Title", key="position_title")
st.text_input("Company Name", key="company_name")
st.text_input("Industry", key="industry")  # New field for industry
st.number_input("Pay (in USD)", min_value=0, step=1, key="pay")
st.date_input("Start Date", key="date_start", value=st.session_state["date_start"] or datetime.date.today())
st.date_input("End Date (Optional)", key="date_end", value=st.session_state["date_end"])
st.text_input("City", key="city")
st.text_input("State", key="state")
st.text_input("Country", key="country")
st.text_area("Description", key="description")
st.text_input("Required Skills (comma-separated)", key="skills")

# Submit button
if st.button("Add to Profile"):
    job_data = {
        "title": st.session_state["position_title"],
        "company_name": st.session_state["company_name"],
        "industry": st.session_state.get("industry", ""),  # Add industry
        "pay": st.session_state["pay"],
        "date_start": st.session_state["date_start"].strftime('%Y-%m-%d'),
        "date_end": st.session_state["date_end"].strftime('%Y-%m-%d'),
        "city": st.session_state["city"],
        "state": st.session_state["state"],
        "country": st.session_state["country"],
        "description": st.session_state["description"],
        "skills": st.session_state["skills"].split(",") if st.session_state["skills"] else []
    }
    add_alumni_position(alumni_id, job_data)
    st.switch_page("pages/Alumn_Home.py")


# Divider
st.divider()
