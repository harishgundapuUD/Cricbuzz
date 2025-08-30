import streamlit as st
import pandas as pd
import os
import json
from utils.api_calls import perform_api_call

def render():
    st.title("Player Search")
    search_name = st.text_input("Enter player name:")
    queries = None
    if search_name:
        player_found, data = load_data(input_txt=search_name)
        if not player_found:
            queries = data
            data = get_data(queries=queries, search_name=search_name)
        searched_data(search_name=search_name, input_data=data)

def get_data(queries, search_name):
    player_data = {}
    player_search = api_queries(query_data=queries.get("search_query"), query_string={"plrN":search_name}, player_search=True)
    print(f"the api query is: {player_search}")
    if player_search:
        for player in player_search.get("player"):
            player_id = player.get("id")
            player_name = player.get("name")
            
            player_data[player_name] = {"player_search": player}
            
            batting_stats = api_queries(query_data=queries.get("batting_query"),player_id=player_id)
            player_data[player_name]["player_batting"] = batting_stats
            
            bowling_stats = api_queries(query_data=queries.get("bowling_query"), player_id=player_id)
            player_data[player_name]["player_bowling"] = bowling_stats
            
            player_bio = api_queries(query_data=queries.get("player_bio_query"), player_id=player_id)
            player_data[player_name]["player_stats"] = player_bio
        
        existing_data = queries.get("players_data")
        existing_data.update(player_data)
        
        with open(queries.get("json_path"), 'w') as file:
            json.dump(existing_data, file, indent=4)

        return player_data

def load_data(input_txt):
    """Main data loader"""
    code_path = os.path.dirname(os.path.abspath(__file__))
    project_data_path = os.path.join(code_path, "..", "project_data")
    players_stats = os.path.join(project_data_path, "player_stats.json")
    api_input_path = os.path.join(project_data_path, "api_Calls_input.json")

    has_data, player_data = load_player_data(search_text=input_txt, players_info=players_stats)
    if has_data:
        return True, player_data
    search_query = json.load(open(api_input_path))["search_player"]
    batting_query = json.load(open(api_input_path))["player_batting_stats"]
    bowling_query = json.load(open(api_input_path))["player_bowling_stats"]
    player_bio = json.load(open(api_input_path))["player_stats"]

    queries = {
                    "search_query": search_query,
                    "batting_query": batting_query,
                    "bowling_query": bowling_query,
                    "player_bio_query": player_bio,
                    "json_path": players_stats,
                    "players_data": player_data
              }
    
    return False, queries

def api_queries(query_data, query_string=None, player_id="", player_search=False):
    if player_id:
        url = query_data.get("url").format(player_id=player_id)
    else:
        url = query_data.get("url")
    print(f"the query string is: {query_string}")
    if player_search and query_string:
        search_player = perform_api_call(url, query_data["api_key"], query_string)
    elif not player_search:
        search_player = perform_api_call(url, query_data["api_key"], query_string)
    print(search_player)
    return search_player

def load_player_data(search_text, players_info):
    if os.path.exists(players_info):
        players_info = json.load(open(players_info))
        matched_players = match_keys(input_str=search_text, keys=players_info.keys())
        if matched_players:
            output = {}
            for player in matched_players:
                print(f"load player: {player}")
                print(players_info.get(player))
                print("\n")
                output[player] = players_info.get(player)
            return True, output
        return False, players_info
    else:
        if not os.path.exists(players_info):
            os.makedirs(os.path.dirname(players_info), exist_ok=True)
            with open(players_info, "w") as f:
                json.dump({}, f, indent=4) 
        return False, {}

def match_keys(input_str, keys):
    input_str = input_str.lower()
    return [key for key in keys if input_str in key.lower()]

