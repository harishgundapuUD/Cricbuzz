# import streamlit as st
# import pandas as pd
# from utils.api_calls import perform_api_call
# import json
# import os
# import time
# from concurrent.futures import ThreadPoolExecutor

# def render():
#     live_response, scorecards_data = load_data()
#     update_page(live_response=live_response, scorecard_data=scorecards_data)

# @st.cache_data(ttl=300)  # cache for 5 mins
# def load_data():
#     return preprocessing()

# def preprocessing():
#     code_path = os.path.dirname(os.path.abspath(__file__))
#     project_data_path = os.path.join(code_path, "..", "project_data")
#     live_json_path = os.path.join(project_data_path, "live_matches.json")
#     score_json_path = os.path.join(project_data_path, "score_card.json")
#     api_input_path = os.path.join(project_data_path, "api_Calls_input.json")

#     def is_file_expired(file_path, max_age_seconds=300):
#         if not os.path.exists(file_path):
#             return True
#         return (time.time() - os.path.getmtime(file_path)) > max_age_seconds

#     # ------------------- Load or Fetch Live Matches -------------------
#     if not is_file_expired(live_json_path):
#         with open(live_json_path, "r") as f:
#             live_response = json.load(f)
#     else:
#         query_data = json.load(open(api_input_path)).get("live_matches")
#         query_strings = query_data.get("query_strings")
#         live_response = perform_api_call(
#             url=query_data.get("url"),
#             api_key=query_data.get("api_key"),
#             query_strings=query_strings if query_strings else None
#         )
#         with open(live_json_path, "w") as f:
#             json.dump(live_response, f, indent=4)

#     # ------------------- Load or Fetch Scorecards -------------------
#     if not is_file_expired(score_json_path):
#         with open(score_json_path, "r") as f:
#             scorecards_data = json.load(f)
#     else:
#         query_data = json.load(open(api_input_path)).get("score_card")
#         query_strings = query_data.get("query_strings")
#         output = get_score_card_urls(url_template=query_data.get("url"), live_response=live_response)

#         # Parallel API calls for scorecards
#         def fetch_scorecard(match_id_url):
#             match_id, url = match_id_url
#             return match_id, score_cards(url=url, api_key=query_data.get("api_key"))

#         with ThreadPoolExecutor(max_workers=5) as executor:
#             results = executor.map(fetch_scorecard, output.items())

#         scorecards_data = {match_id: data for match_id, data in results}

#         with open(score_json_path, "w") as f:
#             json.dump(scorecards_data, f, indent=4)

#     return live_response, scorecards_data

# def is_file_expired(file_path, max_age_seconds=300):  # 5 minutes = 300 seconds
#         if not os.path.exists(file_path):
#             return True
#         mod_time = os.path.getmtime(file_path)
#         return (time.time() - mod_time) > max_age_seconds

# def get_score_card_urls(url_template, live_response):
#     # Extract all matchIds from live_response
#     match_ids = []

#     for match_type in live_response.get('typeMatches'):
#         if match_type:
#             for series_wrapper in match_type.get('seriesMatches'):
#                 if series_wrapper:
#                     series = series_wrapper.get('seriesAdWrapper')
#                     if series:
#                         for match in series['matches']:
#                             match_id = match['matchInfo']['matchId']
#                             match_ids.append(match_id)
#     # Generate URLs
#     urls = {mid: url_template.format(match_id=mid) for mid in match_ids}
#     return urls

# def score_cards(url, api_key, query_strings=None):
#     output = perform_api_call(url=url, api_key=api_key, query_strings=query_strings)
#     return output

# def extract_scorecards(data):
#     scorecards = []
#     for type_match in data.get("typeMatches", []):
#         for series in type_match.get("seriesMatches", []):
#             matches = series.get("seriesAdWrapper", {}).get("matches", [])
#             for match in matches:
#                 info = match.get("matchInfo", {})
#                 score = match.get("matchScore", {})
#                 venue = info.get("venueInfo", {})
#                 ground = venue.get("ground", "Unknown Ground")
#                 city = venue.get("city", "Unknown City")

#                 team1 = info.get("team1", {})
#                 team2 = info.get("team2", {})

#                 team1_score = score.get("team1Score", {}).get("inngs1", {})
#                 team2_score = score.get("team2Score", {}).get("inngs1", {})

#                 state = info.get("state", "Unknown")
#                 result = info.get("status", "No status")
#                 match_status = result if state == "Complete" else "In Progress"

