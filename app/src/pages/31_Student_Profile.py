import logging
logger = logging.getLogger(__name__)

import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')
# Todo when routes are done- wherever there is something that say TODO: do it

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

STUDENT_ID = st.session_state.get("student_id", 1)
BASE_URL = "http://web-api:4000/st"

try:
    response = requests.get(f"{BASE_URL}/profile/{STUDENT_ID}")
    response.raise_for_status()
    profile = response.json()

    # Map profile fields to Streamlit inputs
    profile_data = {
        "First_Name": profile.get("First_Name", ""),
        "Last_Name": profile.get("Last_Name", ""),
        "Email": profile.get("Email", ""),
        "Graduated": profile.get("Grad_Year", ""),
        "Major": profile.get("Majors", ""),
        "Minor": profile.get("Minors", ""),
        "Description": profile.get("description", "")
    }

except requests.exceptions.RequestException as e:
    st.error(f"Failed to fetch profile: {e}")
    profile_data = {
        "First_Name": "",
        "Last_Name": "",
        "Email": "",
        "Graduated": "",
        "Major": "",
        "Minor": "",
    }


# Fetch data from the backend

# default values
student_name = "Unknown"
major = "Unknown"
grad_year = "N/A"
gpa = 0.0
photo_link = "./assets/profile_photo.png" 
status = 0
resumes = {}
advisor_name = "Unknown"
alumni = {}
description = "N/A"

if profile:
    student_name = f"{profile['First_Name']} {profile['Last_Name']}"
    major = (profile['Majors'])
    grad_year = profile.get('Grad_Year', "N/A")
    gpa = profile.get('GPA')
    description = profile.get('Description')

    resumes = {"Resume": profile.get('Resume_Link')}
    advisor_name = profile.get("Advisor_First_Name") + " " + profile.get("Advisor_Last_Name")
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

# Resumes
col3, col4 = st.columns([2, 3])
with col4:
    st.write("Links to Websites")
    for name, link in resumes.items():
        st.markdown(f"- [{name}]({link})")

st.divider()
team_col = st.container() 



st.markdown("#### Your Team")
st.markdown("##### Advisor")

st.write(advisor_name)

st.divider()


if edit_mode:
    # Editable fields for editing profile
    first_name = st.text_input("First Name", value=profile.get('First_Name', ''))
    last_name = st.text_input("Last Name", value=profile.get('Last_Name', ''))
    preferred_name = st.text_input("Preferred Name", value=profile.get('Preferred_Name', ''))
    email = st.text_input("Email", value=profile.get('Email', ''))
    phone_number = st.text_input("Phone Number", value=profile.get('Phone_Number', ''))
    gpa = st.text_input("GPA", value=profile.get('GPA', ''))
    grad_year = st.text_input("Graduation Year", value=profile.get('Grad_Year', ''))
    description = st.text_area("Description", value=profile.get('Description', ''))
    resume_link = st.text_input("Resume Link", value=profile.get('Resume_Link', ''))
    majors = st.text_input("Majors", value=profile.get('Majors', ''))
    minors = st.text_input("Minors", value=profile.get('Minors', ''))

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
            "Majors": majors,
            "Minors": minors,
        }

        # Send PUT request to update profile
        print("Updated Data:", updated_data)
        response = requests.put(f"{BASE_URL}/edit_profile/{STUDENT_ID}", json=updated_data)
        print(f"{BASE_URL}/edit_profile/{STUDENT_ID}")
        response.raise_for_status()

        if response.status_code == 200:
            st.success("Profile updated successfully!")
            # Ensure `updated_data` is defined in the correct scope