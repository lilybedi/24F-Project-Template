import streamlit as st
from modules.nav import SideBarLinks

# Set page configuration
st.set_page_config(layout="wide", page_title="Dashboard", page_icon="👤")

# Initialize the navigation sidebar
SideBarLinks()

# --- Welcome Section with User Profile ---
st.markdown("## Welcome, Amber")

# --- Open Tickets Section ---
st.markdown("### Open Tickets")

# TICKETS NEED TO BE CONNECTED TO BACKEND
if "tickets" not in st.session_state:
    st.session_state.tickets = [
        {"title": "Broken website page", "time": "Today at 11:57PM"},
        {"title": "403 error", "time": "Today at 2:32PM"},
        {"title": "Can’t see student resumés", "time": "Today at 11:15AM"},
        {"title": "Crazy thing just happened", "time": "Today at 5:47AM"},
        {"title": "New ticket example", "time": "Yesterday at 10:00PM"},
    ]

# Display tickets as a table with clickable buttons
st.markdown("#### Click on a ticket to view details:")

# Check if there are any tickets
if not st.session_state.tickets:
    st.warning("No tickets available.")  # Handle empty ticket list gracefully
else:
    for ticket in st.session_state.tickets:
        with st.container():
            # Use a container for each ticket row
            col1, col2, col3, col4 = st.columns([4, 3, 1, 1])  # Adjusted column layout
            col2.write(ticket["title"])  # Ticket title
            col3.write(ticket["time"])   # Ticket timestamp
            
            # Button to view the ticket details
            if col4.button("View", key=f"view_{ticket['title']}"):
                st.info(f"You clicked on: **{ticket['title']}**")
            
            # Button to mark the ticket as resolved (delete it)
            if col1.button("Mark as Resolved", key=f"resolved_{ticket['title']}"):
                # Remove the ticket from the list in session state
                st.session_state.tickets = [t for t in st.session_state.tickets if t != ticket]
                st.success(f"Ticket **{ticket['title']}** has been marked as resolved and removed.")
                st.rerun()  # Refresh to reflect the changes

        st.divider()  # Add a divider after each ticket for better separation