#                 scorecards.append({
#                     "match_id": info.get("matchId"),
#                     "team1": team1.get("teamName", "Team A"),
#                     "team2": team2.get("teamName", "Team B"),
#                     "match_format": info.get("matchFormat", "Unknown"),
#                     "venue": f"{ground}, {city}",
#                     "team1_score": f"{team1_score.get('runs', '-')}/{team1_score.get('wickets', '-')}"
#                                     f" ({team1_score.get('overs', '-')})",
#                     "team2_score": f"{team2_score.get('runs', '-')}/{team2_score.get('wickets', '-')}"
#                                     f" ({team2_score.get('overs', '-')})",
#                     "status": match_status
#                 })
#     return scorecards

# def render_match_card(match):
#     team1 = match['team1']
#     team2 = match['team2']
#     match_format = match['match_format']
#     series_name = match.get('series_name', "Unknown Series")
#     venue = match['venue']
#     status = match['status']
#     status_lower = status.lower()

#     # Status color logic
#     if "won" in status_lower:
#         if team1.lower() in status_lower:
#             status_color = "#28a745"
#         elif team2.lower() in status_lower:
#             status_color = "#007bff"
#         else:
#             status_color = "#3366cc"
#     elif "no result" in status_lower or "abandoned" in status_lower:
#         status_color = "#dc3545"
#     elif "progress" in status_lower or "day" in status_lower:
#         status_color = "#ff8800"
#     else:
#         status_color = "#6c757d"

#     # Build card using Streamlit containers
#     with st.container(border=True):   # ✅ Streamlit 1.31+ supports border
#         st.markdown(f"### {team1} vs {team2}")
#         st.markdown(f"###### Series: {series_name}")
#         st.markdown(f"{match_format.upper()} • 📍 {venue}")
#         # st.caption(f"{match_format.upper()} • 📍 {venue}")
#         st.write(f"**{team1}:** {match['team1_score']}")
#         st.write(f"**{team2}:** {match['team2_score']}")

#         # Button (this will stay inside because it's inside the same container)
#         btn_clicked = st.button("📊 View Scorecard", key=f"btn_{match['match_id']}")

#         # Status bar
#         st.markdown(
#             f"""
#             <div style="margin-top:10px; padding:8px;
#                         background:{status_color}; color:white;
#                         font-weight:600; text-align:center;
#                         border-radius:6px;">
#                 {status}
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

#         if btn_clicked:
#             return match
#     return None

# def render_detailed_scorecard(scorecard_data):
#     st.header("📊 Detailed Scorecard")
#     st.markdown(
#     "<hr style='border: 3px solid #000; margin: 10px 0;'>",
#     unsafe_allow_html=True
# )

#     if not scorecard_data or "scorecard" not in scorecard_data:
#         st.warning("⚠️ Scorecard data not available")
#         return

#     # Single scrollable container
#     with st.container():
#         # st.markdown(
#         #     "<div style='max-height:700px; overflow-y:auto; padding:10px; border:1px solid #ccc; border-radius:10px;'>",
#         #     unsafe_allow_html=True
#         # )

#         for innings in scorecard_data["scorecard"]:
#             team_name = innings.get("batteamname", f"Innings {innings.get('inningsid')}")
#             st.subheader(f"🏏 {team_name} Innings")

#             # Batting
#             batsmen = innings.get("batsman", [])
#             if batsmen:
#                 st.markdown("### Batting")
#                 df_bat = pd.DataFrame(batsmen)[
#                     ["name", "runs", "balls", "fours", "sixes", "strkrate", "outdec"]
#                 ]
#                 df_bat.columns = ["Batsman", "Runs", "Balls", "4s", "6s", "Strike Rate", "Status"]
#                 st.dataframe(df_bat, use_container_width=True, height=200)

#             # Bowling
#             bowlers = innings.get("bowler", [])
#             if bowlers:
#                 st.markdown("### Bowling")
#                 df_bowl = pd.DataFrame(bowlers)[
#                     ["name", "overs", "maidens", "runs", "wickets", "economy"]
#                 ]
#                 df_bowl.columns = ["Bowler", "Overs", "Maiden", "Runs", "Wickets", "Economy"]
#                 st.dataframe(df_bowl, use_container_width=True, height=200)

#             # Fall of Wickets
#             fow = innings.get("fow", {}).get("fow", [])
#             if fow:
#                 st.markdown("### Fall of Wickets")
#                 fow_df = pd.DataFrame(fow)[["batsmanname", "runs", "overnbr"]]
#                 fow_df.columns = ["Batsman Out", "Score", "Over"]
#                 st.dataframe(fow_df, use_container_width=True, height=150)

