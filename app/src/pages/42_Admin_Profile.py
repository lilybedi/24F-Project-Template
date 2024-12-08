# admin_profile.py
import streamlit as st
import logging
import requests
from datetime import datetime
from modules.nav import SideBarLinks

logger = logging.getLogger(__name__)

# Constants
API_BASE_URL = "http://api:4000/sys"  # Adjust based on your Flask backend URL
DEFAULT_ADMIN_ID = 1

def fetch_admin_data(admin_id):
    """Fetch admin data from backend API"""
    try:
        response = requests.get(f"{API_BASE_URL}/{admin_id}")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to fetch admin data: {response.status_code}")
            return None
    except Exception as e:
        logger.error(f"Error fetching admin data: {str(e)}")
        return None

def fetch_tickets():
    """Fetch tickets from backend API"""
    try:
        response = requests.get(f"{API_BASE_URL}/tickets")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to fetch tickets: {response.status_code}")
            return []
    except Exception as e:
        logger.error(f"Error fetching tickets: {str(e)}")
        return []

def fetch_recent_applications():
    """Fetch recent applications from backend API"""
    try:
        response = requests.get(f"{API_BASE_URL}/activity/applications")
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to fetch applications: {response.status_code}")
            return []
    except Exception as e:
        logger.error(f"Error fetching applications: {str(e)}")
        return []

def main():
    # Page configuration
    st.set_page_config(layout="centered", page_title="Admin Profile", page_icon="🛠️")
    SideBarLinks()

    # Initialize session state
    if 'admin_data' not in st.session_state:
        admin_data = fetch_admin_data(DEFAULT_ADMIN_ID)
        if admin_data:
            st.session_state['admin_data'] = admin_data
            st.session_state['first_name'] = admin_data.get('First_Name', 'Admin')
        else:
            st.session_state['first_name'] = 'Admin'

    # Main header
    st.markdown(f"# Welcome, {st.session_state['first_name']}!")

    # Admin Profile Section
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Admin Information")
        if 'admin_data' in st.session_state:
            admin_data = st.session_state['admin_data']
            st.write(f"**Name**: {admin_data.get('First_Name', '')} {admin_data.get('Last_Name', '')}")
            st.write(f"**Preferred Name**: {admin_data.get('Preferred_Name', 'Not set')}")
            st.write(f"**ID**: {admin_data.get('ID', '')}")
            st.write(f"**Role**: System Administrator")
            st.write(f"**Last Login**: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}")

    # System Settings and Actions
    with col2:
        st.subheader("Quick Actions")
        if st.button("System Settings"):
            st.info("System settings would be implemented here!")
        if st.button("Refresh Data"):
            st.session_state['admin_data'] = fetch_admin_data(DEFAULT_ADMIN_ID)
            st.rerun()

    # Tickets Section
    st.markdown("---")
    st.subheader("Recent Support Tickets")
    tickets = fetch_tickets()
    if tickets:
        for ticket in tickets[:5]:  # Show last 5 tickets
            with st.expander(f"Ticket #{ticket['ID']}: {ticket['Message'][:50]}..."):
                st.write(f"**Reporter**: {ticket['Reporter_First_Name']} {ticket['Reporter_Last_Name']}")
                st.write(f"**Status**: {'Completed' if ticket['Completed'] else 'Pending'}")
                if not ticket['Completed']:
                    if st.button("Mark Complete", key=f"ticket_{ticket['ID']}"):
                        try:
                            requests.put(
                                f"{API_BASE_URL}/tickets/{ticket['ID']}", 
                                json={"completed": True}
                            )
                            st.success("Ticket marked as complete!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Failed to update ticket: {str(e)}")

    # Recent Applications Section
    st.markdown("---")
    st.subheader("Recent Applications")
    applications = fetch_recent_applications()
    if applications:
        for app in applications[:5]:  # Show last 5 applications
            with st.expander(f"Application: {app['Position_Name']} at {app['Company_Name']}"):
                st.write(f"**Student**: {app['Student_First_Name']} {app['Student_Last_Name']}")
                st.write(f"**Submitted**: {app['submittedDate']}")
                st.write(f"**Status**: {app['Status_Description']}")

    # Footer
    st.markdown("---")
    st.markdown("*For technical support, please contact the IT department.*")

if __name__ == "__main__":
    main()