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
        {"role": "Jeremy", "content": "Hi Lily, just wanted to check in on how your interview went today?"},
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to Neel's input
if lily_message := st.chat_input("Lily: Type your message here..."):
    # Display Neel's message
    with st.chat_message("Lily"):
        st.markdown(lily_message)

    # Add Neel's message to chat history
    st.session_state.messages.append({"role": "Lily", "content": lily_message})