#             # Partnerships
#             partnerships = innings.get("partnership", {}).get("partnership", [])
#             if partnerships:
#                 st.markdown("### Partnerships")
#                 part_df = pd.DataFrame(partnerships)[
#                     ["bat1name", "bat1runs", "bat2name", "bat2runs", "totalruns", "totalballs"]
#                 ]
#                 part_df.columns = ["Batsman 1", "Runs (B1)", "Batsman 2", "Runs (B2)", "Total Runs", "Balls Faced"]
#                 st.dataframe(part_df, use_container_width=True, height=150)

#             # Powerplays
#             powerplays = innings.get("pp", {}).get("powerplay", [])
#             # Remove empty dicts
#             powerplays = [pp for pp in powerplays if pp]
#             if powerplays:
#                 st.markdown("### Powerplays")
#                 pp_df = pd.DataFrame(powerplays)
#                 if "pptype" in pp_df.columns:
#                     pp_df["pptype"] = pp_df["pptype"].str.title()
#                 pp_df = pp_df[["pptype", "ovrfrom", "ovrto", "run", "wickets"]]
#                 pp_df.columns = ["Type", "From", "To", "Runs", "Wkts"]
#                 st.dataframe(pp_df, use_container_width=True, height=150)

#             # Extras
#             extras = innings.get("extras", {})
#             if extras:
#                 st.markdown(
#                     f"**Extras:** {extras.get('total',0)} "
#                     f"(b {extras.get('byes',0)}, lb {extras.get('legbyes',0)}, "
#                     f"w {extras.get('wides',0)}, nb {extras.get('noballs',0)}, p {extras.get('penalty',0)})"
#                 )

#             # Final Total
#             st.markdown(
#                 f"**Total:** {innings.get('score','-')}/{innings.get('wickets','-')} "
#                 f"({innings.get('overs','-')} overs, RR: {innings.get('runrate','-')})"
#             )

#             st.markdown(
#                             "<hr style='border: 2px solid #000; margin: 10px 0;'>",
#                             unsafe_allow_html=True
#                         )  # separator between innings

#         st.markdown("</div>", unsafe_allow_html=True)

# def update_page(live_response, scorecard_data):
#     st.set_page_config(page_title="Live Cricket Scores", layout="wide")
#     st.title("🏏 Live Cricket Scorecards")
#     scorecards = extract_scorecards(live_response)

#     clicked_match = None

#     if not scorecards:
#         st.warning("No matches found.")
#     else:
#         # Display cards in rows of 2
#         for i in range(0, len(scorecards), 2):
#             cols = st.columns(2)

#             for j, col in enumerate(cols):
#                 series_name = ""
#                 if i + j < len(scorecards):
#                     match = scorecards[i + j]
#                     with col:
#                         for match_type in live_response.get('typeMatches'):
#                             if match_type:
#                                 for series_match in match_type.get('seriesMatches'):
#                                     if series_match and series_match.get('seriesAdWrapper'):
#                                         for m in series_match.get('seriesAdWrapper').get('matches'):
#                                             if m:
#                                                 if m.get('matchInfo').get('matchId') == match.get("match_id"):
#                                                     series_name = m['matchInfo']['seriesName']
#                                                     break
#                         match.update({"series_name":series_name})
#                         selected = render_match_card(match)
#                         if selected:
#                             clicked_match = selected
#                             # Show detailed view if clicked
#                             if clicked_match:
#                                 st.markdown("---")
#                                 # print(match)
#                                 # print(scorecard_data)
#                                 render_detailed_scorecard(scorecard_data.get(match.get("match_id")))






import streamlit as st
import pandas as pd
from utils.api_calls import perform_api_call
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor


def render():
    live_response, scorecards_data = load_data()
    update_page(live_response=live_response, scorecard_data=scorecards_data)


# -------------------- Utility --------------------

def is_file_expired(file_path, max_age_seconds=300):
    """Check if file is older than `max_age_seconds`"""
    if not os.path.exists(file_path):
        return True
    return (time.time() - os.path.getmtime(file_path)) > max_age_seconds


# -------------------- Cached Loaders --------------------

@st.cache_data(ttl=300)
def load_live_response(api_input_path, live_json_path):
    reloaded = False
    """Load live matches (from cache or API)"""
    if not is_file_expired(live_json_path):
        return reloaded, json.load(open(live_json_path))
    
    query_data = json.load(open(api_input_path))["live_matches"]
    live_response = perform_api_call(
        query_data["url"], query_data["api_key"], query_data.get("query_strings")
    )
    if live_response.json():
        json.dump(live_response, open(live_json_path, "w"), indent=4)
        reloaded = True
    return reloaded, live_response


