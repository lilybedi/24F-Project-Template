import streamlit as st

# Sample data for applications - generated with ChatGPT
applications = [
    {
        "job_title": "Software Engineer",
        "company": "TechCorp",
        "resume": "Resume 1",
        "date_applied": "2023-11-15",
        "status": "Pending",
    },
    {
        "job_title": "Data Scientist",
        "company": "DataCorp",
        "resume": "Resume 2",
        "date_applied": "2023-11-20",
        "status": "Accepted",
    },
    {
        "job_title": "Product Manager",
        "company": "BizCorp",
        "resume": "Resume 1",
        "date_applied": "2023-11-25",
        "status": "Rejected",
    },
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
    .profile-pic {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: white; /* Placeholder for profile picture */
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
        <div class="search-bar"><input type="text" placeholder="Search Applications..." style="width: 100%; padding: 8px; border-radius: 5px; border: 1px solid #ccc;"></div>
        <div class="profile-pic"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# Filters Section
filter_col, sort_col = st.columns([2, 1])

with filter_col:
    st.markdown("**Filter**")
    with st.expander("Filter by"):
        selected_filter = st.selectbox("Choose a filter", ["Status", "Date"], key="filter_select")
        
        if selected_filter == "Status":
            selected_status = st.selectbox("Select Status", ["All", "Pending", "Accepted", "Rejected"], key="status_filter")
        elif selected_filter == "Date":
            st.date_input("Select Date Range", key="date_filter")

# Sort by section
with sort_col:
    st.markdown("**Sort By**")
    st.selectbox("Sort By", ["Relevance", "Date Applied", "Company"], key="sort_by")

st.divider()

# Applications Section
st.markdown("### Your Applications")

# Loop through the applications and display them as buttons with details
for application in applications:

    with st.container():
        col1, col2, col3, col4 = st.columns([2, 3, 2, 2])

        with col1:
            st.markdown(f"**{application['job_title']}**")
            st.write(application["company"])

        with col2:
            st.markdown(f"**Resume:** {application['resume']}")
            st.write(f"**Date Applied:** {application['date_applied']}")

        with col3:
            st.markdown(f"**Status:** {application['status']}")

        with col4:
            st.button("View Details", key=f"view_{application['job_title']}")
        
        st.divider()