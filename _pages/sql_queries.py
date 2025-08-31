import streamlit as st
import pandas as pd
from utils.db_connection import SQLQuery

def render():
    st.title("🛠️ Services")
    questions = [
                    "Find all players representing India.",
                    "List cricket matches played in the last 30 days, sorted by most recent.",
                    "Show the top 10 highest ODI run scorers.",
                    "Display venues with seating capacity over 50,000.",
                    "Count players by playing role.",
                ]
    
    sql_queries = [
        "select name, playing_role, batting_style, bowling_style from indian_players",
        "select match_desc, team1_name, team2_name, venue_ground, venue_city, end_date from recent_matches order by end_date DESC",
        "select batter_name, runs, average from odi_info order by runs DESC limit 10",
        "select ground, city, country, capacity from venues_info where capacity>=50000",
        "SELECT playing_role, COUNT(*) as player_count FROM indian_players GROUP BY playing_role ORDER BY player_count DESC;"
    ]

    selected_option = st.selectbox("Choose an option:", questions)

    selected_index = questions.index(selected_option)

    db = SQLQuery()
    result = db.execute_query(sql_queries[selected_index])
    
    output = []
    for data in result:
        output.append(data)
    # print(output)
    # print("\n")

    df = pd.DataFrame(output)
    
    if selected_index == 0:
        df.columns = ["Name", "Role", "Batting Style", "Bowling Style"]
    elif selected_index == 1:
        df.columns = ["Match Description", "Team1", "Team2", "Venue", "City", "Date"]
        # Convert to datetime and format as d-m-y
        df['Date'] = pd.to_datetime(df['Date'], unit='ms').dt.strftime('%d-%m-%Y')
    elif selected_index == 2:
        df.columns = ["Name", "Runs", "Average"]
    elif selected_index == 3:
        df.columns = ["Venue", "City", "Country", "Capacity"]
    elif selected_index == 4:
        df.columns = ["Role", "Count"]
    
    # Display as DataFrame
    st.subheader("Query Results")
    st.dataframe(df)
    
    # Show statistics
    st.subheader("Data Overview")
    st.write(f"Total rows: {len(df)}")
    st.write(f"Total columns: {len(df.columns)}")