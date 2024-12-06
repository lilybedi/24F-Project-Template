import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import pandas as pd

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()
# Fetch data from Flask API
# @st.cache_data
# def fetch_students_data():
#     try:
#         # Replace with the URL of your Flask API
#         api_url =  "/api/backend/students_routes"
#         response = requests.get(api_url)
#         response.raise_for_status()  # Raise an error for bad responses
#         data = response.json()

#         # Convert to DataFrame
#         df = pd.DataFrame(data, columns=["Name", "Section", "Applications", "Status"])
#         return df

#     except Exception as e:
#         logger.error(f"Error fetching data from API: {e}")
#         st.error("Failed to fetch data. Please check the API connection.")
#         return pd.DataFrame(columns=["Name", "Section", "Applications", "Status"])


# Main Streamlit app
st.title(f"Welcome Advisor, {st.session_state['first_name']}.")

# Fetch data from API

# needs to connect to the backend
df = fetch_students_data()

# Search bar
search_query = st.text_input("Search by name", value="")

# Filter dropdown
filter_option = st.radio(
    "Filter by status",
    options=["All", "Received Offer", "Still Searching"],
    horizontal=True
)

# Sort dropdown
sort_by = st.selectbox("Sort By", ["None", "Applications Ascending", "Applications Descending"])

# Start filtering data
filtered_df = df.copy()

# Apply search filter
if search_query.strip():
    filtered_df = filtered_df[filtered_df["Name"].str.contains(search_query.strip(), case=False, na=False)]

# Apply status filter
if filter_option == "Received Offer":
    filtered_df = filtered_df[filtered_df["Status"] == "Received offer"]
elif filter_option == "Still Searching":
    filtered_df = filtered_df[filtered_df["Status"] == "Still Searching"]

# Apply sorting
if sort_by == "Applications Ascending":
    filtered_df = filtered_df.sort_values(by="Applications", ascending=True)
elif sort_by == "Applications Descending":
    filtered_df = filtered_df.sort_values(by="Applications", ascending=False)

# Display the filtered data
if filtered_df.empty:
    st.warning("No data matches the current filters.")
else:
    st.table(filtered_df)