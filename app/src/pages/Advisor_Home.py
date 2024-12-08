import streamlit as st
import pandas as pd
import requests
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the currently logged-in user
SideBarLinks()

# API Configuration
API_BASE_URL = "http://api:4000/ad"

# Helper function to fetch students data
def fetch_students(advisor_id):
    try:
        response = requests.get(f"{API_BASE_URL}/students/{advisor_id}")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.json()  # Returns a list of student dictionaries
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching students: {e}")
        return []

# Helper function to fetch advisor term summary
def fetch_term_summary(advisor_id):
    try:
        response = requests.get(f"{API_BASE_URL}/term-summary/{advisor_id}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching term summary: {e}")
        return {}

# Display Welcome Header
advisor_first_name = st.session_state.get("first_name", "Guest")
st.title(f"Welcome Advisor, {advisor_first_name}.")

# Fetch Advisor ID
advisor_id = st.session_state.get("advisor_id", 25)  # Default to 25 if not set

# Fetch students data
students_data = fetch_students(advisor_id)
df = pd.DataFrame(students_data)

# --- Filter and Search Functionality ---
st.markdown("### Manage Students")

# Search bar
search_query = st.text_input("Search by name", value="")

# Filter dropdown
filter_option = st.radio(
    "Filter by status",
    options=["All", "Received Offer", "Still Searching"],
    horizontal=True
)

# Sort dropdown
sort_by = st.selectbox("Sort By", ["None", "Applications Ascending", "Applications Descending"])

# Start filtering data
filtered_df = df.copy()

# Apply search filter
if search_query.strip():
    filtered_df = filtered_df[filtered_df["First_Name"].str.contains(search_query.strip(), case=False, na=False) |
                              filtered_df["Last_Name"].str.contains(search_query.strip(), case=False, na=False)]

# Apply status filter
if filter_option == "Received Offer":
    filtered_df = filtered_df[filtered_df["Hired"] == "TRUE"]
elif filter_option == "Still Searching":
    filtered_df = filtered_df[filtered_df["Hired"] == "FALSE"]

# Apply sorting
if sort_by == "Applications Ascending":
    filtered_df = filtered_df.sort_values(by="Total_Applications", ascending=True)
elif sort_by == "Applications Descending":
    filtered_df = filtered_df.sort_values(by="Total_Applications", ascending=False)

# --- Display the filtered data ---
if filtered_df.empty:
    st.warning("No data matches the current filters.")
else:
    # Add column headers
    st.markdown("#### Students Overview")
    st.write("Below is the list of students matching your filters:")

    # Format the DataFrame to include clean headers
    formatted_df = filtered_df[["First_Name", "Last_Name", "Hired", "Total_Applications", "GPA", "Latest_Application"]]
    formatted_df.rename(columns={
        "First_Name": "First Name",
        "Last_Name": "Last Name",
        "Hired": "Status",
        "Total_Applications": "Total Applications",
        "GPA": "GPA",
        "Latest_Application": "Latest Application"
    }, inplace=True)
    
    # Display the table
    st.dataframe(formatted_df, use_container_width=True)

# --- Display the Student Profile Panel ---
if "profile_open" in st.session_state and st.session_state["profile_open"]:
    student = st.session_state["selected_student"]
    st.sidebar.markdown(f"### Student Profile: {student['First_Name']} {student['Last_Name']}")
    st.sidebar.write(f"**GPA:** {student['GPA']}")
    st.sidebar.write(f"**Status:** {'Hired' if student['Hired'] == 'TRUE' else 'Searching'}")
    st.sidebar.write(f"**Total Applications:** {student['Total_Applications']}")
    st.sidebar.write(f"**Latest Application Date:** {student['Latest_Application']}")

    if st.sidebar.button("Close Profile"):
        st.session_state["profile_open"] = False
