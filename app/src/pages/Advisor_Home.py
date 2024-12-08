import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(layout='wide')

# Show appropriate sidebar links for the currently logged-in user
SideBarLinks()

# Main Streamlit app
st.title(f"Welcome Advisor, {st.session_state.get('first_name', 'Guest')}.")

# --- Temporarily Replace API Call with Sample Data ---

# Sample student data (replace this with your real API response later)
sample_data = [
    {"Name": "John Doe", "Status": "Received offer", "Applications": 5, "GPA": 3.8, "CoopCycle": "Spring", "GradYear": 2024, "EligibleForCoop": True},
    {"Name": "Jane Smith", "Status": "Still Searching", "Applications": 3, "GPA": 3.5, "CoopCycle": "Fall", "GradYear": 2025, "EligibleForCoop": True},
    {"Name": "Michael Johnson", "Status": "Received offer", "Applications": 7, "GPA": 3.9, "CoopCycle": "Spring", "GradYear": 2023, "EligibleForCoop": False},
    {"Name": "Emily Davis", "Status": "Still Searching", "Applications": 2, "GPA": 3.2, "CoopCycle": "Fall", "GradYear": 2026, "EligibleForCoop": True},
    {"Name": "James Brown", "Status": "Received offer", "Applications": 6, "GPA": 3.7, "CoopCycle": "Spring", "GradYear": 2024, "EligibleForCoop": True},
]

# Create a DataFrame from the sample data
df = pd.DataFrame(sample_data)

# --- Add Filters and Search Functionality ---

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
    filtered_df = filtered_df[filtered_df["Name"].str.contains(search_query.strip(), case=False, na=False)]

# Apply status filter
if filter_option == "Received Offer":
    filtered_df = filtered_df[filtered_df["Status"] == "Received offer"]
elif filter_option == "Still Searching":
    filtered_df = filtered_df[filtered_df["Status"] == "Still Searching"]

# Apply sorting
if sort_by == "Applications Ascending":
    filtered_df = filtered_df.sort_values(by="Applications", ascending=True)
elif sort_by == "Applications Descending":
    filtered_df = filtered_df.sort_values(by="Applications", ascending=False)

# --- Display the filtered data with clickable names ---
if filtered_df.empty:
    st.warning("No data matches the current filters.")
else:
    # Add a header row for the table
    col1, col2, col3 = st.columns([3, 2, 1])
    with col1:
        st.markdown("### Name")
    with col2:
        st.markdown("### Status")
    with col3:
        st.markdown("### Applications")

    # Display a table with clickable student names
    for index, row in filtered_df.iterrows():
        col1, col2, col3 = st.columns([3, 2, 1])

        with col1:
            # Create a button for each student's name
            if st.button(row["Name"], key=row["Name"]):
                # Store the clicked student's data in session_state
                st.session_state["selected_student"] = row.to_dict()
                st.session_state["profile_open"] = True  # Set profile panel to be open

        with col2:
            st.write(row["Status"])

        with col3:
            st.write(row["Applications"])

# --- Display the Student Profile Panel on the Right ---
if "profile_open" in st.session_state and st.session_state["profile_open"]:
    student = st.session_state["selected_student"]

    # Custom CSS to position the profile panel on the right side
    st.markdown(
        """
        <style>
            .profile-container {
                position: fixed;
                top: 10%;
                right: 0;
                width: 350px;
                height: 90%;
                background-color: #f1f1f1;
                border-left: 2px solid #ccc;
                padding: 20px;
                overflow-y: auto;
                z-index: 9999;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .profile-container h3 {
                color: #333;
            }
            .profile-container p {
                font-size: 14px;
            }
        </style>
        """, unsafe_allow_html=True
    )

    # Display profile data inside the slide-over panel
    st.markdown(f"""
    <div class="profile-container">
        <h3>Student Profile: {student['Name']}</h3>
        <p><strong>Name:</strong> {student['Name']}</p>
        <p><strong>Status:</strong> {student['Status']}</p>
        <p><strong>Applications:</strong> {student['Applications']}</p>
        <p><strong>GPA:</strong> {student['GPA']} / 4.0</p>
        <p><strong>Co-op Cycle:</strong> {student['CoopCycle']}</p>
        <p><strong>Graduation Year:</strong> {student['GradYear']}</p>
        <p><strong>Eligible for Co-op:</strong> {'Yes' if student['EligibleForCoop'] else 'No'}</p>
    </div>
    """, unsafe_allow_html=True)

    # Single button to close the profile panel
    if st.button("Close Profile"):
        st.session_state["profile_open"] = False  # Close the profile panel
        del st.session_state["selected_student"]  # Remove selected student data
