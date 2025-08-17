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
        if name and matches and runs and player_type and batting_type and bowling_type and fours and sixes and fifties and hundreds and wickets:
            data = {
                        "name": name,
                        "matches": matches,
                        "runs": runs,
                        "player_type": player_type,
                        "batting_type": batting_type,
                        "bowling_type": bowling_type,
                        "fours": fours,
                        "sixes": sixes,
                        "fifties": fifties,
                        "hundreds": hundreds,
                        "wickets": wickets
                    }
            db.add_user(input_data=data)
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

    all_users = db.get_users()  # list of tuples (id, name, email, ...)
    # Build a list of user display strings
    user_display_list = [f"{u[0]}: {u[1]} ({u[2]})" for u in all_users]

    # Search box for filtering
    search_term = st.text_input("Search user by name to delete")

    if search_term:
        # Filter users whose name contains the search term (case-insensitive)
        filtered_users = [u for u in all_users if search_term.lower() in u[1].lower()]
        if filtered_users:
            filtered_display = [f"{u[0]}: {u[1]} ({u[2]})" for u in filtered_users]
        else:
            filtered_display = []
    else:
        # No search term => show all users
        filtered_display = user_display_list

    if filtered_display:
        selected = st.selectbox("Select a user to delete", filtered_display)
        # Get user info from selected string
        selected_id = int(selected.split(":")[0])
        selected_user = next((u for u in all_users if u[0] == selected_id), None)
        user_name = selected_user[1]

        # Confirmation input
        confirm_text = st.text_input(f"Type 'delete {user_name}' to confirm")

        if st.button("Delete User"):
            if confirm_text == f"delete {user_name}":
                db.delete_user(selected_id)
                st.success(f"User '{user_name}' deleted.")
            else:
                st.error("Confirmation text does not match. Deletion aborted.")
    else:
        st.info("No users found matching your search.")



def view_users():
    st.subheader("📋 All Users")
    users = db.get_users()
    count = db.get_user_count()
    st.info(f"Total users: {count}")
    if users:
        st.table(users)
    else:
        st.warning("No users found.")