@st.cache_data(ttl=300)
def load_scorecards(api_input_path, score_json_path, live_response, reloaded=False):
    """Load scorecards (from cache or API, with parallel calls)"""
    if not is_file_expired(score_json_path) or not reloaded:
        return json.load(open(score_json_path))

    query_data = json.load(open(api_input_path))["score_card"]
    urls = get_score_card_urls(query_data["url"], live_response)

    def fetch_scorecard(mid_url):
        mid, url = mid_url
        return mid, score_cards(url=url, api_key=query_data["api_key"])

    max_workers = min(32, (os.cpu_count() or 1) + 4)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = dict(executor.map(fetch_scorecard, urls.items()))

    json.dump(results, open(score_json_path, "w"), indent=4)
    return results


def load_data():
    """Main data loader"""
    code_path = os.path.dirname(os.path.abspath(__file__))
    project_data_path = os.path.join(code_path, "..", "project_data")

    live_json_path = os.path.join(project_data_path, "live_matches.json")
    score_json_path = os.path.join(project_data_path, "score_card.json")
    api_input_path = os.path.join(project_data_path, "api_Calls_input.json")

    reloaded, live_response = load_live_response(api_input_path, live_json_path)
    scorecards_data = load_scorecards(api_input_path, score_json_path, live_response, reloaded=reloaded)
    return live_response, scorecards_data


# -------------------- API Helpers --------------------

def get_score_card_urls(url_template, live_response):
    """Extract match IDs and generate scorecard URLs"""
    match_ids = []
    for match_type in live_response.get('typeMatches', []):
        for series_wrapper in match_type.get('seriesMatches', []):
            series = series_wrapper.get('seriesAdWrapper', {})
            for match in series.get('matches', []):
                match_id = match['matchInfo']['matchId']
                match_ids.append(match_id)
    return {mid: url_template.format(match_id=mid) for mid in match_ids}


def score_cards(url, api_key, query_strings=None):
    return perform_api_call(url=url, api_key=api_key, query_strings=query_strings)


# -------------------- Data Extraction --------------------

def extract_scorecards(data):
    """Extract simplified scorecard info for match cards"""
    scorecards = []
    for type_match in data.get("typeMatches", []):
        for series in type_match.get("seriesMatches", []):
            series_name = series.get("seriesAdWrapper", {}).get("seriesName", "Unknown Series")
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for match in matches:
                info = match.get("matchInfo", {})
                score = match.get("matchScore", {})
                venue = info.get("venueInfo", {})

                team1_score = score.get("team1Score", {}).get("inngs1", {})
                team2_score = score.get("team2Score", {}).get("inngs1", {})

                scorecards.append({
                    "match_id": str(info.get("matchId")),
                    "series_name": series_name,
                    "team1": info.get("team1", {}).get("teamName", "Team A"),
                    "team2": info.get("team2", {}).get("teamName", "Team B"),
                    "match_format": info.get("matchFormat", "Unknown"),
                    "venue": f"{venue.get('ground','?')}, {venue.get('city','?')}",
                    "team1_score": f"{team1_score.get('runs','-')}/{team1_score.get('wickets','-')} ({team1_score.get('overs','-')})",
                    "team2_score": f"{team2_score.get('runs','-')}/{team2_score.get('wickets','-')} ({team2_score.get('overs','-')})",
                    "status": info.get("status", "No status"),
                })
    return scorecards


# -------------------- UI Rendering --------------------

def render_match_card(match):
    """Render a match card with button + status"""
    team1 = match['team1']
    team2 = match['team2']
    match_format = match['match_format']
    venue = match['venue']
    status = match['status']
    status_lower = status.lower()

    # Status color logic
    if "won" in status_lower:
        if team1.lower() in status_lower:
            status_color = "#28a745"
        elif team2.lower() in status_lower:
            status_color = "#007bff"
        else:
            status_color = "#3366cc"
    elif "no result" in status_lower or "abandoned" in status_lower:
        status_color = "#dc3545"
    elif "progress" in status_lower or "day" in status_lower:
        status_color = "#ff8800"
    else:
        status_color = "#6c757d"

    with st.container(border=True):
        st.markdown(f"### {team1} vs {team2}")
        st.markdown(f"###### Series: {match['series_name']}")
        st.markdown(f"{match_format.upper()} • 📍 {venue}")
        st.write(f"**{team1}:** {match['team1_score']}")
        st.write(f"**{team2}:** {match['team2_score']}")

        btn_clicked = st.button("📊 View Scorecard", key=f"btn_{match['match_id']}")

        st.markdown(
            f"""
            <div style="margin-top:10px; padding:8px;
                        background:{status_color}; color:white;
                        font-weight:600; text-align:center;
                        border-radius:6px;">
                {status}
            </div>
            """,
            unsafe_allow_html=True,
        )

        if btn_clicked:
            return match
    return None


