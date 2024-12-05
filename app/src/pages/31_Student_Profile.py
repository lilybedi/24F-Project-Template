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
gpa = 3.0
photo_link = "./assets/profile_photo.png"
status = 1
resumes = {"Teaching Resume": "google.com",
           "Lawyer Resume": "yahoo.com"}

advisor_name = "Jeremy"
advisor_contact = "gmail.com"

alumni = {"Mary": "gmail2.com",
          "Alice": "gmail3.com"}



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
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Content
st.divider()

# Profile Section (Left)
col1, col2 = st.columns([2, 3])

with col1:
    st.image(photo_link, width=150) 

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
    for compets in list(skills_experiences.keys()):
        skill_container = st.container()
        st.markdown("**" + compets + "**")
        st.write(skills_experiences.get(compets))

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
