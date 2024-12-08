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

# admin_id = st.session_state.get("alumni_id", 1)

# # try:
# #     # Fetch alumni profile details
# #     response = requests.get(f"{BASE_URL}/{admin_id}")
# #     response.raise_for_status()
# #     profile = response.json()
    
# #     # Display profile details
# #     st.markdown(f"""
# #     - **Name**: {profile['First_Name']} {profile['Last_Name']}
# #     """)
    
# # except requests.RequestException as e:
# #     st.error(f"Failed to fetch profile: {e}")

# try:
#         # Fetch admin profile details
#         response = requests.get(f"{BASE_URL}/sys/{admin_id}")
#         response.raise_for_status()
#         profile = response.json()

#         # Display profile details
#         st.markdown(f"""
#         - **Name**: {profile['First_Name']} {profile['Last_Name']}
#         - **Preferred Name**: {profile.get('Preferred_Name', 'N/A')}
#         """)

# except requests.RequestException as e:
#         st.error(f"Failed to fetch profile: {e}")

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