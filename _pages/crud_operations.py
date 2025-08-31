import streamlit as st
from utils.db_connection import SQLQuery

db = SQLQuery()

def render():
    st.title("👥 User Management Page")
    menu = st.selectbox("🔽 What would you like to do?", ["View", "Update", "Delete", "Add"])
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

    # Row 1: player_id and name
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        player_id = st.text_input("Player ID", key="player_id_input")
    with row1_col2:
        name = st.text_input("Name", key="name_input")

    # Row 2: matches and innings
    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        matches = st.text_input("Matches",key="matches_input")
    with row2_col2:
        innings = st.text_input("Innings",key="innings_input")

    # Row 3: runs and average
    row3_col1, row3_col2 = st.columns(2)
    with row3_col1:
        runs = st.text_input("Runs",key="runs-input")
    with row3_col2:
        average = st.text_input("Average",key="average_input")
        
    if st.button("Add User"):
        before = db.get_user_count(table="players")
        if name and matches and runs and player_id and innings and average:
            data = {
                        "name": name,
                        "matches": matches,
                        "runs": runs,
                        "player_id": player_id,
                        "innings": innings,
                        "average": average
                    }
            db.add_user(input_data=data)
            after = db.get_user_count(table="players")
            st.success(f"User '{name}' added.")
            st.info(f"Users before: {before}, after: {after}")
        else:
            st.warning("Please enter both name and email.")

def update_user():
    st.subheader("✏️ Update User")
    users = db.get_users()
    
    if users:
        # Create display options with proper column names
        user_options = [f"{u['player_id']}: {u['name']} ({u['matches']} matches)" for u in users]
        selected = st.selectbox("Select a user to update", user_options)
        
        # Get the selected user's ID
        selected_id = int(selected.split(":")[0])
        selected_user = next((u for u in users if u['player_id'] == selected_id), None)
        
        if selected_user:
            row1_col1, row1_col2 = st.columns(2)
            with row1_col1:
                new_player_id = st.text_input("New Player ID", value=str(selected_user['player_id']))
            with row1_col2:
                new_name = st.text_input("New Name", value=selected_user['name'])

            # Row 2: matches and innings
            row2_col1, row2_col2 = st.columns(2)
            with row2_col1:
                new_matches = st.text_input("New Matches", value=str(selected_user['matches']))
            with row2_col2:
                new_innings = st.text_input("New Innings", value=selected_user['innings'])

            # Row 3: runs and average
            row3_col1, row3_col2 = st.columns(2)
            with row3_col1:
                new_runs = st.text_input("New Runs", value=str(selected_user['runs']))
            with row3_col2:
                new_average = st.text_input("New Average", value=str(selected_user['average']))
        
            new_data = {
                "player_id": int(new_player_id),
                "name": new_name,
                "matches": int(new_matches),
                "innings": new_innings,
                "runs": int(new_runs),
                "average": float(new_average)
            }

            if st.button("Update User"):
                db.update_user(input_data=new_data)
                st.success("User updated.")
    else:
        st.info("No users found to update.")

def delete_user():
    st.subheader("❌ Delete User")

    all_users = db.get_users()
    
    if all_users:
        # Build display list with proper column names
        user_display_list = [f"{u['player_id']}: {u['name']} ({u['matches']} matches)" for u in all_users]

        # Search box for filtering
        search_term = st.text_input("Search user by name to delete")

        if search_term:
            # Filter users whose name contains the search term
            filtered_users = [u for u in all_users if search_term.lower() in u['name'].lower()]
            filtered_display = [f"{u['player_id']}: {u['name']} ({u['matches']} matches)" for u in filtered_users]
        else:
            filtered_display = user_display_list

        if filtered_display:
            selected = st.selectbox("Select a user to delete", filtered_display)
            selected_id = int(selected.split(":")[0])
            selected_user = next((u for u in all_users if u['player_id'] == selected_id), None)
            
            if selected_user:
                user_name = selected_user['name']
                confirm_text = st.text_input(f"Type 'delete {user_name}' to confirm")

                if st.button("Delete User"):
                    if confirm_text == f"delete {user_name}":
                        db.delete_user(selected_id)
                        st.success(f"User '{user_name}' deleted.")
                    else:
                        st.error("Confirmation text does not match. Deletion aborted.")
        else:
            st.info("No users found matching your search.")
    else:
        st.info("No users found to delete.")

def view_users():
    st.subheader("📋 All Users")
    users = db.get_users()
    count = db.get_user_count(table="players")
    st.info(f"Total users: {count}")
    
    if users:
        import pandas as pd
        df = pd.DataFrame(users)
        
        # CSS specifically for tables
        st.markdown("""
        <style>
        table {
            text-align: left !important;
            width: 100%;
        }
        th {
            text-align: left !important;
            font-weight: bold;
        }
        td {
            text-align: left !important;
        }
        </style>
        """, unsafe_allow_html=True)
        # Rename columns for display purposes only
        column_mapping = {
            'player_id': 'Player ID',
            'name': 'Name', 
            'matches': 'Matches',
            'innings': 'Innings',
            'runs': 'Runs',
            'average': 'Average'
        }
        
        # Create a copy of the data for display
        display_data = []
        for user in users:
            display_user = user.copy()
            # Format average to 2 decimals for display only
            try:
                display_user['average'] = f"{float(user['average']):.2f}"
            except (ValueError, TypeError):
                display_user['average'] = user['average']  # Keep original if conversion fails
            display_data.append(display_user)
        
        # Convert to DataFrame
        df = pd.DataFrame(display_data)

        # Rename the columns for display
        df = df.rename(columns=column_mapping)
            
        st.table(df)
        
    else:
        st.warning("No users found.")