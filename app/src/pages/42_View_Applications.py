import streamlit as st
from modules.nav import SideBarLinks
from urllib.parse import quote

st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged-in user
SideBarLinks()

# Sample data
applications = [
    {
        "id": "#8675309",
        "job": "Data Analyst",
        "gpa": "3.76",
        "applicant_name": "John Doe",
        "major": "Engineering",
        "grad_year": "2024",
        "college": "Engineering",
        "cycle": "Summer",
        "resume_link": "https://example.com/resume-john",
    },
    {
        "id": "#2010178",
        "job": "HR",
        "gpa": "3.91",
        "applicant_name": "Jane Smith",
        "major": "Business",
        "grad_year": "2023",
        "college": "Business",
        "cycle": "Fall",
        "resume_link": "https://example.com/resume-jane",
    },
    {
        "id": "#9238483",
        "job": "CEO",
        "gpa": "3.81",
        "applicant_name": "Robert Brown",
        "major": "Science",
        "grad_year": "2025",
        "college": "Science",
        "cycle": "Spring",
        "resume_link": "https://example.com/resume-robert",
    },
    {
        "id": "#7489234",
        "job": "CFO",
        "gpa": "4.0",
        "applicant_name": "Emily Davis",
        "major": "Engineering",
        "grad_year": "2024",
        "college": "Engineering",
        "cycle": "Summer",
        "resume_link": "https://example.com/resume-emily",
    },
]

# Header Section
st.markdown("## View Job Applications")
st.divider()

# Display the application list
st.markdown("### Applications")
for app in applications:
    app_col1, app_col2, app_col3, app_col4 = st.columns([1, 1, 1, 2])
    with app_col1:
        st.write(app["id"])
    with app_col2:
        st.write(app["gpa"])
    with app_col3:
        st.write(app["job"])
    with app_col4:
        # Create a button to navigate to the application details page
        if st.button(f"View {app['applicant_name']}'s Application →", key=f"view_{app['id']}"):
            # Store the selected application in session state
            st.session_state["selected_application"] = app
            # Navigate to the details page
            st.switch_page("pages/application_details.py")
