import streamlit as st
from modules.nav import SideBarLinks


st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Initialize w/ position
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Position Name"

# Defaults
if "required_skills" not in st.session_state:
    st.session_state["required_skills"] = ["Skill 1", "Skill 2", "Skill 3", "Skill 4", "Skill 5"]

if "description" not in st.session_state:
    st.session_state["description"] = "Editable description of position here..."

# Sample data for applicants - generated with ChatGPT
applicants = [
    {"id": "#8675309", "skills_match": "95%", "gpa": "3.76"},
    {"id": "#2010178", "skills_match": "91%", "gpa": "3.91"},
    {"id": "#9238483", "skills_match": "86%", "gpa": "3.81"},
    {"id": "#7489234", "skills_match": "82%", "gpa": "4.0"},
]

# Header Section
st.markdown("## Career Compass")
st.divider()

# Title and Action Buttons
if "position_title" not in st.session_state:
    st.session_state["position_title"] = "Default Title"

# Ensure value is managed consistently through session state
position_title = st.text_input("Position Title", key="position_title")

col1, col2 = st.columns([1, 1])

with col1:
    st.button("Browse Active Applications")
with col2:
    st.button("Browse Closed Applications")

st.divider()

# Title and Skills
left_col, right_col = st.columns([1.5, 3.5])

with left_col:

    # Required skills
    st.markdown("**Required Skills:**")
    for skill in st.session_state["required_skills"]:
        st.write(f"- {skill}")
    
    # Add new skill
    new_skill = st.text_input("Add Required Skill +", key="new_skill_input")
    if st.button("Add Skill"):
        if new_skill:
            st.session_state["required_skills"].append(new_skill)
            st.experimental_rerun()

    # Description
    st.text_area("Editable description:", value=st.session_state["description"], key="description")

with right_col:
    st.markdown("**Applicants:**")     # Applicants Table
    sort_option = st.selectbox("Sort By:", ["Skills Match Percentage", "GPA"])     # Sort by dropdown

    for applicant in applicants:     # Display aplicants as rows
        row_col1, row_col2, row_col3, row_col4 = st.columns([1, 1, 1, 2])
        with row_col1:
            st.write(applicant["id"])
        with row_col2:
            st.write(applicant["skills_match"])
        with row_col3:
            st.write(applicant["gpa"])
        with row_col4:
            st.button("See full application →", key=f"view_{applicant['id']}")