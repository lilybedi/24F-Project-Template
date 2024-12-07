import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

BASE_URL = "http://web-api:4000"

# Function to fetch applications for a job post
def fetch_applications():
    if job_id:
        # real response 
        response = 1
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching applications: {response.status_code}")
        return []

# Sample Data for Testing - chatgpt
applications = [
    {"id": "#8675309", "job": "Data Analyst", "gpa": "3.76", "applicant_name": "John Doe"},
    {"id": "#2010178", "job": "HR", "gpa": "3.91", "applicant_name": "Jane Smith"},
    {"id": "#9238483", "job": "CEO", "gpa": "3.81", "applicant_name": "Robert Brown"},
    {"id": "#7489234", "job": "CFO", "gpa": "4.0", "applicant_name": "Emily Davis"},
]

# Header Section
st.markdown("## View Job Applications")
st.divider()


# Applications Table
left_col, right_col = st.columns([1.5, 3.5])

with left_col:
    st.markdown("### Filters")
    sort_option = st.selectbox("Sort By:", ["GPA"], key="sort_option") # add skills match if we have time

    # Apply sorting thanks https://pythonhow.com/how/sort-a-list-of-dictionaries-by-a-value-of-the-dictionary/
    applications.sort(key=lambda x: float(x["gpa"]), reverse=True)

with right_col:
    st.markdown("### Applications")
    if not applications:
        st.write("No applications found for this job.")
    else:
        for app in applications:
            app_col1, app_col2, app_col3, app_col4 = st.columns([1, 1, 1, 2])
            with app_col1:
                st.write(app["id"])
            with app_col2:
                st.write(app["gpa"])
            with app_col3:
                st.write(app["job"])
            with app_col4:
                st.button(f"View {app['applicant_name']}'s Application →", key=f"view_{app['id']}")
