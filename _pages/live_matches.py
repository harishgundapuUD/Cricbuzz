import streamlit as st

live_response = {'typeMatches': [{'matchType': 'League', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 9575, 'seriesName': 'Caribbean Premier League 2025', 'matches': [{'matchInfo': {'matchId': 116696, 'seriesId': 9575, 'seriesName': 'Caribbean Premier League 2025', 'matchDesc': '14th Match', 'matchFormat': 'T20', 'startDate': '1756335600000', 'endDate': '1756348200000', 'state': 'Complete', 'status': 'Trinbago Knight Riders won by 8 wkts', 'team1': {'teamId': 1978, 'teamName': 'Antigua and Barbuda Falcons', 'teamSName': 'ABF', 'imageId': 507236}, 'team2': {'teamId': 271, 'teamName': 'Trinbago Knight Riders', 'teamSName': 'TKR', 'imageId': 172325}, 'venueInfo': {'id': 500, 'ground': 'Brian Lara Stadium', 'city': 'Tarouba, Trinidad', 'timezone': '-04:00', 'latitude': '10.295034', 'longitude': '-61.445609'}, 'currBatTeamId': 271, 'seriesStartDt': '1755043200000', 'seriesEndDt': '1758499200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 146, 'wickets': 7, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 152, 'wickets': 2, 'overs': 18.4}}}}]}}]}, {'matchType': 'Domestic', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matches': [{'matchInfo': {'matchId': 123655, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '1st Quarter-Final', 'matchFormat': 'TEST', 'startDate': '1756353600000', 'endDate': '1756638000000', 'state': 'In Progress', 'status': 'Day 1: 1st Session', 'team1': {'teamId': 233, 'teamName': 'North Zone', 'teamSName': 'NZONE', 'imageId': 172286}, 'team2': {'teamId': 235, 'teamName': 'East Zone', 'teamSName': 'EZONE', 'imageId': 172288}, 'venueInfo': {'id': 1438087, 'ground': 'BCCI Centre of Excellence Ground', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '12.978853', 'longitude': '77.599533'}, 'currBatTeamId': 233, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 15, 'overs': 4.6}}}}, {'matchInfo': {'matchId': 123661, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '2nd Quarter-Final', 'matchFormat': 'TEST', 'startDate': '1756353600000', 'endDate': '1756638000000', 'state': 'In Progress', 'status': 'Day 1: 1st Session', 'team1': {'teamId': 237, 'teamName': 'Central Zone', 'teamSName': 'CZONE', 'imageId': 172290}, 'team2': {'teamId': 1146, 'teamName': 'North East Zone', 'teamSName': 'NEZONE', 'imageId': 242496}, 'venueInfo': {'id': 1438102, 'ground': 'BCCI Centre of Excellence Ground B', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '13.174092', 'longitude': '77.706999'}, 'currBatTeamId': 237, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 5, 'wickets': 1, 'overs': 2.6}}}}]}}, {'seriesAdWrapper': {'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matches': [{'matchInfo': {'matchId': 129007, 'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matchDesc': '23rd Match', 'matchFormat': 'ODI', 'startDate': '1756288800000', 'endDate': '1756317600000', 'state': 'Complete', 'status': 'No result', 'team1': {'teamId': 14, 'teamName': 'Kenya', 'teamSName': 'KEN', 'imageId': 172129}, 'team2': {'teamId': 287, 'teamName': 'Papua New Guinea', 'teamSName': 'PNG', 'imageId': 172336}, 'venueInfo': {'id': 1563, 'ground': 'Grainville', 'city': 'St Saviour', 'timezone': '+01:00', 'latitude': '49.1995792', 'longitude': '-2.087867'}, 'seriesStartDt': '1727136000000', 'seriesEndDt': '1769731200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 275, 'wickets': 8, 'overs': 49.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 53, 'wickets': 2, 'overs': 14.3}}}}, {'matchInfo': {'matchId': 129018, 'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matchDesc': '24th Match', 'matchFormat': 'ODI', 'startDate': '1756288800000', 'endDate': '1756317600000', 'state': 'Complete', 'status': 'No result', 'team1': {'teamId': 525, 'teamName': 'Qatar', 'teamSName': 'QAT', 'imageId': 172575}, 'team2': {'teamId': 185, 'teamName': 'Denmark', 'teamSName': 'DEN', 'imageId': 172245}, 'venueInfo': {'id': 1566, 'ground': 'Farmers Cricket Club Ground', 'city': 'St Martin', 'timezone': '+01:00', 'latitude': '49.2184521', 'longitude': '-2.0601565'}, 'seriesStartDt': '1727136000000', 'seriesEndDt': '1769731200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 265, 'wickets': 7, 'overs': 49.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 37, 'wickets': 3, 'overs': 15.6}}}}]}}]}, {'matchType': 'Women', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matches': [{'matchInfo': {'matchId': 131235, 'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matchDesc': '12th Match', 'matchFormat': 'T20', 'startDate': '1756302300000', 'endDate': '1756314900000', 'state': 'Complete', 'status': 'Italy Women need 34 runs in 9 balls', 'team1': {'teamId': 189, 'teamName': 'Ireland Women', 'teamSName': 'IREW', 'imageId': 172249}, 'team2': {'teamId': 1125, 'teamName': 'Italy Women', 'teamSName': 'ITAW', 'imageId': 248417}, 'venueInfo': {'id': 265, 'ground': 'Hazelaarweg', 'city': 'Rotterdam', 'timezone': '+02:00', 'latitude': '51.922829', 'longitude': '4.478450'}, 'currBatTeamId': 189, 'seriesStartDt': '1755561600000', 'seriesEndDt': '1756339200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 175, 'wickets': 6, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 142, 'wickets': 9, 'overs': 18.3}}}}, {'matchInfo': {'matchId': 131229, 'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matchDesc': '11th Match', 'matchFormat': 'T20', 'startDate': '1756285200000', 'endDate': '1756297800000', 'state': 'Complete', 'status': 'Netherlands Women won by 65 runs', 'team1': {'teamId': 188, 'teamName': 'Netherlands Women', 'teamSName': 'NEDW', 'imageId': 172248}, 'team2': {'teamId': 504, 'teamName': 'Germany Women', 'teamSName': 'GERW', 'imageId': 172553}, 'venueInfo': {'id': 265, 'ground': 'Hazelaarweg', 'city': 'Rotterdam', 'timezone': '+02:00', 'latitude': '51.922829', 'longitude': '4.478450'}, 'currBatTeamId': 188, 'seriesStartDt': '1755561600000', 'seriesEndDt': '1756339200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 175, 'wickets': 4, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 110, 'wickets': 1, 'overs': 19.6}}}}]}}]}], 'filters': {'matchType': ['International', 'League', 'Domestic', 'Women']}, 'appIndex': {'seoTitle': 'Live Cricket Score - Scorecard and Match Results', 'webURL': 'www.cricbuzz.com/live-cricket-scores/'}, 'responseLastUpdated': '1756358017'}

def render():
    update_page(response=live_response)

def extract_scorecards(data):
    scorecards = []
    seen_match_ids = set()  # Avoid duplicates if needed

    for type_match in data.get("typeMatches", []):
        for series in type_match.get("seriesMatches", []):
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for match in matches:
                info = match.get("matchInfo", {})
                match_id = info.get("matchId")

                if match_id in seen_match_ids:
                    continue
                seen_match_ids.add(match_id)

                score = match.get("matchScore", {})

                team1 = info.get("team1", {})
                team2 = info.get("team2", {})

                team1_name = team1.get("teamName", "Team A")
                team2_name = team2.get("teamName", "Team B")
                match_format = info.get("matchFormat", "Unknown")

                team1_score_data = score.get("team1Score", {}).get("inngs1", {})
                team2_score_data = score.get("team2Score", {}).get("inngs1", {})

                team1_runs = team1_score_data.get("runs", "-")
                team1_wkts = team1_score_data.get("wickets", "-")
                team1_overs = team1_score_data.get("overs", "-")

                team2_runs = team2_score_data.get("runs", "-")
                team2_wkts = team2_score_data.get("wickets", "-")
                team2_overs = team2_score_data.get("overs", "-")

                state = info.get("state", "Unknown")
                result = info.get("status", "No status")
                match_status = result if state == "Complete" else "In Progress"

                scorecards.append({
                    "team1": team1_name,
                    "team2": team2_name,
                    "match_format": match_format,
                    "team1_score": f"{team1_runs}/{team1_wkts} ({team1_overs})",
                    "team2_score": f"{team2_runs}/{team2_wkts} ({team2_overs})",
                    "status": match_status
                })

    return scorecards

def render_match_card(match):
    team1 = match['team1']
    team2 = match['team2']
    match_format = match['match_format']
    status = match['status'].lower()

    # Status color logic
    if "won" in status:
        if team1.lower() in status:
            status_color = "#28a745"  # Green
        elif team2.lower() in status:
            status_color = "#007bff"  # Blue
        else:
            status_color = "#3366cc"
    elif "no result" in status or "abandoned" in status:
        status_color = "#dc3545"  # Red
    elif "progress" in status or "day" in status:
        status_color = "#ff8800"  # Orange
    else:
        status_color = "#6c757d"  # Gray fallback

    return f"""
        <div style="
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 5px;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            height: 270px;
        ">
            <div>
                <h3 style="margin: 0 0 5px 0; font-weight: 700; font-size: 20px;">
                    {team1} vs {team2}
                </h3>
                <div style="
                    background-color: #f0f0f0;
                    padding: 4px 8px;
                    border-radius: 5px;
                    display: inline-block;
                    font-size: 15px;
                    font-weight: 600;
                    color: #222;
                    margin-bottom: 10px;
                ">
                    {match_format.upper()} Match
                </div>
                <p style="margin: 5px 0;"><strong>{team1}:</strong> {match['team1_score']}</p>
                <p style="margin: 5px 0;"><strong>{team2}:</strong> {match['team2_score']}</p>
            </div>
            <div style="
                margin-top: auto;
                padding: 8px;
                background-color: {status_color};
                color: white;
                font-weight: 600;
                font-size: 16px;
                text-align: center;
                border-radius: 0 0 10px 10px;
            ">
                {match['status']}
            </div>
        </div>
    """

def update_page(response):
# Streamlit UI
    st.set_page_config(page_title="Live Cricket Scores", layout="wide")
    st.title("🏏 Live Cricket Scorecards")
    # st.markdown("---")

    scorecards = extract_scorecards(data=response)

    if not scorecards:
        st.warning("No matches found.")
    else:
        for i in range(0, len(scorecards), 2):
            cols = st.columns(2)

            # First match
            with cols[0]:
                st.markdown(render_match_card(scorecards[i]), unsafe_allow_html=True)

            # Second match (only if it exists)
            if i + 1 < len(scorecards):
                with cols[1]:
                    st.markdown(render_match_card(scorecards[i + 1]), unsafe_allow_html=True)
