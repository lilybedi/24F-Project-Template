import logging
logger = logging.getLogger(__name__)

import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

#
# Todo when routes are done- wherever there is something that say TODO: do it
#

BASE_URL = "http://web-api:4000"

# Fetch a specific student's profile by ID
def fetch_student_by_id(student_id):
    response = requests.get(f"{BASE_URL}/s/{student_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching student: {response.status_code}")
        return None

student_id = st.session_state.get('student_id', 1)  # Default to ID 1 for testing

# Fetch data from the backend
student = fetch_student_by_id(student_id)

# Initialize variables to default values
student_name = "Unknown"
major = "Unknown"
grad_year = "N/A"
gpa = 0.0
photo_link = "./assets/profile_photo.png"  # Add a default photo
status = 0
resumes = {}
advisor_name = "Unknown"
advisor_contact = "Unknown"
alumni = {}

# Fetch data from the backend
student = fetch_student_by_id(student_id)

if student:
    student_name = f"{student['First_Name']} {student['Last_Name']}"
    major = (student['Majors'])
    grad_year = student.get('Grad_Year', "N/A")
    gpa = student.get('GPA')

    if (student.get('Cycle' == 'active')):
        status = 1
    else:
        status = 0

    resumes = {"Resume": student.get('Resume_Link')}
    advisor_name = student.get("Advisor Name") # TODO: Replace with actual advisor logic / access
    advisor_contact = student.get("Advisor Contact")
    alumni = {"Alumnus Name": "alumnus@example.com"}  # TODO: Replace with alumni logic if available
else:
    st.error("Failed to load student profile.")

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
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown( 
    """
    <div class="navbar">
        <div>Career Compass</div>
    </div>
    """,
    unsafe_allow_html=True,
)
#
# Main Content
#

st.divider()

# Profile Section (Left)
col1, col2 = st.columns([2, 3])

with col1:
    st.image(photo_link, width=150) 
    edit_mode = st.button("Edit Profile")

with col2:
    st.write(student_name)
    st.write(major + " / " + str(grad_year))
    st.write("GPA: " + str(gpa))

    # Default shows up first
    if (status == 0):
        st.selectbox("Status", ["Looking for co-op", "Not looking for co-op"]) 
    else:
        st.selectbox("Status", ["Not looking for co-op", "Looking for co-op"]) 

# Resumes
col3, col4 = st.columns([2, 3])
with col4:
    st.write("Links to Websites")
    for name, link in resumes.items():
        st.markdown(f"- [{name}]({link})")

st.divider()
exp_col, team_col = st.columns([3, 2]) 

# Experiences and Skills
with exp_col:
    st.markdown("#### Experiences and Skills")

    # Uncomment this section
    # for compets in list(skills_experiences.keys()):
    #    skill_container = st.container()
    #    st.markdown("**" + compets + "**")
    #    st.write(skills_experiences.get(compets))

# Your Team
with team_col:

    st.markdown("#### Your Team")
    st.markdown("##### Advisor")

    st.write(advisor_name)
    st.write(advisor_contact)

    st.divider()

    st.markdown("#### Alumni")

    for alumnus in list(alumni.keys()):
        st.markdown("#### " + alumnus)
        st.write(alumni.get(alumnus))


if edit_mode:
    # Editable fields for editing profile
    first_name = st.text_input("First Name", value=student.get('First_Name', ''))
    last_name = st.text_input("Last Name", value=student.get('Last_Name', ''))
    preferred_name = st.text_input("Preferred Name", value=student.get('Preferred_Name', ''))
    email = st.text_input("Email", value=student.get('Email', ''))
    phone_number = st.text_input("Phone Number", value=student.get('Phone_Number', ''))
    gpa_value = student.get('GPA', "3.0") if student.get('GPA') else "3.0"
    gpa = st.text_input("GPA", value=student.get('GPA', ''))
    grad_year = st.text_input("Graduation Year", value=student.get('Grad_Year', 2024))
    description = st.text_area("Description", value=student.get('Description', ''))
    resume_link = st.text_input("Resume Link", value=student.get('Resume_Link', ''))
    majors = st.text_input("Majors (comma-separated)", value=", ".join(student.get('Majors', [])))
    minors = st.text_input("Minors (comma-separated)", value=", ".join(student.get('Minors', [])))

    # Save changes button
    if st.button("Save Changes"):
        updated_data = {
            "First_Name": first_name,
            "Last_Name": last_name,
            "Preferred_Name": preferred_name,
            "Email": email,
            "Phone_Number": phone_number,
            "GPA": gpa,
            "Grad_Year": grad_year,
            "Description": description,
            "Resume_Link": resume_link,
            "Majors": [major.strip() for major in majors.split(",") if major.strip()],
            "Minors": [minor.strip() for minor in minors.split(",") if minor.strip()],
        }

        response = requests.put(f"{BASE_URL}/s/edit_profile/{student_id}", json=updated_data)
        if response.status_code == 200:
            st.success("Profile updated successfully!")
        else:
            st.error(f"Failed to update profile: {response.status_code}")






