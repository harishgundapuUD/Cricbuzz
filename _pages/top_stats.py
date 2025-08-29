import streamlit as st
import pandas as pd

# Provided JSON
data = {
    'player': [
        {'id': '674', 'name': 'Kwame Tucker', 'teamName': 'Bermuda', 'faceImageId': '155488', 'dob': '1976-09-28', 'birthPlace': 'Hamilton, Bermuda', 'height': "5'10\"", 'role': 'Batsman', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'Right-arm medium', 'internationalTeam': 'Bermuda', 'teamsPlayedFor': ['Bermuda National Team']},
        {'id': '673', 'name': 'Janeiro Tucker', 'teamName': 'Bermuda', 'faceImageId': '155599', 'dob': '1975-03-15', 'birthPlace': 'Hamilton, Bermuda', 'height': "5'9\"", 'role': 'All-rounder', 'battingStyle': 'Left-hand bat', 'bowlingStyle': 'Right-arm offbreak', 'internationalTeam': 'Bermuda', 'teamsPlayedFor': ['Bermuda National Team']},
        {'id': '866', 'name': 'Tamauri Tucker', 'teamName': 'Bermuda', 'faceImageId': '155612', 'dob': '1988-12-10', 'birthPlace': 'Hamilton, Bermuda', 'height': "6'0\"", 'role': 'Batsman', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'N/A', 'internationalTeam': 'Bermuda', 'teamsPlayedFor': ['Bermuda National Team']},
        {'id': '11131', 'name': 'Lorcan Tucker', 'teamName': 'Ireland', 'faceImageId': '244650', 'dob': '1996-09-10', 'birthPlace': 'Dublin, Ireland', 'height': "5'11\"", 'role': 'Wicketkeeper-Batsman', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'N/A', 'internationalTeam': 'Ireland', 'teamsPlayedFor': ['Ireland National Team']},
        {'id': '26178', 'name': 'Delmi Tucker', 'teamName': 'South Africa', 'faceImageId': '255000', 'dob': '1997-03-05', 'birthPlace': 'Johannesburg, South Africa', 'height': "5'7\"", 'role': 'All-rounder', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'Right-arm medium', 'internationalTeam': 'South Africa', 'teamsPlayedFor': ['South Africa National Team']},
        {'id': '7240', 'name': 'Rod Tucker', 'teamName': 'Australia', 'faceImageId': '182026', 'dob': '1964-08-28', 'birthPlace': 'Tasmania, Australia', 'height': "5'10\"", 'role': 'Umpire', 'battingStyle': 'N/A', 'bowlingStyle': 'N/A', 'internationalTeam': 'Australia', 'teamsPlayedFor': ['Australia National Team']},
        {'id': '11123', 'name': 'Fiachra Tucker', 'teamName': 'Ireland', 'faceImageId': '182026', 'dob': 'N/A', 'birthPlace': 'N/A', 'height': "N/A", 'role': 'Batsman', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'N/A', 'internationalTeam': 'Ireland', 'teamsPlayedFor': ['Ireland National Team']},
        {'id': '38265', 'name': 'Emily Tucker', 'teamName': 'Scotland', 'faceImageId': '182026', 'dob': 'N/A', 'birthPlace': 'N/A', 'height': "N/A", 'role': 'Batsman', 'battingStyle': 'Right-hand bat', 'bowlingStyle': 'N/A', 'internationalTeam': 'Scotland', 'teamsPlayedFor': ['Scotland National Team']}
    ],
    'category': 'Tucker'
}

def render():
    st.title("Player Search")
    search_name = st.text_input("Enter player name:")
    searched_data(search_name=search_name, api_data=data)