def searched_data(search_name, input_data):
    if search_name:
        matched_players = []
        # print(input_data)
        for player in input_data.keys():
            print(player)
            if search_name.lower() in player.lower():
                matched_players.append(input_data[player])
        print(matched_players)
        if len(matched_players) == 0:
            st.warning("No player found.")
        else:
            if len(matched_players) == 1:
                player = matched_players[0]
            else:
                options = [f"{p["player_search"]['name']} ({p["player_search"]['teamName']})" for p in matched_players]
                selected_option = st.selectbox("Select Player:", options)
                selected_index = options.index(selected_option)
                player = matched_players[selected_index]

            # --- Tabs ---
            tabs = st.tabs(["Profile", "Batting Stats", "Bowling Stats"])
            print(player)

            # --- Profile Tab ---
            with tabs[0]:
                st.subheader("🧑‍💼 Personal Information")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown("**Cricket Details**")
                    st.write(f"Role: {player.get("player_stats").get('role', '-')}")
                    st.write(f"Batting: {player.get("player_stats").get('bat', '-')}")
                    st.write(f"Bowling: {player.get("player_stats").get('bowl', '-')}")
                    st.write(f"International Team: {player.get("player_stats").get('intlTeam', '-')}")
                with col2:
                    st.markdown("**Personal Details**")
                    st.write(f"Date of Birth: {player.get("player_stats").get('DoB', '-')}")
                    st.write(f"Birth Place: {player.get("player_stats").get('birthPlace', '-')}")
                    st.write(f"Height: {player.get("player_stats").get('height', '-')}")
                with col3:
                    st.markdown("**Teams Played For**")
                    player_stats = player.get("player_stats")
                    for team in player_stats.get("teams").split(","):
                        st.write(f"- {team}")

                
                # Full profile link
                full_profile_url = player_stats.get("appIndex").get("webURL")
                st.markdown(f'🔗 Full Profile: [{full_profile_url}]({full_profile_url})')

            # --- Batting Stats Tab ---
            with tabs[1]:
                st.subheader("🏏 Batting Career Statistics")

                batting_stats = player.get("player_batting")
                
                summary_df = pd.DataFrame({})
                detailed_stats = pd.DataFrame({})

                # Extract headers and values
                if "headers" in batting_stats and "values" in batting_stats:
                    keys = batting_stats.get("headers")[1:]
                    values = batting_stats.get("values")
                    row_labels = [row['values'][0] for row in values]  # Get row labels like 'Matches', 'Innings', etc.
                    values = [row['values'][1:] for row in values]  # Get the data for each category (Test, ODI, etc.)

                    # Create DataFrame for detailed statistics (dict_two equivalent)
                    detailed_stats = pd.DataFrame(values, columns=keys, index=row_labels)

                    # Create DataFrame for summary statistics (dict_one equivalent)
                    # Select only specific rows for summary statistics: Matches, Runs, Average, Strike Rate
                    summary_rows = ['Matches', 'Runs', 'Average', 'SR']
                    summary_df = detailed_stats.loc[summary_rows]

                    # Add column and row names
                    detailed_stats.columns.name = 'Statistics'
                    detailed_stats.index.name = 'Format'

                    summary_df.columns.name = 'Statistics'
                    summary_df.index.name = 'Format'

                # Section 1: Career Overview
                st.markdown("📊 **Career Overview**")
                st.dataframe(summary_df)
                
                # Separator
                st.markdown("---")

                # Section 2: Detailed Statistics
                st.markdown("📝 **Detailed Statistics**")
                st.dataframe(detailed_stats)

            # --- Bowling Stats Tab ---
            with tabs[2]:
                st.subheader("🎯 Bowling Career Statistics")

                bowling_stats = player.get("player_bowling")

                summary_df = pd.DataFrame({})
                detailed_df = pd.DataFrame({})

                if "headers" in bowling_stats and "values" in bowling_stats:
                    keys = bowling_stats.get("headers")[1:]
                    values = bowling_stats.get("values")

                    # Extract headers and values
                    row_labels = [row['values'][0] for row in values]  # Get row labels like 'Matches', 'Innings', etc.
                    values = [row['values'][1:] for row in values]  # Get the data for each category (Test, ODI, etc.)

                    # Create DataFrame for detailed statistics (dict_two equivalent)
                    detailed_df = pd.DataFrame(values, columns=keys, index=row_labels)

                    # Create DataFrame for summary statistics (dict_one equivalent)
                    # Select only specific rows for summary statistics: Matches, Innings, Balls, Maidens, Wickets, Eco, Avg
                    summary_rows = ['Matches', 'Innings', 'Balls', 'Maidens', 'Wickets', 'Eco', 'Avg']
                    summary_df = detailed_df.loc[summary_rows]

                    # Add column and row names
                    detailed_df.columns.name = 'Statistics'
                    detailed_df.index.name = 'Format'

                    summary_df.columns.name = 'Statistics'
                    summary_df.index.name = 'Format'
                
                # Section 1: Career Overview
                st.markdown("📊 **Career Overview**")
                st.dataframe(summary_df)
                
                # Separator
                st.markdown("---")

                # Section 2: Detailed Statistics
                st.markdown("📝 **Detailed Statistics**")
                st.dataframe(detailed_df)