def render_detailed_scorecard(scorecard_data):
    """Render detailed scorecard when match is selected"""
    st.header("📊 Detailed Scorecard")
    st.markdown("<hr style='border: 3px solid #000; margin: 10px 0;'>", unsafe_allow_html=True)

    if not scorecard_data or "scorecard" not in scorecard_data:
        st.warning("⚠️ Scorecard data not available")
        return

    for innings in scorecard_data["scorecard"]:
        team_name = innings.get("batteamname", f"Innings {innings.get('inningsid')}")
        st.subheader(f"🏏 {team_name} Innings")

        # Batting
        batsmen = innings.get("batsman", [])
        if batsmen:
            st.markdown("### Batting")
            df_bat = pd.DataFrame(batsmen)[
                ["name", "runs", "balls", "fours", "sixes", "strkrate", "outdec"]
            ]
            df_bat.columns = ["Batsman", "Runs", "Balls", "4s", "6s", "Strike Rate", "Status"]
            st.table(df_bat)

        # Bowling
        bowlers = innings.get("bowler", [])
        if bowlers:
            st.markdown("### Bowling")
            df_bowl = pd.DataFrame(bowlers)[
                ["name", "overs", "maidens", "runs", "wickets", "economy"]
            ]
            df_bowl.columns = ["Bowler", "Overs", "Maiden", "Runs", "Wickets", "Economy"]
            st.table(df_bowl)

        # Fall of Wickets
        fow = innings.get("fow", {}).get("fow", [])
        if fow:
            st.markdown("### Fall of Wickets")
            fow_df = pd.DataFrame(fow)[["batsmanname", "runs", "overnbr"]]
            fow_df.columns = ["Batsman Out", "Score", "Over"]
            st.table(fow_df)

        # Partnerships
        partnerships = innings.get("partnership", {}).get("partnership", [])
        if partnerships:
            st.markdown("### Partnerships")
            part_df = pd.DataFrame(partnerships)[
                ["bat1name", "bat1runs", "bat2name", "bat2runs", "totalruns", "totalballs"]
            ]
            part_df.columns = ["Batsman 1", "Runs (B1)", "Batsman 2", "Runs (B2)", "Total Runs", "Balls Faced"]
            st.table(part_df)

        # Powerplays
        powerplays = [pp for pp in innings.get("pp", {}).get("powerplay", []) if pp]
        if powerplays:
            st.markdown("### Powerplays")
            pp_df = pd.DataFrame(powerplays)
            if "pptype" in pp_df.columns:
                pp_df["pptype"] = pp_df["pptype"].str.title()
            pp_df = pp_df[["pptype", "ovrfrom", "ovrto", "run", "wickets"]]
            pp_df.columns = ["Type", "From", "To", "Runs", "Wkts"]
            st.table(pp_df)

        # Extras
        extras = innings.get("extras", {})
        if extras:
            st.markdown(
                f"**Extras:** {extras.get('total',0)} "
                f"(b {extras.get('byes',0)}, lb {extras.get('legbyes',0)}, "
                f"w {extras.get('wides',0)}, nb {extras.get('noballs',0)}, p {extras.get('penalty',0)})"
            )

        # Final Total
        st.markdown(
            f"**Total:** {innings.get('score','-')}/{innings.get('wickets','-')} "
            f"({innings.get('overs','-')} overs, RR: {innings.get('runrate','-')})"
        )
        st.markdown("<hr style='border: 2px solid #000; margin: 10px 0;'>", unsafe_allow_html=True)


def update_page(live_response, scorecard_data):
    """Main UI Page"""
    st.set_page_config(page_title="Live Cricket Scores", layout="wide")
    st.title("🏏 Live Cricket Scorecards")

    scorecards = extract_scorecards(live_response)
    if not scorecards:
        st.warning("No matches found.")
        return

    clicked_match = None
    cols = st.columns(2, gap="large")
    for idx, match in enumerate(scorecards):
        with cols[idx % 2]:
            selected = render_match_card(match)
            if selected:
                st.markdown("---")
                # print(match.get("match_id"))
                # print(match.get("match_id") in scorecard_data)
                render_detailed_scorecard(scorecard_data.get(match.get("match_id")))
