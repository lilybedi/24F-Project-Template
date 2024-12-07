import logging
import pandas as pd
from modules.nav import SideBarLinks
import streamlit as st

st.set_page_config(layout='wide')

# Retrieve the selected student's data from session_state
student = st.session_state.get("selected_student", None)

# If no student data exists, show a warning and exit
if not student:
    st.warning("No student data found. Please select a student from the main page.")
    st.stop()

# Display detailed student information
st.title(f"Detailed Information for {student['Name']}")

st.markdown("### Personal Details")
st.write(f"**Name:** {student['Name']}")
st.write(f"**Status:** {student['Status']}")
st.write(f"**Number of Applications:** {student['Applications']}")
st.write(f"**GPA:** {student['GPA']} / 4.0")
st.write(f"**Co-op Cycle:** {student['CoopCycle']}")
st.write(f"**Graduation Year:** {student['GradYear']}")
st.write(f"**Eligible for Co-op:** {'Yes' if student['EligibleForCoop'] else 'No'}")

# Display the resume link
if "ResumeURL" in student and student["ResumeURL"]:
    st.markdown(f"**[View Resume](<{student['ResumeURL']}>)**", unsafe_allow_html=True)

st.markdown("---")

# Additional details (you can expand this section as needed)
if st.button("Go to Company Application"):
    st.switch_page("pages/application_details.py")

# Button to go back to the main page
if st.button("Back to Main Page"):
    st.switch_page("pages/45_Advisor_View_Students.py")
