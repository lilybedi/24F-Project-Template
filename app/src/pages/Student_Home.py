import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Student, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Job Apps', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'usaid_worker'
    st.session_state['first_name'] = 'Mohammad'
    st.switch_page('pages/32_Job_Apps.py')

if st.button('Student profile', 
            type = 'primary', 
            use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'administrator'
    st.session_state['first_name'] = 'SysAdmin'
    st.switch_page('pages/31_Student_Profile.py')

# if st.button('View World Bank Data Visualization', 
#              type='primary',
#              use_container_width=True):
#   st.switch_page('pages/01_World_Bank_Viz.py')

# if st.button('View World Map Demo', 
#              type='primary',
#              use_container_width=True):
#   st.switch_page('pages/02_Map_Demo.py')