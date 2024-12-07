import streamlit as st
import requests
from modules.nav import SideBarLinks

# Base URL for your API
BASE_URL = "http://api:4000"

# Sidebar navigation
SideBarLinks()

# Retrieve Alumni ID from session or use a fallback for testing
ALUMNI_ID = st.session_state.get("alumni_id", 1)  # Replace 1 with dynamic ID retrieval in production

# Title
st.title("Edit Alumni Profile")

# Fetch the existing profile details
try:
    response = requests.get(f"{BASE_URL}/a/{ALUMNI_ID}")
    response.raise_for_status()
    profile = response.json()  # Parse the JSON response

    # Map profile fields to Streamlit inputs
    profile_data = {
        "First_Name": profile.get("First_Name", ""),
        "Last_Name": profile.get("Last_Name", ""),
        "Email": profile.get("Email", ""),
        "Graduated": profile.get("Grad_Year", ""),
        "Major": profile.get("Majors", "").split(",")[0] if profile.get("Majors") else "",
        "Minor": profile.get("Minors", "").split(",")[0] if profile.get("Minors") else "",
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

# Create a form for editing the profile
with st.form(key="profile_form"):
    profile_data["First_Name"] = st.text_input("First Name", profile_data["First_Name"])
    profile_data["Last_Name"] = st.text_input("Last Name", profile_data["Last_Name"])
    profile_data["Email"] = st.text_input("Email", profile_data["Email"])
    profile_data["Graduated"] = st.text_input("Graduation Year", profile_data["Graduated"])
    profile_data["Major"] = st.text_input("Major", profile_data["Major"])
    profile_data["Minor"] = st.text_input("Minor", profile_data["Minor"])

    # Submit button
    if st.form_submit_button("Save Changes"):
        # Prepare data for the PUT request
        updated_data = {
            "First_Name": profile_data["First_Name"],
            "Last_Name": profile_data["Last_Name"],
            "Email": profile_data["Email"],
            "Grad_Year": profile_data["Graduated"],
            "Majors": [profile_data["Major"]],
            "Minors": [profile_data["Minor"]],
        }

        try:
            # Make the PUT request to update the profile
            response = requests.put(f"{BASE_URL}/a/{ALUMNI_ID}", json=updated_data)
            if response.status_code == 200:
                st.success("Profile updated successfully!")
                # Update session state with the new data
                st.session_state.update(profile_data)
                st.switch_page("pages/Alumn_Home.py")

            else:
                st.error(f"Failed to update profile: {response.json().get('error', 'Unknown error')}")

        except requests.exceptions.RequestException as e:
            st.error(f"Error updating profile: {e}")
