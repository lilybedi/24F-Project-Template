from modules.nav import SideBarLinks
import streamlit as st

st.set_page_config(layout="wide")

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

# Company details
company_logo = "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg"  #cat photo
company_name = "Company Name"
company_description = "Description"

# Job positions data - generated with ChatGPT
positions = [
    {
        "position_name": "Dev Intern",
        "active_applications": 47,
        "closed_applications": 103,
        "position_views": 2042,
        "filled": "NOT FILLED",
    },
    {
        "position_name": "Design Intern",
        "active_applications": 36,
        "closed_applications": 43,
        "position_views": 1037,
        "filled": "NOT FILLED",
    },
    {
        "position_name": "Business Intern",
        "active_applications": 23,
        "closed_applications": 121,
        "position_views": 4037,
        "filled": "NOT FILLED",
    },
    {
        "position_name": "Marketing Intern",
        "active_applications": 104,
        "closed_applications": 14,
        "position_views": 1832,
        "filled": "NOT FILLED",
    },
]

# Header Section
st.markdown("## Career Compass")
st.divider()

# Company Info
col1, col2 = st.columns([1, 3])

with col1:
    st.image(company_logo, width=100)
with col2:
    st.markdown(f"### {company_name}")
    st.write(company_description)

st.divider()

# Job Positions Table Header
st.markdown(
    """
    <style>
    .position-header {
        background-color: #f0f0f0;
        font-weight: bold;
        padding: 10px;
        margin-bottom: 0px;
        display: flex;
        justify-content: space-between;
    }
    .position-row {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    .position-row:hover {
        background-color: #f9f9f9;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Table Header
st.markdown(
    """
    <div class="position-header">
        <div style="flex: 2;">Position Name</div>
        <div style="flex: 2;"># Active Applications</div>
        <div style="flex: 2;"># Closed Applications</div>
        <div style="flex: 2;"># Position Views</div>
        <div style="flex: 1;">Filled?</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Job Positions Table Rows
for position in positions:
    st.markdown(
        f"""
        <div class="position-row">
            <div style="flex: 2;">{position['position_name']}</div>
            <div style="flex: 2;">{position['active_applications']} Active Applications</div>
            <div style="flex: 2;">{position['closed_applications']} Closed Applications</div>
            <div style="flex: 2;">{position['position_views']} Views</div>
            <div style="flex: 1;">{position['filled']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )