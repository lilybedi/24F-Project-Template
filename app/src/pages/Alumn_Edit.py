import streamlit as st

# Retrieve existing profile details
profile = {
    "Graduated": st.session_state.get("Graduated", "2022"),
    "Major": st.session_state.get("Major", "Computer Science"),
    "Minor": st.session_state.get("Minor", "Neuroscience"),
    "GPA": st.session_state.get("GPA", "3.8"),
    "Email": st.session_state.get("Email", "neel@gmail.com"),
}

st.title("Edit Profile")

# Create a form for editing the profile
with st.form(key="profile_form"):
    profile["Graduated"] = st.text_input("Graduated", profile["Graduated"])
    profile["Major"] = st.text_input("Major", profile["Major"])
    profile["Minor"] = st.text_input("Minor", profile["Minor"])
    profile["GPA"] = st.text_input("GPA", profile["GPA"])
    profile["Email"] = st.text_input("Email", profile["Email"])
    if st.form_submit_button("Save"):
        # Save changes to session state
        for key, value in profile.items():
            st.session_state[key] = value
        st.success("Profile updated successfully!")
        st.switch_page("pages/Alumn_Home.py")