def searched_data(search_name, api_data):
    if search_name:
        matched_players = [p for p in api_data['player'] if search_name.lower() in p['name'].lower()]
        
        if len(matched_players) == 0:
            st.warning("No player found.")
        else:
            if len(matched_players) == 1:
                player = matched_players[0]
            else:
                options = [f"{p['name']} ({p['teamName']})" for p in matched_players]
                selected_option = st.selectbox("Select Player:", options)
                selected_index = options.index(selected_option)
                player = matched_players[selected_index]

            # --- Tabs ---
            tabs = st.tabs(["Profile", "Batting Stats", "Bowling Stats"])

            # --- Profile Tab ---
            with tabs[0]:
                st.subheader("🧑‍💼 Personal Information")
                st.image(f"https://www.example.com/images/{player['faceImageId']}.jpg", width=150)

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("**Cricket Details**")
                    st.write(f"Role: {player.get('role', 'N/A')}")
                    st.write(f"Batting: {player.get('battingStyle', 'N/A')}")
                    st.write(f"Bowling: {player.get('bowlingStyle', 'N/A')}")
                    st.write(f"International Team: {player.get('internationalTeam', 'N/A')}")
                with col2:
                    st.markdown("**Personal Details**")
                    st.write(f"Date of Birth: {player.get('dob', 'N/A')}")
                    st.write(f"Birth Place: {player.get('birthPlace', 'N/A')}")
                    st.write(f"Height: {player.get('height', 'N/A')}")
                with col3:
                    st.markdown("**Teams Played For**")
                    for team in player.get('teamsPlayedFor', []):
                        st.write(f"- {team}")
                
                # Full profile link
                full_profile_url = "https://www.example.com/full-profile"
                st.markdown(f'🔗 Full Profile: [{full_profile_url}]({full_profile_url})')



            # --- Batting Stats Tab ---
            with tabs[1]:
                st.subheader("🏏 Batting Career Statistics")

                # Section 1: Career Overview
                st.markdown("📊 **Career Overview**")
                col_test, col_odi, col_t20, col_ipl = st.columns(4)

                career_overview = api_data.get("career_overview")
                # {
                #     'Test': {'Matches': 10, 'Runs': 600, 'Average': 40.0, 'Strike Rate': 50.0},
                #     'ODI': {'Matches': 50, 'Runs': 1800, 'Average': 36.0, 'Strike Rate': 75.0},
                #     'T20': {'Matches': 30, 'Runs': 900, 'Average': 30.0, 'Strike Rate': 130.0},
                #     'IPL': {'Matches': 20, 'Runs': 700, 'Average': 35.0, 'Strike Rate': 140.0}
                # }

                for col, fmt in zip([col_test, col_odi, col_t20, col_ipl], ['Test','ODI','T20','IPL']):
                    with col:
                        st.markdown(f"**{fmt}**")
                        stats = career_overview[fmt]
                        for k, v in stats.items():
                            if k in ['Average', 'Strike Rate']:
                                st.write(f"{k}: {v:.2f}")
                            else:
                                st.write(f"{k}: {int(v)}")

                # Separator
                st.markdown("---")

                # Section 2: Detailed Statistics
                st.markdown("📝 **Detailed Statistics**")

                detailed_stats = api_data.get("detailed_stats")
                # pd.DataFrame({
                #     "Statistic": ["Matches", "Innings", "Runs", "Balls", "Highest", "Average", "SR", "Not Out", "50s", "100s"],
                #     "Test": ["10", "18", "600", "1200", "120", "40.00", "50.00", "2", "4", "1"],
                #     "ODI": ["50", "48", "1800", "2400", "110", "36.00", "75.00", "4", "12", "3"],
                #     "T20": ["30", "30", "900", "700", "85", "30.00", "130.00", "0", "5", "0"],
                #     "IPL": ["20", "20", "700", "550", "90", "35.00", "140.00", "1", "4", "1"]
                # })

                st.table(detailed_stats)

            # --- Bowling Stats Tab ---
            with tabs[2]:
                st.subheader("🎯 Bowling Career Statistics")
                bowling_stats = api_data.get("bowling_stats")
                # pd.DataFrame([
                #     {"Match": "Match 1", "Overs": 4, "Runs": 30, "Wickets": 2},
                #     {"Match": "Match 2", "Overs": 4, "Runs": 25, "Wickets": 1}
                # ])
                st.subheader("Bowling Stats")
                st.table(bowling_stats)

