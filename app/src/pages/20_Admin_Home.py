import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests


st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('System Admin Home Page')

st.write(f"### Welcome, {st.session_state['first_name']}!")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('See Tickets', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/43_See_Tickets.py')

if st.button('See All Users', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/44_See_All_Users.py')

if st.button('Admin Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/42_Admin_Profile.py')

st.write('\n\n')