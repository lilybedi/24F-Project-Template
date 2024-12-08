import streamlit as st
import requests
from datetime import datetime
from modules.nav import SideBarLinks
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_tickets() -> List[Dict]:
    """Fetch tickets from the backend API."""
    try:
        response = requests.get('http://api:4000/sys/tickets')
        if response.status_code == 200:
            tickets = response.json()
            # Format the tickets data
            formatted_tickets = []
            for ticket in tickets:
                formatted_tickets.append({
                    "id": ticket["ID"],
                    "title": ticket["Message"],
                    "reporter": f"{ticket['Reporter_First_Name']} {ticket['Reporter_Last_Name']}",
                    "completed": ticket["Completed"],
                    "time": ticket.get("created_at", "No date available")  # Add if you have timestamp in backend
                })
            return formatted_tickets
        else:
            st.error(f"Error fetching tickets: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to the backend: {str(e)}")
        return []

def mark_ticket_resolved(ticket_id: int) -> bool:
    """Mark a ticket as resolved in the backend."""
    try:
        response = requests.put(
            f'http://api:4000/sys/tickets/{ticket_id}',
            json={"completed": True}
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to update ticket: {str(e)}")
        return False

# Set page configuration
st.set_page_config(layout="wide", page_title="Tickets Dashboard", page_icon="🎫")

# Initialize the navigation sidebar
SideBarLinks()

# Welcome Section with User Profile
st.markdown("## System Admin Ticket Dashboard")

# Fetch tickets from backend
if "tickets" not in st.session_state or st.button("Refresh Tickets"):
    st.session_state.tickets = fetch_tickets()

# Open Tickets Section
st.markdown("### Open Tickets")

# Display tickets
if not st.session_state.tickets:
    st.warning("No tickets available.")
else:
    # Create a container for the tickets list
    tickets_container = st.container()
    
    with tickets_container:
        for ticket in st.session_state.tickets:
            if not ticket["completed"]:  # Only show uncompleted tickets
                with st.container():
                    cols = st.columns([3, 2, 2, 1, 1])
                    
                    # Ticket information
                    cols[0].write(ticket["title"])
                    cols[1].write(f"Reporter: {ticket['reporter']}")
                    cols[2].write(ticket["time"])
                    
                    # View button
                    if cols[3].button("View", key=f"view_{ticket['id']}"):
                        st.session_state.selected_ticket = ticket
                        st.info(
                            f"""
                            **Ticket Details:**
                            - Title: {ticket['title']}
                            - Reporter: {ticket['reporter']}
                            - Status: {'Completed' if ticket['completed'] else 'Open'}
                            - Time: {ticket['time']}
                            """
                        )
                    
                    # Resolve button
                    if cols[4].button("Resolve", key=f"resolve_{ticket['id']}"):
                        if mark_ticket_resolved(ticket['id']):
                            st.success(f"Ticket '{ticket['title']}' has been marked as resolved.")
                            # Remove from session state
                            st.session_state.tickets = [t for t in st.session_state.tickets if t['id'] != ticket['id']]
                            st.rerun()
                        else:
                            st.error("Failed to mark ticket as resolved. Please try again.")
                
                st.divider()

# Add a "Show Resolved Tickets" section
if st.checkbox("Show Resolved Tickets"):
    st.markdown("### Resolved Tickets")
    resolved_exists = False
    
    for ticket in st.session_state.tickets:
        if ticket["completed"]:
            resolved_exists = True
            with st.container():
                cols = st.columns([3, 2, 2, 1])
                cols[0].write(ticket["title"])
                cols[1].write(f"Reporter: {ticket['reporter']}")
                cols[2].write(ticket["time"])
                
                if cols[3].button("View", key=f"view_resolved_{ticket['id']}"):
                    st.info(
                        f"""
                        **Resolved Ticket Details:**
                        - Title: {ticket['title']}
                        - Reporter: {ticket['reporter']}
                        - Status: Resolved
                        - Time: {ticket['time']}
                        """
                    )
            st.divider()
    
    if not resolved_exists:
        st.info("No resolved tickets found.")