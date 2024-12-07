import streamlit as st
import requests

# Base API URL for alumni routes
BASE_URL = "http://api:4000/a"

st.set_page_config(layout="wide")
st.title(f"Welcome Alumni, {st.session_state.get('first_name', 'Guest')}!")

# Sidebar navigation
if st.sidebar.button("Chat with Lily McStudent"):
    st.switch_page("Chat_Lily.py")
if st.sidebar.button("Chat with Other Student"):
    st.switch_page("Other_Student.py")

# Display alumni profile
st.markdown("### Profile Details")
alumni_id = st.session_state.get("alumni_id", 1)  # Replace '1' with dynamic ID for real implementation

try:
    # Fetch alumni profile details
    response = requests.get(f"{BASE_URL}/{alumni_id}")
    response.raise_for_status()
    profile = response.json()

    # Display profile details
    st.markdown(f"""
    - **Name**: {profile['First_Name']} {profile['Last_Name']}
    - **Email**: {profile['Email']}
    - **Graduated**: {profile['Grad_Year']}
    - **College**: {profile['College']}
    - **Majors**: {profile['Majors']}
    - **Minors**: {profile['Minors']}
    """)

except requests.RequestException as e:
    st.error(f"Failed to fetch profile: {e}")

# Buttons for profile actions
if st.button("Edit Profile Details"):
    st.switch_page("Alumn_Edit.py")

if st.button("Add Co-op Experience"):
    st.switch_page("Add_Alumn_Experience.py")

# Alumni Previous Positions
st.markdown("### Previous Positions")
try:
    response = requests.get(f"{BASE_URL}/{alumni_id}/previous_positions")
    response.raise_for_status()
    positions = response.json()

    if positions["count"] > 0:
        st.write("#### Previous Positions:")
        for position in positions["positions"]:
            st.write(f"""
            - **Title**: {position['Title']}
            - **Company**: {position['Company_Name']} ({position['Industry']})
            - **Duration**: {position['Date_Start']} to {position['Date_End']}
            - **Pay**: ${position['Pay']}
            - **Location**: {position['City']}, {position['State']}, {position['Country']}
            - **Skills**: {", ".join(position['Required_Skills']) if position['Required_Skills'] else "None"}
            """)
    else:
        st.info("No previous positions found.")
except requests.RequestException as e:
    st.error(f"Failed to fetch previous positions: {e}")

# Alumni Messages
st.markdown("### Messages")
try:
    response = requests.get(f"{BASE_URL}/messages/{alumni_id}")
    response.raise_for_status()
    messages = response.json()

    if messages:
        st.write("#### Messages:")
        for message in messages:
            st.write(f"""
            - **From**: {message['Student_First_Name']} {message['Student_Last_Name']}
            - **Message**: {message['Message']}
            """)
    else:
        st.info("No messages found.")
except requests.RequestException as e:
    st.error(f"Failed to fetch messages: {e}")

# Send Message
st.markdown("### Send Message")
student_id = st.number_input("Enter Student ID:", min_value=1, step=1, value=1)
message = st.text_area("Message:")

if st.button("Send Message"):
    payload = {
        "Student_ID": student_id,
        "Alumni_ID": alumni_id,
        "Message": message,
    }
    try:
        response = requests.post(f"{BASE_URL}/messages/send", json=payload)
        response.raise_for_status()
        st.success("Message sent successfully!")
    except requests.RequestException as e:
        st.error(f"Failed to send message: {e}")
