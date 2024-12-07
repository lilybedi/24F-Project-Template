import streamlit as st
from urllib.parse import unquote
import logging
logger = logging.getLogger(__name__)
st.set_page_config(layout="wide")

# Retrieve the selected application from session state
app = st.session_state.get("selected_application")

# Display the application details or show a warning if no application is found
if app:
    st.markdown(f"## {app['applicant_name']}'s Application")
    st.write(f"**Job:** {app['job']}")
    st.write(f"**Major/College:** {app['college']} / {app['major']}")
    st.write(f"**Graduation Year:** {app['grad_year']}")
    st.write(f"**GPA:** {app['gpa']}")
    st.write(f"**Cycle:** {app['cycle']}")
    st.markdown(f"[View Resume]({app['resume_link']})")
    
    # Button to return to the main page
    
# Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:
         # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "company":
            if st.button("Back to Applications"):
                st.switch_page("pages/42_View_Applications.py")
        # If the user is an advisor, give them access to the advisor pages 
        if st.session_state["role"] == "advisor":
            if st.button("Back to Student"):
                st.switch_page("pages/42_View_Applications.py")
    # else:
    #     st.warning("No application data available. Please go back and select an application.")

    
