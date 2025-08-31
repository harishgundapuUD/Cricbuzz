import os
import json
from db_connection import SQLQuery
from api_calls import perform_api_call

def extract_player_data_total(player_dict):
    extracted_data = []
    
    for player_name, player_info in player_dict.items():
        print(player_name)
        # Extract player_id from player_search
        player_id = player_info["player_search"]["id"]
        
        # Extract batting data from player_batting
        batting_headers = player_info["player_batting"]["headers"]
        batting_values = player_info["player_batting"]["values"]
        
        # Initialize totals
        total_matches = 0
        total_innings = 0
        total_runs = 0
        
        # Get the format indices from headers (skip "ROWHEADER" which is index 0)
        format_indices = range(1, len(batting_headers))
        
        # Calculate totals across all formats
        for i in format_indices:
            try:
                # Convert string values to integers before adding
                matches_str = batting_values[0]["values"][i]    # Matches row
                innings_str = batting_values[1]["values"][i]    # Innings row
                runs_str = batting_values[2]["values"][i]       # Runs row
                
                # Convert to integers (handle empty strings and non-numeric values)
                matches = int(matches_str) if matches_str.isdigit() else 0
                innings = int(innings_str) if innings_str.isdigit() else 0
                runs = int(runs_str) if runs_str.isdigit() else 0
                
                total_matches += matches
                total_innings += innings
                total_runs += runs
                
            except (ValueError, IndexError, AttributeError):
                # Handle cases where values might not be valid
                continue
        
        # Calculate average (runs per innings, avoid division by zero)
        if total_innings > 0:
            average = round(total_runs / total_innings, 2)
        else:
            average = 0.0
        
        # Create data entry
        player_data = {
            "player_id": player_id,
            "name": player_name.strip(),  # Remove any extra spaces
            "matches": str(total_matches),
            "innings": str(total_innings),
            "runs": str(total_runs),
            "average": str(average)
        }
        
        extracted_data.append(player_data)
    
    return extracted_data

def create_and_update_players_data(table):
    db_connection.create_tables(table=table)
    # print(json.load(open(r"C:\Users\haris\OneDrive\Desktop\Guvi\Live class codes\Projects\project_data\player_stats.json")))
    player_data = extract_player_data_total(json.load(open(r"C:\Users\haris\OneDrive\Desktop\Guvi\Live class codes\Projects\project_data\player_stats.json")))
    for player in player_data:
        db_connection.add_user(input_data=player)
        # print(f"added player: {player}")
        # print("\n")

import json

def extract_player_info(json_string):
    """
    Extract player information with properly formatted roles.
    """
    data = json_string
    players_info = []
    current_role = "Unknown"
    
    for player in data["player"]:
        # If this is a role header (no ID), update current role
        if "id" not in player:
            role_name = player.get("name", "").strip()
            current_role = role_name.title() if role_name else "Unknown"
            continue
        
        # If this is a player with ID, extract their info
        players_info.append({
            "id": int(player.get("id")),
            "name": player.get("name"),
            "role": current_role,
            "batting_style": player.get("battingStyle"),
            "bowling_style": player.get("bowlingStyle")
        })
    
    return players_info

def create_and_update_indian_players(table):
    api_data = api_config_data.get("indian_players")
    local_path = os.path.join(configs_path, "indian_players.json")
    json_data = None
    if os.path.exists(local_path):
        json_data = json.load(open(local_path))
        if json_data:
            players = extract_player_info(json_string=json_data)
            print("inside the json reading part")
            for player in players:
                db_connection.create_tables(table=table)
                db_connection.add_indian_user(input_data=player)
                print(f"added player: {player}")
                print("\n")
    if not os.path.exists(local_path) or not json_data:
        json_data = perform_api_call(url=api_data.get("url"), api_key=api_data.get("api_key"))
        with open(local_path, "w") as indian_players:
            json.dump(json_data, indian_players, indent=4)
        
        players = extract_player_info(json_string=json_data)
        for player in players:
            db_connection.create_tables(table=table)
            db_connection.add_indian_user(input_data=player)
            print(f"added player: {player}")
            print("\n")

configs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "project_data")
db_config_data = json.load(open(os.path.join(configs_path, "db_config.json")))
api_config_data = json.load(open(os.path.join(configs_path, "api_calls_input.json")))

# creating the db
db_connection = SQLQuery()
db_connection.get_connection()
db_connection.create_db()
# create_and_update_players_data(table=db_config_data.get("players_table"))
# create_and_update_indian_players(table=db_config_data.get("indian_players_table"))
