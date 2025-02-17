import streamlit as st
# Sample Data - connect to backend
cat_photo = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat03.jpg/640px-Cat03.jpg"

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
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class="navbar">
        <div>Career Compass</div>
        <div class="search-bar"><input type="text" placeholder="Search..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.divider()
# Tab Navigation
tabs = st.tabs(["Job Search", "Job Applications", "Alumni Network"])
with tabs[0]:
    # Get first job
    if "selected_job" not in st.session_state:
        st.session_state["selected_job"] = job_postings[0] 
    job_col, details_col = st.columns([2, 3])
    # Job Postings
    with job_col:
        st.markdown("### Job Applications")
        for job in job_postings:
            if st.button(job["title"], key=job["id"]):  # Each job title is a button
                st.session_state["selected_job"] = job  # Update session state with the selected job
    # Right Column: Job Details
    with details_col:
        selected_job = st.session_state["selected_job"]  # Get the selected job from session state
        st.markdown("### Job Details")
        st.image(selected_job["image"], use_container_width=True)
        st.markdown(f"**Job Title:** {selected_job['title']}")
        st.write(f"**Company Name:** {selected_job['company']}")
        st.write(f"**Percentage Match:** {selected_job['match']}")
        st.button("Click to see full breakdown")  # Static button for additional breakdown functionality
        st.write(f"**Job Description:** {selected_job['description']}")