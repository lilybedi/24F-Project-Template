import streamlit as st
import logging
logger = logging.getLogger(__name__)
import requests  # You can use this to make API calls in real-world apps
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(layout="centered", page_title="Admin Profile", page_icon="🛠️")
SideBarLinks()

# --- Check if 'first_name' is in session state and display it ---
if 'first_name' not in st.session_state:
    st.session_state['first_name'] = 'Admin'  # Default value if not set


# Admin Profile Information NEEDS TO BE CONNECTED TO BACKEND
admin_profile = {
    "ID": "123243435",
    "role": "System Admin",
    "last_login": "2024-12-06 09:45 AM"
}

# --- Admin Profile Display ---
st.markdown(f"# Welcome, {st.session_state['first_name']}.")

# Display the admin's profile in two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Admin Information")
    st.write(f"**Name**: {st.session_state['first_name']}")
    st.write(f"**ID**: {admin_profile['ID']}")
    st.write(f"**Role**: {admin_profile['role']}")
    st.write(f"**Last Login**: {admin_profile['last_login']}")

# --- Footer Section ---
st.markdown("---")
