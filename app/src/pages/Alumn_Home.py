# import logging
# logger = logging.getLogger(__name__)
# import streamlit as st
# from streamlit_extras.app_logo import add_logo
# import numpy as np
# import random
# import time
# from modules.nav import SideBarLinks

import logging

import requests
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()
import requests
import streamlit as st

# Example Streamlit page
st.title("Filter Postings by Location")

# Input field for location
location = st.text_input("Enter location (city, state, or country):")

# Button to trigger API call
if st.button("Search"):
    if location:
        try:
            # Make the API call
            response = requests.get(
                "http://api:4000/s/postings/by_location",
                params={"location": location},
            )
            
            # Raise error for bad status codes
            response.raise_for_status()
            
            # Parse and display the data
            data = response.json()
            st.write(f"Results for location: {location}")
            st.dataframe(data)
        except requests.RequestException as e:
            st.error(f"Error fetching data: {e}")
    else:
        st.error("Please enter a location before searching.")


# st.title(f"Welcome Alumni , {st.session_state['first_name']}.")
# st.write('')
# st.write('')
# st.write('### What would you like to do today?')

# data = {} 
# try:
#   data = requests.get('http://api:4000/s/get_all').json()
# except:
#   st.write("**Important**: Could not connect to sample api, so using dummy data.")
#   data = {"a":{"b": "123", "c": "hello"}, "z": {"b": "456", "c": "goodbye"}}

# st.dataframe(data)