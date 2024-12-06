import streamlit as st
import requests


# Sample Data - connect to backend - generated with ChatGPT

cat_photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"

BASE_URL = "http://web-api:4000"

def fetch_all_jobs():
    response = requests.get(f"{BASE_URL}/s/postings/by_pay")
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error fetching student: {response.status_code}")
        return None
    
job_postings = [
    {
        "id": 1,
        "title": "Software Engineer",
        "company": "domp",
        "description": "Develop and maintain software applications.",
        "match": "85%", # Idk how to implement match
        "image": cat_photo
    },
    {
        "id": 2,
        "title": "Software Engineer",
        "company": "blep",
        "description": "glorp",
        "match": "44%",
        "image": cat_photo
    },
        {
        "id": 3,
        "title": "Software Engineer",
        "company": "domp",
        "description": "Develop and maintain software applications.",
        "match": "85%",
        "image": cat_photo
    }
]



# Header Section: Navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #d3d3d3; /* Light gray background for the navbar */
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

    .search-bar {
        flex-grow: 1;
        margin: 0 20px;
        display: flex;
        align-items: center;
    }

    .button-row {
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    .button-row button {
        border: none;
        margin: 10px 20px;
        font-size: 16px;
        border-radius: 5px;
    }
    </style>

    <div class="navbar">
        <div>Career Compass</div>
        <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
    </div>
    

    """,
    unsafe_allow_html=True,
)

filter_col, sort_col = st.columns([2, 1])

# "Filter By"
with filter_col:
    st.markdown("**Filter**")
    with st.expander("Filter by"):
        selected_filter = st.selectbox("Choose a filter", ["Status", "Location"], key="filter_select")
        
        if selected_filter == "Status":
            st.selectbox("Select Status", ["Pending", "Accepted", "Rejected"], key="status_filter")
        
        elif selected_filter == "Location":
            st.selectbox("Select Location", ["City, State 1", "City, State 2"], key="location_filter")

# "Sort By"
with sort_col:
    st.markdown("**Sort By**")
    st.selectbox("Sort By", ["Relevance", "Date Applied", "Company"], key="sort_by")

st.divider()

# Get first job
if "selected_job" not in st.session_state:
    st.session_state["selected_job"] = job_postings[0] 

job_col, details_col = st.columns([2, 3])

# Job Postings
with job_col:
    st.markdown("### Job Postings")
    for job in job_postings:
        if st.button(job["title"], key=job["id"]):  # Each job title is a button
            st.session_state["selected_job"] = job  # Update session state with the selected job

# Job Details
with details_col:
    selected_job = st.session_state["selected_job"]  # Get the selected job from session state
    st.markdown("### Job Details")
    st.image(selected_job["image"], use_container_width=True)
    st.markdown(f"**Job Title:** {selected_job['title']}")
    st.write(f"**Company Name:** {selected_job['company']}")
    st.write(f"**Percentage Match:** {selected_job['match']}")
    st.button("Click to see full breakdown")  # Static button for additional breakdown functionality
    st.write(f"**Job Description:** {selected_job['description']}")

