import streamlit as st
import pandas as pd
import os
import json
import concurrent.futures
from functools import lru_cache
from utils.api_calls import perform_api_call

# Cache API responses to avoid redundant calls
@lru_cache(maxsize=128)
def cached_api_call(url, api_key, query_string_str=""):
    """Cached version of API call to avoid duplicate requests"""
    query_string = json.loads(query_string_str) if query_string_str else None
    return perform_api_call(url, api_key, query_string)

def render():
    st.title("Player Search")
    search_name = st.text_input("Enter player name:")
    if search_name:
        player_found, data = load_data(input_txt=search_name)
        if not player_found:
            data = get_data(queries=data, search_name=search_name)
        searched_data(search_name=search_name, input_data=data)

def get_data(queries, search_name):
    player_search = api_queries(
        query_data=queries["search_query"], 
        query_string={"plrN": search_name}, 
        player_search=True
    )
    
    if not player_search or "player" not in player_search:
        return {}
    
    players_list = player_search["player"]
    existing_data = queries["players_data"]
    
    # Filter out players that already exist in our cache
    new_players = [
        player for player in players_list 
        if player.get("name") not in existing_data
    ]
    
    if not new_players:
        # All players already exist in cache, no API calls needed
        return {player.get("name"): existing_data[player.get("name")] for player in players_list}
    
    player_data = {}
    
    # Process only NEW players in parallel (batting + bowling + bio = 3 calls per new player)
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(5, len(new_players) * 3)) as executor:
        futures = []
        for player in new_players:
            player_id = player.get("id")
            player_name = player.get("name")
            
            if player_id and player_name:
                futures.append(
                    executor.submit(
                        process_single_player,
                        queries, player_id, player_name, player
                    )
                )
        
        # Collect results as they complete
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                if result:
                    player_name, player_info = result
                    player_data[player_name] = player_info
            except Exception as e:
                st.error(f"Error processing player data: {e}")
    
    if player_data:
        # Update cache with new players
        existing_data.update(player_data)
        
        # Write to file only once after processing all players
        with open(queries["json_path"], 'w') as file:
            json.dump(existing_data, file, indent=4)
    
    # Return combined data (existing + new)
    combined_data = {}
    for player in players_list:
        player_name = player.get("name")
        if player_name in existing_data:
            combined_data[player_name] = existing_data[player_name]
    
    return combined_data

def process_single_player(queries, player_id, player_name, player_info):
    """Process a single player's data (batting, bowling, bio)"""
    try:
        # Make parallel API calls for this player
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            batting_future = executor.submit(
                api_queries, queries["batting_query"], None, player_id, False
            )
            bowling_future = executor.submit(
                api_queries, queries["bowling_query"], None, player_id, False
            )
            bio_future = executor.submit(
                api_queries, queries["player_bio_query"], None, player_id, False
            )
            
            batting_stats = batting_future.result()
            bowling_stats = bowling_future.result()
            player_bio = bio_future.result()
        
        return player_name, {
            "player_search": player_info,
            "player_batting": batting_stats,
            "player_bowling": bowling_stats,
            "player_stats": player_bio
        }
    except Exception as e:
        st.error(f"Error processing player {player_name}: {e}")
        return None

def load_data(input_txt):
    """Optimized data loader with cached file reads"""
    code_path = os.path.dirname(os.path.abspath(__file__))
    project_data_path = os.path.join(code_path, "..", "project_data")
    players_stats = os.path.join(project_data_path, "player_stats.json")
    api_input_path = os.path.join(project_data_path, "api_Calls_input.json")

    has_data, player_data = load_player_data(search_text=input_txt, players_info=players_stats)
    if has_data:
        return True, player_data
    
    # Load API queries once and reuse
    if not hasattr(load_data, 'api_input_cache'):
        with open(api_input_path) as f:
            load_data.api_input_cache = json.load(f)
    
    queries = {
        "search_query": load_data.api_input_cache["search_player"],
        "batting_query": load_data.api_input_cache["player_batting_stats"],
        "bowling_query": load_data.api_input_cache["player_bowling_stats"],
        "player_bio_query": load_data.api_input_cache["player_stats"],
        "json_path": players_stats,
        "players_data": player_data
    }
    
    return False, queries

def api_queries(query_data, query_string=None, player_id="", player_search=False):
    """Optimized API query function with caching"""
    url = query_data["url"].format(player_id=player_id) if player_id else query_data["url"]
    api_key = query_data["api_key"]
    
    # Convert query_string to string for caching
    query_string_str = json.dumps(query_string, sort_keys=True) if query_string else ""
    
    # Use cached version if available
    return cached_api_call(url, api_key, query_string_str)

def load_player_data(search_text, players_info):
    """Optimized player data loading with file existence check first"""
    if not os.path.exists(players_info):
        os.makedirs(os.path.dirname(players_info), exist_ok=True)
        with open(players_info, "w") as f:
            json.dump({}, f, indent=4)
        return False, {}
    
    try:
        with open(players_info) as f:
            players_data = json.load(f)
        
        if not players_data:
            return False, {}
        
        matched_players = match_keys(input_str=search_text, keys=players_data.keys())
        if matched_players:
            output = {player: players_data[player] for player in matched_players}
            return True, output
        
        return False, players_data
    except (json.JSONDecodeError, IOError):
        return False, {}

