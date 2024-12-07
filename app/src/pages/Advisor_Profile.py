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

# Profile section
st.image("./assets/profile_photo.png", width=100)  # Replace with the actual path to the sunflower image
st.markdown("<h3 style='text-align: center;'>Welcome, Susan</h3>", unsafe_allow_html=True)

# Spacer
st.write("")

# Recent Activity section
st.markdown("### Recent Activity")
recent_activity = [
    {"Activity": "STUDENT accepted an offer at COMPANY", "Time": "Today at 11:59PM"},
    {"Activity": "STUDENT got a co-op offer at COMPANY", "Time": "Today at 11:29PM"},
    {"Activity": "STUDENT accepted an offer at COMPANY", "Time": "Today at 10:42PM"},
    {"Activity": "STUDENT got a co-op offer at COMPANY", "Time": "Today at 9:30PM"},
]
for activity in recent_activity:
    st.markdown(
        f"<div style='display: flex; justify-content: space-between; padding: 5px; border-bottom: 1px solid #ddd;'>"
        f"<span>{activity['Activity']}</span><span style='color: gray;'>{activity['Time']}</span></div>",
        unsafe_allow_html=True,
    )

# Spacer
st.write("")
