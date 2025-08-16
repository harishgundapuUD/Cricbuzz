import streamlit as st
import importlib

# Define the page structure
PAGES = {
    "Home": "_pages.home",
    "Live Matches": "_pages.live_matches",
    "Top Stats": "_pages.top_stats",
    "SQL Queries": "_pages.sql_queries",
    "CRUD Operations": "_pages.crud_operations"
}

# Sidebar menu
st.sidebar.title("📚 Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))


module = importlib.import_module(PAGES[selection])
module.render()
