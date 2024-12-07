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

if st.sidebar.button("Chat with Lily McStudent"):
    st.switch_page("pages/Chat_Lily.py")
st.sidebar.button("Chat with Other Student", on_click=lambda: st.switch_page("pages/Other_Student.py"))

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

if st.button("Add co-op experience"):
    st.switch_page("pages/Add_Alumn_Experience.py")
