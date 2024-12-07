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
st.title('Advisor Home Page')
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Students', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/45_Advisor_View_Students.py')
  
if st.button('Advisor Profile', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/Advisor_Profile.py')

st.write('\n\n')
