# import logging
# logger = logging.getLogger(__name__)
# import streamlit as st
# from streamlit_extras.app_logo import add_logo
# import numpy as np
# import random
# import time
# from modules.nav import SideBarLinks

import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title(f"Welcome Alumni , {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')