import streamlit as st

# Set up initial profile data (or load from session state if already set)
if 'student_name' not in st.session_state:
    st.session_state.student_name = "John Kennedy"
    st.session_state.major = "English"
    st.session_state.grad_year = 2027
    st.session_state.gpa = 3.0
    st.session_state.skills_experiences = {"Writing": "Advanced", "Mathematics": "Basic"}
    st.session_state.resumes = {"Teaching Resume": "google.com", "Lawyer Resume": "yahoo.com"}

# Edit Profile Form
st.title("Edit Profile")

# Student Name
st.session_state.student_name = st.text_input("Student Name", value=st.session_state.student_name)

# Major
st.session_state.major = st.text_input("Major", value=st.session_state.major)

# Graduation Year
st.session_state.grad_year = st.number_input("Graduation Year", value=st.session_state.grad_year, min_value=2020, max_value=2100)

# GPA
st.session_state.gpa = st.number_input("GPA", value=st.session_state.gpa, min_value=0.0, max_value=4.0, step=0.1)

# Update Skills Section
st.markdown("#### Update Skills")

# Display current skills
for skill, proficiency in st.session_state.skills_experiences.items():
    new_proficiency = st.selectbox(f"Proficiency Level for {skill}", ["Basic", "Intermediate", "Advanced"], index=["Basic", "Intermediate", "Advanced"].index(proficiency))
    st.session_state.skills_experiences[skill] = new_proficiency

# Add New Skill
new_skill = st.text_input("New Skill", placeholder="Enter a new skill")
if st.button("Add Skill") and new_skill:
    proficiency = st.selectbox("Proficiency Level", ["Basic", "Intermediate", "Advanced"])
    st.session_state.skills_experiences[new_skill] = proficiency
    st.success(f"Added skill: {new_skill} ({proficiency})")

# Update Resumes Section
st.markdown("#### Update Resumes")
for resume_name, link in st.session_state.resumes.items():
    new_link = st.text_input(f"Update {resume_name} Link", value=link)
    st.session_state.resumes[resume_name] = new_link

# Button to Save Changes
if st.button("Save Changes"):
    st.success("Profile updated successfully!")
    st.write(f"Updated Name: {st.session_state.student_name}")
    st.write(f"Updated Major: {st.session_state.major}")
    st.write(f"Updated Graduation Year: {st.session_state.grad_year}")
    st.write(f"Updated GPA: {st.session_state.gpa}")
    st.write(f"Updated Skills: {st.session_state.skills_experiences}")
    st.write(f"Updated Resumes: {st.session_state.resumes}")