def match_keys(input_str, keys):
    """Optimized key matching"""
    if not input_str or not keys:
        return []
    
    input_lower = input_str.lower()
    return [key for key in keys if input_lower in key.lower()]

def searched_data(search_name, input_data):
    """Optimized data display with early returns"""
    if not input_data:
        st.warning("No player found.")
        return
    
    search_lower = search_name.lower()
    matched_players = [
        player_data for player_name, player_data in input_data.items() 
        if search_lower in player_name.lower()
    ]
    
    if not matched_players:
        st.warning("No player found.")
        return
    
    if len(matched_players) == 1:
        player = matched_players[0]
    else:
        options = [f"{p['player_search']['name']} ({p['player_search']['teamName']})" for p in matched_players]
        selected_option = st.selectbox("Select Player:", options)
        player = matched_players[options.index(selected_option)]

    # Display player data
    display_player_data(player)

def display_player_data(player):
    """Optimized player data display with tab management"""
    tabs = st.tabs(["Profile", "Batting Stats", "Bowling Stats"])
    
    # Profile Tab
    with tabs[0]:
        display_profile_tab(player)
    
    # Batting Stats Tab
    with tabs[1]:
        display_batting_tab(player)
    
    # Bowling Stats Tab
    with tabs[2]:
        display_bowling_tab(player)

def display_profile_tab(player):
    """Optimized profile tab display"""
    st.subheader("🧑‍💼 Personal Information")
    player_stats = player.get("player_stats", {})
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Cricket Details**")
        st.write(f"Role: {player_stats.get('role', '-')}")
        st.write(f"Batting: {player_stats.get('bat', '-')}")
        st.write(f"Bowling: {player_stats.get('bowl', '-')}")
        st.write(f"International Team: {player_stats.get('intlTeam', '-')}")
    with col2:
        st.markdown("**Personal Details**")
        st.write(f"Date of Birth: {player_stats.get('DoB', '-')}")
        st.write(f"Birth Place: {player_stats.get('birthPlace', '-')}")
        st.write(f"Height: {player_stats.get('height', '-')}")
    with col3:
        st.markdown("**Teams Played For**")
        teams = player_stats.get("teams", "")
        if teams:
            for team in teams.split(","):
                st.write(f"- {team.strip()}")

    # Full profile link
    app_index = player_stats.get("appIndex", {})
    full_profile_url = app_index.get("webURL", "")
    if full_profile_url:
        st.markdown(f'🔗 Full Profile: [{full_profile_url}]({full_profile_url})')

def display_batting_tab(player):
    """Optimized batting stats display"""
    st.subheader("🏏 Batting Career Statistics")
    batting_stats = player.get("player_batting", {})
    
    if "headers" in batting_stats and "values" in batting_stats:
        headers = batting_stats["headers"][1:]
        values = batting_stats["values"]
        
        row_labels = [row['values'][0] for row in values]
        data_values = [row['values'][1:] for row in values]
        
        detailed_stats = pd.DataFrame(data_values, columns=headers, index=row_labels)
        detailed_stats.columns.name = 'Statistics'
        detailed_stats.index.name = 'Format'
        
        # Summary rows
        summary_rows = ['Matches', 'Runs', 'Average', 'SR']
        summary_df = detailed_stats.loc[summary_rows] if all(row in detailed_stats.index for row in summary_rows) else pd.DataFrame()

        st.markdown("📊 **Career Overview**")
        st.dataframe(summary_df)
        st.markdown("---")
        st.markdown("📝 **Detailed Statistics**")
        st.dataframe(detailed_stats)
    else:
        st.info("No batting statistics available")

def display_bowling_tab(player):
    """Optimized bowling stats display"""
    st.subheader("🎯 Bowling Career Statistics")
    bowling_stats = player.get("player_bowling", {})
    
    if "headers" in bowling_stats and "values" in bowling_stats:
        headers = bowling_stats["headers"][1:]
        values = bowling_stats["values"]
        
        row_labels = [row['values'][0] for row in values]
        data_values = [row['values'][1:] for row in values]
        
        detailed_df = pd.DataFrame(data_values, columns=headers, index=row_labels)
        detailed_df.columns.name = 'Statistics'
        detailed_df.index.name = 'Format'
        
        # Summary rows
        summary_rows = ['Matches', 'Innings', 'Balls', 'Maidens', 'Wickets', 'Eco', 'Avg']
        summary_df = detailed_df.loc[summary_rows] if all(row in detailed_df.index for row in summary_rows) else pd.DataFrame()

        st.markdown("📊 **Career Overview**")
        st.dataframe(summary_df)
        st.markdown("---")
        st.markdown("📝 **Detailed Statistics**")
        st.dataframe(detailed_df)
    else:
        st.info("No bowling statistics available")