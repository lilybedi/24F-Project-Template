import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()



st.title('System Admin Home Page')

st.write(f"### Welcome, {st.session_state['first_name']}!")

st.write('\n\n')

with st.expander("See Open Tickets"):
    st.write('''
        Insert table with open tickets below once we have them!
    ''')

with st.expander("Manage Users"):
    st.write('''
        Insert table with 10 recently accessed users + a search bar that lets you search all users by USER ID
    ''')