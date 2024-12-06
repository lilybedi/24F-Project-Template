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

st.title(f"Welcome Alumni, {st.session_state['first_name']}.")

# # Placeholder for student ID (replace with dynamic value in real implementation)
# student_id = st.session_state.get("student_id", 1)  # Replace '1' with actual student ID

# st.write('')
# st.write('')

import streamlit as st

st.sidebar.button("Chat with Lily McStudent", on_click=lambda: st.experimental_set_query_params(page="Chat_Lily"))
st.sidebar.button("Chat with Zara Studente", on_click=lambda: st.experimental_set_query_params(page="Chat_Zara"))

# Main content
st.markdown("""
### Profile:
- **Graduated**: 2022
- **Major**: Computer Science
- **Minor**: Neuroscience
- **GPA**: 3.8
- **Email**: neel@gmail.com
""")
if st.button("Edit Profile Details"):
    st.switch_page("pages/Alumn_Edit.py")
