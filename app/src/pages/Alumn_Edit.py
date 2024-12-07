# import streamlit as st
# import requests

# # Base URL for your API
# BASE_URL = "http://web-api:4000"

# # http://api:4000/s/get_all'

# # Retrieve existing profile details from session state or set default values
# profile = {
#     "Graduated": st.session_state.get("Graduated", "2022"),
#     "Major": st.session_state.get("Major", "Computer Science"),
#     "Minor": st.session_state.get("Minor", "Neuroscience"),
#     "GPA": st.session_state.get("GPA", "3.8"),
#     "Email": st.session_state.get("Email", "neel@gmail.com"),
# }

# # Simulate the alumni ID (replace this with dynamic ID retrieval if applicable)
# ALUMNI_ID = 1  # Replace with the actual alumni ID from session or user data

# st.title("Edit Profile")

# # Create a form for editing the profile
# with st.form(key="profile_form"):
#     # Input fields for editing
#     profile["Graduated"] = st.text_input("Graduated", profile["Graduated"])
#     profile["Major"] = st.text_input("Major", profile["Major"])
#     profile["Minor"] = st.text_input("Minor", profile["Minor"])
#     profile["GPA"] = st.text_input("GPA", profile["GPA"])
#     profile["Email"] = st.text_input("Email", profile["Email"])

#     # Submit button
#     if st.form_submit_button("Save"):
#         # Prepare data to send to backend
#         updated_data = {
#             "First_Name": st.session_state.get("First_Name", "Neel"),
#             "Last_Name": st.session_state.get("Last_Name", "Doe"),
#             "Email": profile["Email"],
#             "Grad_Year": profile["Graduated"],
#             "Majors": [profile["Major"]],
#             "Minors": [profile["Minor"]],
#         }

#         # Make a PUT request to the backend
#         try:
#             response = requests.put(f"{BASE_URL}/alumni/{ALUMNI_ID}", json=updated_data)
#             if response.status_code == 200:
#                 # Save changes to session state
#                 for key, value in profile.items():
#                     st.session_state[key] = value
#                 st.success("Profile updated successfully!")
#                 st.experimental_rerun()  # Reload the page or redirect
#             else:
#                 st.error(f"Failed to update profile: {response.json().get('error', 'Unknown error')}")
#         except Exception as e:
#             st.error(f"An error occurred: {e}")


import logging
import requests
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Sidebar navigation (if you have this)
SideBarLinks()

# Initialize logger
logger = logging.getLogger(__name__)

# Set the page title
st.title("Edit Alumni Profile")

# Existing profile details (these can come from your session state or pre-populated from the database)
profile = {
    "First_Name": st.session_state.get("First_Name", "Neel"),
    "Last_Name": st.session_state.get("Last_Name", "Alumn"),
    "Email": st.session_state.get("Email", "neel@gmail.com"),
    "Grad_Year": st.session_state.get("Grad_Year", "2022"),
    "College": st.session_state.get("College", "Khoury"),
    "Majors": st.session_state.get("Majors", ["Computer Science"]),
    "Minors": st.session_state.get("Minors", ["Mathematics"]),
}

st.write("\n\n")

# Create a Streamlit form widget to edit the profile
with st.form("edit_profile_form"):
    profile["First_Name"] = st.text_input("First Name", profile["First_Name"])
    profile["Last_Name"] = st.text_input("Last Name", profile["Last_Name"])
    profile["Email"] = st.text_input("Email", profile["Email"])
    profile["Grad_Year"] = st.text_input("Graduation Year", profile["Grad_Year"])
    profile["College"] = st.text_input("College", profile["College"])
    profile["Majors"] = st.text_input("Majors", ", ".join(profile["Majors"]))  # Allow comma separated majors input
    profile["Minors"] = st.text_input("Minors", ", ".join(profile["Minors"]))  # Allow comma separated minors input

    # Add the submit button (which every form needs)
    submit_button = st.form_submit_button("Save Changes")

    # Validate form submission and update profile
    if submit_button:
        # Validate the fields before sending the data
        if not profile["First_Name"]:
            st.error("Please enter a first name")
        elif not profile["Last_Name"]:
            st.error("Please enter a last name")
        elif not profile["Email"]:
            st.error("Please enter a valid email")
        elif not profile["Grad_Year"]:
            st.error("Please enter a graduation year")
        elif not profile["College"]:
            st.error("Please enter your college")
        elif not profile["Majors"]:
            st.error("Please enter at least one major")
        elif not profile["Minors"]:
            st.error("Please enter at least one minor")
        else:
            # If validation passes, prepare the data to be sent in the PUT request
            alumni_data = {
                "First_Name": profile["First_Name"],
                "Last_Name": profile["Last_Name"],
                "Email": profile["Email"],
                "Grad_Year": profile["Grad_Year"],
                "College": profile["College"],
                "Majors": [major.strip() for major in profile["Majors"].split(",")],
                "Minors": [minor.strip() for minor in profile["Minors"].split(",")]
            }

            # Printing out the data for debugging/logging
            logger.info(f"Profile update form submitted with data: {alumni_data}")

            # Make a PUT request to the backend to update the profile
            try:
                # Replace <alumni_id> with the actual alumni ID
                alumni_id = 1  # For example, assume this is the alumni ID
                response = requests.put(f'http://api:4000/alumni/{alumni_id}', json=alumni_data)

                if response.status_code == 200:
                    st.success("Profile updated successfully!")
                else:
                    st.error(f"Error updating profile: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error connecting to the server: {str(e)}")
