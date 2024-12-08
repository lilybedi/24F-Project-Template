import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()
st.title(f"Welcome Company worker, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Add postings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/40_Add_Postings.py')

if st.button('Edit Postings', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/41_Edit_Postings.py')

if st.button('View Applications', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/42_View_Applications.py')
