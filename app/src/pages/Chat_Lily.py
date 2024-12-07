import logging
logger = logging.getLogger(__name__)
import streamlit as st
from streamlit_extras.app_logo import add_logo
import random
import time
from modules.nav import SideBarLinks

SideBarLinks()


# st.set_page_config(page_title="Neel & Lily Chat", page_icon="💬")
add_logo("assets/logo.png", height=400)

st.title("Your chat with Lily McStudent")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "Lily", "content": "Hi Neel! I saw that you did a co-op at Bain Capital. Can you tell me a little bit about what your day to day was like?"},
        {"role": "Neel", "content": "Hi Lily! Yes of course I can. In my position I ... blah blah content stuff work things.... What year & co-op cycle are you?"},
        {"role": "Lily", "content": "I am a second year fall co-op. Thanks for providing that insight on your day to day. What was your relationship like with your driect supervisors? I want to be under soemone who I can learn a lot from. Was that your experience at Bain?"},
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to Neel's input
if neel_message := st.chat_input("Neel: Type your message here..."):
    # Display Neel's message
    with st.chat_message("Neel"):
        st.markdown(neel_message)

    # Add Neel's message to chat history
    st.session_state.messages.append({"role": "Neel", "content": neel_message})
