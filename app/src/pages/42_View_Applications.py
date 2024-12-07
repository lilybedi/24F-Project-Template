import streamlit as st
from modules.nav import SideBarLinks

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

# Initialize session state to track currently opened application
if "view_app_id" not in st.session_state:
    st.session_state.view_app_id = None  # No application view by default

# Always render the application list above everything
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
        # When a user clicks a button, set the state to show the application details
        if st.button(
            f"View {app['applicant_name']}'s Application →",
            key=f"view_{app['id']}"
        ):
            st.session_state.view_app_id = app["id"]

# Render application details only below the application list if a specific application is clicked
if st.session_state.view_app_id:
    selected_app = next(
        (app for app in applications if app["id"] == st.session_state.view_app_id), None
    )
    if selected_app:
        st.markdown("---")
        st.markdown(f"### {selected_app['applicant_name']}'s Application")
        st.write(f"**Major/College:** {selected_app['college']} / {selected_app['major']}")
        st.write(f"**Graduation Year:** {selected_app['grad_year']}")
        st.write(f"**GPA:** {selected_app['gpa']}")
        st.write(f"**Cycle:** {selected_app['cycle']}")
        st.write(f"[View Resume]({selected_app['resume_link']})")
        
        # Button to close detailed view
        if st.button("Close Application View"):
            st.session_state.view_app_id = None
