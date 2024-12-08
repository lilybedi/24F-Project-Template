import streamlit as st
import requests
import logging
from modules.nav import SideBarLinks

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API endpoint configuration
API_BASE_URL = "http://api:4000/sys"

def fetch_users():
    """Fetch all users from different tables"""
    try:
        response = requests.get(f"{API_BASE_URL}/users")
        if response.status_code == 200:
            users = []
            for user in response.json():
                name = f"{user['First_Name']} {user['Last_Name']}"
                if user.get('Preferred_Name'):
                    name = f"{user['Preferred_Name']} ({name})"
                    
                users.append({
                    "Name": name,
                    "Role": user['Type'].capitalize(),
                    "ID": user['ID'],
                    "Type": user['Type']
                })
            return users
        else:
            logger.error(f"Error fetching users: {response.text}")
            return []
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return []

def delete_user(user_type, user_id):
    """Delete a user from the system"""
    try:
        response = requests.delete(f"{API_BASE_URL}/accounts/{user_type}/{user_id}")
        return response.status_code == 200, response.json().get("message", "Error occurred")
    except Exception as e:
        logger.error(f"Error deleting user: {str(e)}")
        return False, f"Error occurred: {str(e)}"

def add_user(user_data, role):
    """Add a new user to the system"""
    try:
        if role == "Advisor":
            response = requests.post(
                f"{API_BASE_URL}/advisors/add",
                json={
                    "First_Name": user_data["first_name"],
                    "Last_Name": user_data["last_name"],
                    "Preferred_Name": user_data.get("preferred_name"),
                    "College_ID": user_data.get("college_id")
                }
            )
            return response.status_code == 201, response.json().get("message", "Error occurred")
        # Add handlers for other roles

    except Exception as e:
        logger.error(f"Error adding user: {str(e)}")
        return False, f"Error occurred: {str(e)}"

# Set the page layout
st.set_page_config(layout="wide", page_title="User Management", page_icon="👥")

# Initialize the navigation sidebar
SideBarLinks()

st.markdown("# Manage Users")

# Initialize session state for users if not exists
if "users" not in st.session_state:
    st.session_state.users = fetch_users()

# --- User Management Section ---
st.markdown("### Add New User")

# Create a form to add a new user
with st.form(key='add_advisor_form'):
    col1, col2 = st.columns(2)
    with col1:
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
    with col2:
        preferred_name = st.text_input("Preferred Name (Optional)")
        college_id = st.text_input("College ID")

    submit_button = st.form_submit_button("Add Advisor")
    
    if submit_button:
        if first_name and last_name and college_id:
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "preferred_name": preferred_name,
                "college_id": college_id
            }
            success, message = add_user(user_data, "Advisor")
            if success:
                st.success(f"New advisor added successfully!")
                st.session_state.users = fetch_users()  # Refresh user list
                st.rerun()
            else:
                st.error(message)
        else:
            st.error("Please enter First Name, Last Name, and College ID.")
    if submit_button:
        if first_name and last_name:
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "preferred_name": preferred_name,
                "college_id": college_id if role == "Advisor" else None
            }
            success, message = add_user(user_data, role)
            if success:
                st.success(f"New user added successfully!")
                st.session_state.users = fetch_users()  # Refresh user list
                st.rerun()
            else:
                st.error(message)
        else:
            st.error("Please enter both first and last names.")

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
        options=["All", "Advisor", "Student", "Alumni"]
    )

# Sort dropdown
with col3:
    sort_option = st.selectbox(
        "Sort by", 
        options=["Name", "Role"]
    )

# --- Display User Table ---
st.divider()
st.markdown("### Users")

# Filter and sort the data
filtered_data = st.session_state.users

if search_input:
    filtered_data = [user for user in filtered_data 
                    if search_input.lower() in user["Name"].lower()]
if filter_option != "All":
    filtered_data = [user for user in filtered_data 
                    if filter_option == user["Role"]]

# Sort the data
filtered_data.sort(key=lambda x: x[sort_option])

# Display the user table
if not filtered_data:
    st.warning("No users found matching the criteria.")
else:
    for idx, user in enumerate(filtered_data):  # Use enumerate to get an index for each user
        with st.container():
            col1, col2, col3 = st.columns([3, 2, 1])
            
            col1.write(user["Name"])
            col2.write(user["Role"])
            
            # Use idx to ensure uniqueness of the key
            if col3.button("Delete", key=f"delete_{user['ID']}_{idx}"):
                success, message = delete_user(user["Type"], user["ID"])
                if success:
                    st.success(f"User {user['Name']} has been deleted.")
                    st.session_state.users = fetch_users()  # Refresh user list
                    st.rerun()
                else:
                    st.error(message)
                    
        st.divider()

# Add a refresh button
if st.button("Refresh User List"):
    st.session_state.users = fetch_users()
    st.rerun()