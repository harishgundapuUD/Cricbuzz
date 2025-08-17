import streamlit as st
from utils.db_connection import SQLQuery

db = SQLQuery()

def render():
    st.title("👥 User Management Page")

    menu = st.selectbox("🔽 What would you like to do?", ["Add", "Update", "Delete", "View"])

    if menu == "Add":
        add_user()
    elif menu == "Update":
        update_user()
    elif menu == "Delete":
        delete_user()
    elif menu == "View":
        view_users()

def add_user():
    st.subheader("➕ Add New User")

    # Row 1: ID and Name
    name = st.text_input("Full Name")
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        matches = st.text_input("Matches Played")
    with row1_col2:
        player_type = st.selectbox("Player Type", ["", "Batsman", "Bowler", "All Rounder"])

    # Row 2: Email and Age
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        runs = st.text_input("Runs Scored")
    with row2_col2:
        wickets = st.text_input("Wickets Taken")

    # Row 3: Batting and Bowling Type
    row3_col1, row3_col2 = st.columns(2)
    with row3_col1:
        batting_type = st.selectbox("Batting Type", ["", "Right Handed", "Left Handed"])
    with row3_col2:
        bowling_type = st.selectbox("Bowling Type", ["", "Right Arm Fast", "Left Arm Fast", 
                                                     "Right Arm Spin", "Left Arm Spin", 
                                                     "Right Arm Medium", "Left Arm Medium"])
    
    # Row 4: Fours and Sixes
    row4_col1, row4_col2 = st.columns(2)
    with row4_col1:
        fours = st.text_input("4's")
    with row4_col2:
        sixes = st.text_input("6's")
    
    # Row 5: Fifties and Hundreds
    row5_col1, row5_col2 = st.columns(2)
    with row5_col1:
        fifties = st.text_input("50's")
    with row5_col2:
        hundreds = st.text_input("100's")
    
    # Row 6: Hundreds
    # row6_col1, row6_col2 = st.columns(2)
    # with row6_col1:
        

    if st.button("Add User"):
        before = db.get_user_count()
        if name and email:
            db.add_user(name, email)
            after = db.get_user_count()
            st.success(f"User '{name}' added.")
            st.info(f"Users before: {before}, after: {after}")
        else:
            st.warning("Please enter both name and email.")

def update_user():
    st.subheader("✏️ Update User")
    users = db.get_users()
    user_dict = {f"{u[0]}: {u[1]} ({u[2]})": u for u in users}

    if users:
        selected = st.selectbox("Select a user to update", list(user_dict.keys()))
        selected_user = user_dict[selected]

        new_name = st.text_input("New Name", value=selected_user[1])
        new_email = st.text_input("New Email", value=selected_user[2])

        if st.button("Update User"):
            db.update_user(selected_user[0], new_name, new_email)
            st.success("User updated.")
    else:
        st.info("No users found to update.")

def delete_user():
    st.subheader("❌ Delete User")
    users = db.get_users()
    user_dict = {f"{u[0]}: {u[1]} ({u[2]})": u[0] for u in users}

    if users:
        selected = st.selectbox("Select a user to delete", list(user_dict.keys()))
        if st.button("Delete User"):
            db.delete_user(user_dict[selected])
            st.success("User deleted.")
    else:
        st.info("No users to delete.")

def view_users():
    st.subheader("📋 All Users")
    users = db.get_users()
    count = db.get_user_count()
    st.info(f"Total users: {count}")
    if users:
        st.table(users)
    else:
        st.warning("No users found.")
