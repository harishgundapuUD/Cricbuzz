import streamlit as st

def render():
    st.title("❓ FAQ")
    st.write("Frequently Asked Questions:")
    st.markdown("""
    **Q:** What is this app?  
    **A:** A demo of multi-page support in Streamlit.

    **Q:** How can I use it?  
    **A:** Navigate via the sidebar and explore!
    """)
