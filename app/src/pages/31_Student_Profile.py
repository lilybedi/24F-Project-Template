import streamlit as st

#
# Information needed on load
#

import streamlit as st

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
    .profile-pic {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: white; /* Placeholder for profile picture */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="navbar">
        <div>Career Compass</div>
        <div>Profile</div>
        <div class="profile-pic"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Content
st.divider()

# Profile Section (Left)
col1, col2 = st.columns([2, 3])

with col1:
    st.image("./assets/profile_photo.png", caption="Picture", width=150)  # Placeholder for profile image
    st.button("Edit Profile")  # Edit Profile Button

with col2:
    st.write("Student Name")
    st.write("Major / Graduation Year")
    st.write("GPA")
    st.selectbox("Status", ["Looking for co-op", "Accepted Offer"])  # Dropdown for status

# Links to Websites Section (Top-Right)
col3, col4 = st.columns([2, 3])

with col4:
    st.markdown("**Links to Websites**")
    st.selectbox("Resumes", ["Resume 1", "Resume 2", "Resume 3"])  # Dropdown for resumes

# Experiences and Skills Section (Bottom-Left)
st.markdown("### Experiences and Skills")
exp_col1, exp_col2, exp_col3 = st.columns([1, 1, 1])

with exp_col1:
    st.empty()  # Placeholder for first experience block

with exp_col2:
    st.empty()  # Placeholder for second experience block

with exp_col3:
    st.empty()  # Placeholder for third experience block

# Your Team Section (Bottom-Right)
st.markdown("### Your Team")
team_col1, team_col2 = st.columns([1, 1])

with team_col1:
    st.button("Advisor Profile and Contact")  # Advisor profile block

with team_col2:
    st.button("Alumni Profile and Contact")  # Alumni profile block