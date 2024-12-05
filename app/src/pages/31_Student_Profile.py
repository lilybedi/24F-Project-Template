import streamlit as st

#
# Information needed on load
#

import streamlit as st

student_name = "John Kennedy"
major = "English"
grad_year = 2027 # skill / description?
skills_experiences = {"Writing": "Advanced",
               "Mathematics": "Basic"}



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
        <div>Jobs</div>
        <div class="profile-pic">Edit Profile</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Content
st.divider()

# Profile Section (Left)
col1, col2 = st.columns([2, 3])

with col1:
    st.image("./assets/profile_photo.png", caption="Picture", width=150) 
    st.button("Edit Profile")  

with col2:
    st.write(student_name)
    st.write("Major / Graduation Year")
    st.write("GPA")
    st.selectbox("Status", ["Looking for co-op", "Accepted Offer"]) 

# Resumes
col3, col4 = st.columns([2, 3])

with col4:
    st.write("Links to Websites")
    st.selectbox("Resumes", ["Resume 1", "Resume 2", "Resume 3"])  # Dropdown for resumes

st.divider()
exp_col, team_col = st.columns([3, 2]) 

# Experiences and Skills
with exp_col:
    st.markdown("#### Experiences and Skills")
    for compets in list(skills_experiences.keys()):
        skill_container = st.container()
        st.markdown("**" + compets + "**")
        st.write(skills_experiences.get(compets))

# Your Team
with team_col:
    st.write("#### Your Team")
    st.button("Advisor Profile and Contact")
    st.button("Alumni Profile and Contact")