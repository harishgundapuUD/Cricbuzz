import json
from db_connection import SQLQuery

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


# creating the db
db_connection = SQLQuery()
db_connection.get_connection()
db_connection.create_db()
db_connection.create_tables()
print(json.load(open(r"C:\Users\haris\OneDrive\Desktop\Guvi\Live class codes\Projects\project_data\player_stats.json")))
player_data = extract_player_data_total(json.load(open(r"C:\Users\haris\OneDrive\Desktop\Guvi\Live class codes\Projects\project_data\player_stats.json")))
for player in player_data:
    db_connection.add_user(input_data=player)
    print(f"added player: {player}")
    print("\n")
