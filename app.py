import streamlit as st
import importlib

# Define the page structure
PAGES = {
    "Home": "pages.home",
    "Live Matches": "pages.live_matches",
    "Top Stats": "pages.top_stats",
    "SQL Queries": "pages.sql_queries",
    "CRUD Operations": "pages.crud_operations"
}

# Sidebar menu
st.sidebar.title("📚 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))


module = importlib.import_module(PAGES[selection])
module.render()
