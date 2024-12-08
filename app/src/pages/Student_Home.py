import streamlit as st
st.set_page_config(layout="wide")

from modules.nav import SideBarLinks

SideBarLinks()

#TODO: FIX ERROR 404 ON FETCHING JOBS
BASE_URL = "http://api:4000"

#
# Information needed on load -- FIX
#
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

# Main Content
st.divider()
# Profile Section (Left)
col1, col2 = st.columns([2, 3])
with col1:
    st.image(photo_link, width=150) 
    if st.button("Edit Profile Details"):
        st.switch_page("pages/Student_Edit.py")
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
    # st.markdown("### Add a Skill")
    # new_skill = st.text_input("Skill Name", placeholder="Enter skill name")
    # proficiency = st.selectbox("Proficiency Level", ["Basic", "Intermediate", "Advanced"])
    # if st.button("Add Skill"):
    #     if new_skill and proficiency:
    #         skills_experiences[new_skill] = proficiency
    #         st.success(f"Added skill: {new_skill} ({proficiency})")
    #     else:
    #         st.error("Please provide both a skill name and proficiency level.")
    
    # st.markdown("#### Experiences and Skills")
    # for compets in list(skills_experiences.keys()):
    #     skill_container = st.container()
    #     st.markdown("**" + compets + "**")
    #     st.write("• Level: " + skills_experiences.get(compets))
    with exp_col:
        st.markdown("#### Experiences and Skills")
    
    # Initialize session state for skills_experiences if it doesn't exist
    if 'skills_experiences' not in st.session_state:
        st.session_state.skills_experiences = skills_experiences
    
    # Display current skills
    for skill, proficiency in st.session_state.skills_experiences.items():
        st.markdown(f"**{skill}** - {proficiency}")
    
    # Add skill functionality
    st.markdown("### Add a Skill")
    new_skill = st.text_input("Skill Name", placeholder="Enter skill name")
    proficiency = st.selectbox("Proficiency Level", ["Basic", "Intermediate", "Advanced"])
    
    if st.button("Add Skill"):
        if new_skill:
            # Add the new skill with proficiency to session state
            st.session_state.skills_experiences[new_skill] = proficiency
            st.success(f"Added skill: {new_skill} ({proficiency})")
        else:
            st.error("Please provide a skill name.")
# Your Team
with team_col:
    st.markdown("#### Your Team")
    st.markdown("##### Advisor")
    st.write(advisor_name)
    st.write(advisor_contact)
    if st.button("Message " + advisor_name):
        st.switch_page("pages/Student_Advisor_Message.py")
    st.divider()
    st.markdown("#### Alumni")
    for alumnus in list(alumni.keys()):
        st.markdown("#### " + alumnus)
        st.write(alumni.get(alumnus))
        if st.button("Message " + alumnus):
            st.switch_page("pages/Student_Alumn_Message.py")