import streamlit as st
from modules.nav import SideBarLinks

# Set the page layout
st.set_page_config(layout="wide", page_title="Admin View", page_icon="📊")

# Initialize the navigation sidebar
SideBarLinks()

st.markdown("# Manage Users")

# USER DATA NEEDS TO BE CONNECTED TO BACKEND
if "data" not in st.session_state:
    st.session_state.data = [
        {"Name": "Douglass McStudent", "Role": "Co-Op Advisor"},
        {"Name": "Susan Rodriguez", "Role": "Alumni"},
        {"Name": "Jarred Wong", "Role": "Alumni"},
        {"Name": "John Doe", "Role": "Student"},
        {"Name": "Jane Smith", "Role": "Faculty"},
    ]

# --- User Management Section ---
st.markdown("### Add New User")

# Create a form to add a new user
with st.form(key='add_user_form'):
    new_name = st.text_input("Name", placeholder="Enter the new user's name")
    new_role = st.selectbox("Role", options=["Faculty", "Student", "Company", "Alumni", "Co-Op Advisor"])

    # Submit button to add the new user
    submit_button = st.form_submit_button("Add User")
    
    # If the form is submitted, add the new user to the session state
    if submit_button:
        if new_name:  # Ensure the name is not empty
            new_user = {"Name": new_name, "Role": new_role}
            st.session_state.data.append(new_user)  # Add new user to the list
            st.success(f"New user **{new_name}** added successfully!")
            st.rerun()  # Refresh the app to show the newly added user
        else:
            st.error("Please enter a name for the new user.")

# --- Filter and Sort Section ---
st.markdown("### Filter and Sort")

col1, col2, col3 = st.columns([5, 2, 2])

# Search bar
with col1:
    search_input = st.text_input("Search", placeholder="Type to search...")

# Filter dropdown
with col2:
    filter_option = st.selectbox(
        "Filter by", 
        options=["All", "Faculty", "Student", "Company", "Alumni"]
    )

# Sort dropdown
with col3:
    sort_option = st.selectbox(
        "Sort by", 
        options=["Name", "Role", "Date Added"]
    )

# --- Display User Table ---
st.divider()  # Adds a horizontal divider
st.markdown("### Users")

# Filter the data dynamically based on the search and filter inputs
filtered_data = st.session_state.data

if search_input:
    filtered_data = [user for user in filtered_data if search_input.lower() in user["Name"].lower()]
if filter_option != "All":
    filtered_data = [user for user in filtered_data if filter_option.lower() in user["Role"].lower()]

# Display the user table dynamically
if not filtered_data:
    st.warning("No users found matching the criteria.")
else:
    for row in filtered_data:
        with st.container():
            col1, col2, col3 = st.columns([3, 2, 1])
            # Button for the user's name
            if col1.button(row["Name"], key=row["Name"]):
                st.info(f"**You clicked on {row['Name']}!**")
            # Display the role
            col2.write(row["Role"])

            # Add a delete button
            if col3.button("Delete", key=f"delete_{row['Name']}"):
                # Remove the user from the data in session state
                st.session_state.data = [user for user in st.session_state.data if user != row]
                st.success(f"User {row['Name']} has been deleted.")
                st.rerun()  # Refresh to reflect the changes

        st.divider()
