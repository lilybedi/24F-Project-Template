import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Advisor, {st.session_state['first_name']}.")
import streamlit as st
import pandas as pd


# Sample data
data = {
"Name": ["Adam McStudent", "Kalina Monova", "Lily McStudent", "Anya McStudent"],
"Section": [1, 1, 1, 1],
"Applications": [300, 2, 5, 6],
"Status": ["Received offer", "Received offer", "Still Searching", "Received offer"],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

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