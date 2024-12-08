import streamlit as st
import requests

from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Sidebar navigation
SideBarLinks()
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

# # Show appropriate sidebar links for the role of the currently logged in user
# SideBarLinks()
# # Sample Data - connect to backend - generated with ChatGPT

# cat_photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"

# #TODO: FIX ERROR 404 ON FETCHING JOBS
# BASE_URL = "http://web-api:4000"

# # Function to fetch job postings from the backend
# # def fetch_jobs(min_pay=None):
# #     params = {}
# #     if min_pay is not None:
# #         params["min_pay"] = min_pay
# #     response = requests.get(f"{BASE_URL}/postings/by_pay", params=params)
# #     if response.status_code == 200:
# #         return response.json()
# #     else:
# #         st.error(f"Error fetching jobs: {response.status_code}")
# #         return []

# # # Fetch initial job postings (default)
# # job_postings = fetch_jobs()

# job_postings = [
#     {
#         "id": 1,
#         "title": "Software Engineer",
#         "company": "domp",
#         "description": "Develop and maintain software applications.",
#     },
#     {
#         "id": 2,
#         "title": "Software Engineer",
#         "company": "blep",
#         "description": "glorp",
#     },
#         {
#         "id": 3,
#         "title": "Software Engineer",
#         "company": "domp",
#         "description": "glep"
#     }
# ]



# # Header Section: Navbar
# st.markdown(
#     """
#     <style>
#     .navbar {
#         background-color: #d3d3d3; /* Light gray background for the navbar */
#         padding: 15px;
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         font-size: 18px;
#         font-weight: bold;
#     }
#     .navbar div {
#         display: inline-block;
#     }

#     .search-bar {
#         flex-grow: 1;
#         margin: 0 20px;
#         display: flex;
#         align-items: center;
#     }

#     .button-row {
#         display: flex;
#         justify-content: center;
#         gap: 10px;
#     }
#     .button-row button {
#         border: none;
#         margin: 10px 20px;
#         font-size: 16px;
#         border-radius: 5px;
#     }
#     </style>

#     <div class="navbar">
#         <div>Career Compass</div>
#         <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
#     </div>
    

#     """,
#     unsafe_allow_html=True,
# )

# filter_col, sort_col = st.columns([2, 1])

# # "Filter By"
# with filter_col:
#     st.markdown("**Filter**")
#     with st.expander("Filter by"):
#         selected_filter = st.selectbox("Choose a filter", ["Status", "Location"], key="filter_select")
        
#         if selected_filter == "Status":
#             st.selectbox("Select Status", ["Pending", "Accepted", "Rejected"], key="status_filter")
        
#         elif selected_filter == "Location":
#             st.selectbox("Select Location", ["City, State 1", "City, State 2"], key="location_filter")


# st.divider()

# # Get first job
# if "selected_job" not in st.session_state:
#     st.session_state["selected_job"] = job_postings[0] 

# job_col, details_col = st.columns([2, 3])

# # Job Postings
# with job_col:
#     st.markdown("### Job Postings")
#     for job in job_postings:
#         if st.button(job["title"], key=job["id"]):  # Each job title is a button
#             st.session_state["selected_job"] = job  # Update session state with the selected job

# # Job Details
# with details_col:
#     selected_job = st.session_state["selected_job"]  # Get the selected job from session state
#     st.markdown("### Job Details")
#     st.markdown(f"**Job Title:** {selected_job['title']}")
#     st.write(f"**Company Name:** {selected_job['company']}")
#     st.write(f"**Job Description:** {selected_job['description']}")

