import streamlit as st
import pandas as pd

live_response = {'typeMatches': [{'matchType': 'League', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 9575, 'seriesName': 'Caribbean Premier League 2025', 'matches': [{'matchInfo': {'matchId': 116696, 'seriesId': 9575, 'seriesName': 'Caribbean Premier League 2025', 'matchDesc': '14th Match', 'matchFormat': 'T20', 'startDate': '1756335600000', 'endDate': '1756348200000', 'state': 'Complete', 'status': 'Trinbago Knight Riders won by 8 wkts', 'team1': {'teamId': 1978, 'teamName': 'Antigua and Barbuda Falcons', 'teamSName': 'ABF', 'imageId': 507236}, 'team2': {'teamId': 271, 'teamName': 'Trinbago Knight Riders', 'teamSName': 'TKR', 'imageId': 172325}, 'venueInfo': {'id': 500, 'ground': 'Brian Lara Stadium', 'city': 'Tarouba, Trinidad', 'timezone': '-04:00', 'latitude': '10.295034', 'longitude': '-61.445609'}, 'currBatTeamId': 271, 'seriesStartDt': '1755043200000', 'seriesEndDt': '1758499200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 146, 'wickets': 7, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 152, 'wickets': 2, 'overs': 18.4}}}}]}}]}, {'matchType': 'Domestic', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matches': [{'matchInfo': {'matchId': 123655, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '1st Quarter-Final', 'matchFormat': 'TEST', 'startDate': '1756353600000', 'endDate': '1756638000000', 'state': 'In Progress', 'status': 'Day 1: 1st Session', 'team1': {'teamId': 233, 'teamName': 'North Zone', 'teamSName': 'NZONE', 'imageId': 172286}, 'team2': {'teamId': 235, 'teamName': 'East Zone', 'teamSName': 'EZONE', 'imageId': 172288}, 'venueInfo': {'id': 1438087, 'ground': 'BCCI Centre of Excellence Ground', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '12.978853', 'longitude': '77.599533'}, 'currBatTeamId': 233, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 15, 'overs': 4.6}}}}, {'matchInfo': {'matchId': 123661, 'seriesId': 10311, 'seriesName': 'Duleep Trophy 2025', 'matchDesc': '2nd Quarter-Final', 'matchFormat': 'TEST', 'startDate': '1756353600000', 'endDate': '1756638000000', 'state': 'In Progress', 'status': 'Day 1: 1st Session', 'team1': {'teamId': 237, 'teamName': 'Central Zone', 'teamSName': 'CZONE', 'imageId': 172290}, 'team2': {'teamId': 1146, 'teamName': 'North East Zone', 'teamSName': 'NEZONE', 'imageId': 242496}, 'venueInfo': {'id': 1438102, 'ground': 'BCCI Centre of Excellence Ground B', 'city': 'Bengaluru', 'timezone': '+05:30', 'latitude': '13.174092', 'longitude': '77.706999'}, 'currBatTeamId': 237, 'seriesStartDt': '1756252800000', 'seriesEndDt': '1757980800000', 'isTimeAnnounced': True, 'stateTitle': 'In Progress'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 5, 'wickets': 1, 'overs': 2.6}}}}]}}, {'seriesAdWrapper': {'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matches': [{'matchInfo': {'matchId': 129007, 'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matchDesc': '23rd Match', 'matchFormat': 'ODI', 'startDate': '1756288800000', 'endDate': '1756317600000', 'state': 'Complete', 'status': 'No result', 'team1': {'teamId': 14, 'teamName': 'Kenya', 'teamSName': 'KEN', 'imageId': 172129}, 'team2': {'teamId': 287, 'teamName': 'Papua New Guinea', 'teamSName': 'PNG', 'imageId': 172336}, 'venueInfo': {'id': 1563, 'ground': 'Grainville', 'city': 'St Saviour', 'timezone': '+01:00', 'latitude': '49.1995792', 'longitude': '-2.087867'}, 'seriesStartDt': '1727136000000', 'seriesEndDt': '1769731200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 275, 'wickets': 8, 'overs': 49.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 53, 'wickets': 2, 'overs': 14.3}}}}, {'matchInfo': {'matchId': 129018, 'seriesId': 8993, 'seriesName': 'ICC CWC Challenge League A, 2024-26', 'matchDesc': '24th Match', 'matchFormat': 'ODI', 'startDate': '1756288800000', 'endDate': '1756317600000', 'state': 'Complete', 'status': 'No result', 'team1': {'teamId': 525, 'teamName': 'Qatar', 'teamSName': 'QAT', 'imageId': 172575}, 'team2': {'teamId': 185, 'teamName': 'Denmark', 'teamSName': 'DEN', 'imageId': 172245}, 'venueInfo': {'id': 1566, 'ground': 'Farmers Cricket Club Ground', 'city': 'St Martin', 'timezone': '+01:00', 'latitude': '49.2184521', 'longitude': '-2.0601565'}, 'seriesStartDt': '1727136000000', 'seriesEndDt': '1769731200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 265, 'wickets': 7, 'overs': 49.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 37, 'wickets': 3, 'overs': 15.6}}}}]}}]}, {'matchType': 'Women', 'seriesMatches': [{'seriesAdWrapper': {'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matches': [{'matchInfo': {'matchId': 131235, 'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matchDesc': '12th Match', 'matchFormat': 'T20', 'startDate': '1756302300000', 'endDate': '1756314900000', 'state': 'Complete', 'status': 'Italy Women need 34 runs in 9 balls', 'team1': {'teamId': 189, 'teamName': 'Ireland Women', 'teamSName': 'IREW', 'imageId': 172249}, 'team2': {'teamId': 1125, 'teamName': 'Italy Women', 'teamSName': 'ITAW', 'imageId': 248417}, 'venueInfo': {'id': 265, 'ground': 'Hazelaarweg', 'city': 'Rotterdam', 'timezone': '+02:00', 'latitude': '51.922829', 'longitude': '4.478450'}, 'currBatTeamId': 189, 'seriesStartDt': '1755561600000', 'seriesEndDt': '1756339200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 175, 'wickets': 6, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 142, 'wickets': 9, 'overs': 18.3}}}}, {'matchInfo': {'matchId': 131229, 'seriesId': 10669, 'seriesName': 'ICC Womens T20 World Cup Europe Qualifier Division 1, 2025', 'matchDesc': '11th Match', 'matchFormat': 'T20', 'startDate': '1756285200000', 'endDate': '1756297800000', 'state': 'Complete', 'status': 'Netherlands Women won by 65 runs', 'team1': {'teamId': 188, 'teamName': 'Netherlands Women', 'teamSName': 'NEDW', 'imageId': 172248}, 'team2': {'teamId': 504, 'teamName': 'Germany Women', 'teamSName': 'GERW', 'imageId': 172553}, 'venueInfo': {'id': 265, 'ground': 'Hazelaarweg', 'city': 'Rotterdam', 'timezone': '+02:00', 'latitude': '51.922829', 'longitude': '4.478450'}, 'currBatTeamId': 188, 'seriesStartDt': '1755561600000', 'seriesEndDt': '1756339200000', 'isTimeAnnounced': True, 'stateTitle': 'Complete'}, 'matchScore': {'team1Score': {'inngs1': {'inningsId': 1, 'runs': 175, 'wickets': 4, 'overs': 19.6}}, 'team2Score': {'inngs1': {'inningsId': 2, 'runs': 110, 'wickets': 1, 'overs': 19.6}}}}]}}]}], 'filters': {'matchType': ['International', 'League', 'Domestic', 'Women']}, 'appIndex': {'seoTitle': 'Live Cricket Score - Scorecard and Match Results', 'webURL': 'www.cricbuzz.com/live-cricket-scores/'}, 'responseLastUpdated': '1756358017'}
scorecard_data = {'scorecard': [{'inningsid': 1, 'batsman': [{'id': 9394, 'balls': 2, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'R Cornwall', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'lbw b Amir', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 54287, 'balls': 31, 'runs': 40, 'fours': 3, 'sixes': 2, 'strkrate': '129.03', 'name': 'Jewel Andrew', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'c McKenny Clarke b Russell', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 14811, 'balls': 3, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Karima Gore', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'lbw b Amir', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11959, 'balls': 17, 'runs': 14, 'fours': 1, 'sixes': 0, 'strkrate': '82.35', 'name': 'Andries Gous', 'nickname': '', 'iscaptain': False, 'iskeeper': True, 'outdec': 'b Akeal Hosein', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 544, 'balls': 14, 'runs': 13, 'fours': 2, 'sixes': 0, 'strkrate': '92.86', 'name': 'Shakib', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'c Narine b Akeal Hosein', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 10408, 'balls': 25, 'runs': 37, 'fours': 5, 'sixes': 0, 'strkrate': '148', 'name': 'Imad Wasim', 'nickname': '', 'iscaptain': True, 'iskeeper': False, 'outdec': 'not out', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 9785, 'balls': 2, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Fabian Allen', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'c Pooran b Russell', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11318, 'balls': 26, 'runs': 34, 'fours': 2, 'sixes': 3, 'strkrate': '130.77', 'name': 'Usama Mir', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'c Pollard b Amir', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 15817, 'balls': 1, 'runs': 1, 'fours': 0, 'sixes': 0, 'strkrate': '100', 'name': 'Jayden Seales', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': 'not out', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 13632, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Salman Irshad', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11221, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Obed McCoy', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': 'IN'}], 'bowler': [{'id': 1917, 'overs': '4', 'maidens': 1, 'wickets': 3, 'runs': 22, 'economy': '5.5', 'name': 'Amir', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11450, 'overs': '3', 'maidens': 0, 'wickets': 0, 'runs': 26, 'economy': '8.7', 'name': 'Ali Khan', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 18, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': 'IN'}, {'id': 23306, 'overs': '1', 'maidens': 0, 'wickets': 0, 'runs': 13, 'economy': '13', 'name': 'McKenny Clarke', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 6, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 8435, 'overs': '4', 'maidens': 0, 'wickets': 2, 'runs': 25, 'economy': '6.2', 'name': 'Akeal Hosein', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 2276, 'overs': '4', 'maidens': 0, 'wickets': 0, 'runs': 34, 'economy': '8.5', 'name': 'Narine', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 7736, 'overs': '4', 'maidens': 1, 'wickets': 2, 'runs': 23, 'economy': '5.8', 'name': 'Russell', 'nickname': '', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}], 'fow': {'fow': [{'batsmanid': 9394, 'batsmanname': 'R Cornwall', 'overnbr': 0.2, 'runs': 0, 'ballnbr': 2}, {'batsmanid': 14811, 'batsmanname': 'Karima Gore', 'overnbr': 0.5, 'runs': 0, 'ballnbr': 5}, {'batsmanid': 11959, 'batsmanname': 'Andries Gous', 'overnbr': 6.4, 'runs': 46, 'ballnbr': 40}, {'batsmanid': 544, 'batsmanname': 'Shakib', 'overnbr': 10.6, 'runs': 71, 'ballnbr': 66}, {'batsmanid': 54287, 'batsmanname': 'Jewel Andrew', 'overnbr': 11.1, 'runs': 71, 'ballnbr': 67}, {'batsmanid': 9785, 'batsmanname': 'Fabian Allen', 'overnbr': 11.3, 'runs': 71, 'ballnbr': 69}, {'batsmanid': 11318, 'batsmanname': 'Usama Mir', 'overnbr': 18.4, 'runs': 135, 'ballnbr': 112}]}, 'extras': {'legbyes': 3, 'byes': 0, 'wides': 3, 'noballs': 1, 'penalty': 0, 'total': 7}, 'pp': {'powerplay': [{'id': 7, 'ovrfrom': 0.1, 'ovrto': 6.0, 'pptype': 'mandatory', 'run': 43, 'wickets': 0}]}, 'score': 146, 'wickets': 7, 'overs': 20.0, 'runrate': 7.3, 'batteamname': 'Antigua and Barbuda Falcons', 'batteamsname': 'ABF', 'isdeclared': False, 'isfollowon': False, 'ballnbr': 120, 'rpb': 1.22, 'partnership': {'partnership': [{'id': 0, 'bat1id': 9394, 'bat1name': 'Cornwall', 'bat1runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2id': 54287, 'bat2name': 'Jewel Andrew', 'bat2runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalruns': 0, 'totalballs': 2, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 14811, 'bat1name': 'Karima Gore', 'bat1runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2id': 54287, 'bat2name': 'Jewel Andrew', 'bat2runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalruns': 0, 'totalballs': 3, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 11959, 'bat1name': 'Gous', 'bat1runs': 14, 'bat1fours': 1, 'bat1sixes': 0, 'bat2id': 54287, 'bat2name': 'Jewel Andrew', 'bat2runs': 29, 'bat2fours': 2, 'bat2sixes': 2, 'totalruns': 46, 'totalballs': 35, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 544, 'bat1name': 'Shakib', 'bat1runs': 13, 'bat1fours': 2, 'bat1sixes': 0, 'bat2id': 54287, 'bat2name': 'Jewel Andrew', 'bat2runs': 11, 'bat2fours': 1, 'bat2sixes': 0, 'totalruns': 25, 'totalballs': 26, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 10408, 'bat1name': 'Imad Wasim', 'bat1runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2id': 54287, 'bat2name': 'Jewel Andrew', 'bat2runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalruns': 0, 'totalballs': 1, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 10408, 'bat1name': 'Imad Wasim', 'bat1runs': 0, 'bat1fours': 0, 'bat1sixes': 0, 'bat2id': 9785, 'bat2name': 'Fabian Allen', 'bat2runs': 0, 'bat2fours': 0, 'bat2sixes': 0, 'totalruns': 0, 'totalballs': 2, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 10408, 'bat1name': 'Imad Wasim', 'bat1runs': 27, 'bat1fours': 3, 'bat1sixes': 0, 'bat2id': 11318, 'bat2name': 'Usama Mir', 'bat2runs': 34, 'bat2fours': 2, 'bat2sixes': 3, 'totalruns': 64, 'totalballs': 43, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}, {'id': 0, 'bat1id': 10408, 'bat1name': 'Imad Wasim', 'bat1runs': 10, 'bat1fours': 2, 'bat1sixes': 0, 'bat2id': 15817, 'bat2name': 'Jayden Seales', 'bat2runs': 1, 'bat2fours': 0, 'bat2sixes': 0, 'totalruns': 11, 'totalballs': 8, 'bat1balls': 0, 'bat2balls': 0, 'teamname': '', 'teamid': 0, 'bat1ones': 0, 'bat1twos': 0, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 0, 'bat2ones': 0, 'bat2twos': 0, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 0, 'bat2sixers': 0}]}}, {'inningsid': 2, 'batsman': [{'id': 8085, 'balls': 10, 'runs': 9, 'fours': 1, 'sixes': 0, 'strkrate': '90', 'name': 'Colin Munro', 'nickname': 'Munro', 'iscaptain': False, 'iskeeper': False, 'outdec': 'c Karima Gore b Shakib', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 6734, 'balls': 46, 'runs': 55, 'fours': 6, 'sixes': 0, 'strkrate': '119.57', 'name': 'Alex Hales', 'nickname': 'Hales', 'iscaptain': False, 'iskeeper': False, 'outdec': 'not out', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11217, 'balls': 45, 'runs': 60, 'fours': 4, 'sixes': 2, 'strkrate': '133.33', 'name': 'Keacy Carty', 'nickname': 'Keacy Carty', 'iscaptain': False, 'iskeeper': False, 'outdec': 'b Jayden Seales', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 9406, 'balls': 11, 'runs': 23, 'fours': 0, 'sixes': 2, 'strkrate': '209.09', 'name': 'Nicholas Pooran', 'nickname': 'Pooran', 'iscaptain': True, 'iskeeper': True, 'outdec': 'not out', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 657, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Kieron Pollard', 'nickname': 'Pollard', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 7736, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Andre Russell', 'nickname': 'Russell', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 8435, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Akeal Hosein', 'nickname': 'Akeal Hosein', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 2276, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Sunil Narine', 'nickname': 'Narine', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 23306, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'McKenny Clarke', 'nickname': 'McKenny Clarke', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 1917, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Mohammad Amir', 'nickname': 'Amir', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11450, 'balls': 0, 'runs': 0, 'fours': 0, 'sixes': 0, 'strkrate': '0', 'name': 'Ali Khan', 'nickname': 'Ali Khan', 'iscaptain': False, 'iskeeper': False, 'outdec': '', 'videotype': '', 'videourl': '', 'videoid': 0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'iscbplusfree': False, 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': 'IN'}], 'bowler': [{'id': 15817, 'overs': '3.4', 'maidens': 0, 'wickets': 1, 'runs': 35, 'economy': '9.5', 'name': 'Jayden Seales', 'nickname': 'Jayden Seales', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 22, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11221, 'overs': '3', 'maidens': 0, 'wickets': 0, 'runs': 33, 'economy': '11', 'name': 'Obed McCoy', 'nickname': 'Obed McCoy', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 18, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': 'IN'}, {'id': 544, 'overs': '4', 'maidens': 0, 'wickets': 1, 'runs': 25, 'economy': '6.2', 'name': 'Shakib Al Hasan', 'nickname': 'Shakib', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 13632, 'overs': '4', 'maidens': 0, 'wickets': 0, 'runs': 26, 'economy': '6.5', 'name': 'Salman Irshad', 'nickname': 'Salman Irshad', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 24, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 11318, 'overs': '2', 'maidens': 0, 'wickets': 0, 'runs': 11, 'economy': '5.5', 'name': 'Usama Mir', 'nickname': 'Usama Mir', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 12, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}, {'id': 14811, 'overs': '2', 'maidens': 0, 'wickets': 0, 'runs': 21, 'economy': '10.5', 'name': 'Karima Gore', 'nickname': 'Karima Gore', 'iscaptain': False, 'iskeeper': False, 'videotype': '', 'videourl': '', 'videoid': 0, 'dots': 0, 'balls': 12, 'rpb': 0.0, 'planid': 0, 'imageid': 0, 'premiumvideourl': '', 'ispremiumfree': False, 'inmatchchange': '', 'isoverseas': False, 'playingxichange': ''}], 'fow': {'fow': [{'batsmanid': 8085, 'batsmanname': 'Colin Munro', 'overnbr': 3.3, 'runs': 27, 'ballnbr': 21}, {'batsmanid': 11217, 'batsmanname': 'Keacy Carty', 'overnbr': 15.4, 'runs': 114, 'ballnbr': 94}]}, 'extras': {'legbyes': 1, 'byes': 0, 'wides': 4, 'noballs': 0, 'penalty': 0, 'total': 5}, 'pp': {'powerplay': [{'id': 8, 'ovrfrom': 0.1, 'ovrto': 6.0, 'pptype': 'mandatory', 'run': 42, 'wickets': 0}]}, 'score': 152, 'wickets': 2, 'overs': 18.4, 'runrate': 8.14, 'batteamname': 'Trinbago Knight Riders', 'batteamsname': 'TKR', 'isdeclared': False, 'isfollowon': False, 'ballnbr': 112, 'rpb': 1.36, 'partnership': {'partnership': [{'id': 0, 'bat1id': 8085, 'bat1name': 'Munro', 'bat1runs': 9, 'bat1fours': 1, 'bat1sixes': 0, 'bat2id': 6734, 'bat2name': 'Hales', 'bat2runs': 18, 'bat2fours': 3, 'bat2sixes': 0, 'totalruns': 27, 'totalballs': 21, 'bat1balls': 10, 'bat2balls': 11, 'teamname': '', 'teamid': 0, 'bat1ones': 3, 'bat1twos': 1, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 1, 'bat1sixers': 0, 'bat2ones': 4, 'bat2twos': 1, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 3, 'bat2sixers': 0}, {'id': 0, 'bat1id': 11217, 'bat1name': 'Keacy Carty', 'bat1runs': 60, 'bat1fours': 4, 'bat1sixes': 2, 'bat2id': 6734, 'bat2name': 'Hales', 'bat2runs': 23, 'bat2fours': 1, 'bat2sixes': 0, 'totalruns': 87, 'totalballs': 73, 'bat1balls': 45, 'bat2balls': 28, 'teamname': '', 'teamid': 0, 'bat1ones': 18, 'bat1twos': 7, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 4, 'bat1sixers': 2, 'bat2ones': 15, 'bat2twos': 2, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 1, 'bat2sixers': 0}, {'id': 0, 'bat1id': 9406, 'bat1name': 'Pooran', 'bat1runs': 23, 'bat1fours': 0, 'bat1sixes': 2, 'bat2id': 6734, 'bat2name': 'Hales', 'bat2runs': 14, 'bat2fours': 2, 'bat2sixes': 0, 'totalruns': 38, 'totalballs': 18, 'bat1balls': 11, 'bat2balls': 7, 'teamname': '', 'teamid': 0, 'bat1ones': 5, 'bat1twos': 3, 'bat1threes': 0, 'bat1fives': 0, 'bat1boundaries': 0, 'bat1sixers': 2, 'bat2ones': 4, 'bat2twos': 1, 'bat2threes': 0, 'bat2fives': 0, 'bat2boundaries': 2, 'bat2sixers': 0}]}}], 'ismatchcomplete': True, 'appindex': {'seotitle': 'Cricket scorecard - TKR vs ABF 14th Match,Caribbean Premier League 2025 | Cricbuzz.com', 'weburl': 'http://www.cricbuzz.com/live-cricket-scorecard/116696/tkr-vs-abf-14th-match-caribbean-premier-league-2025'}, 'status': 'Trinbago Knight Riders won by 8 wkts', 'responselastupdated': 1756365236}

def render():
    update_page(live_response=live_response, scorecard_data=scorecard_data)

def extract_scorecards(data):
    scorecards = []
    for type_match in data.get("typeMatches", []):
        for series in type_match.get("seriesMatches", []):
            matches = series.get("seriesAdWrapper", {}).get("matches", [])
            for match in matches:
                info = match.get("matchInfo", {})
                score = match.get("matchScore", {})
                venue = info.get("venueInfo", {})
                ground = venue.get("ground", "Unknown Ground")
                city = venue.get("city", "Unknown City")

                team1 = info.get("team1", {})
                team2 = info.get("team2", {})

                team1_score = score.get("team1Score", {}).get("inngs1", {})
                team2_score = score.get("team2Score", {}).get("inngs1", {})

                state = info.get("state", "Unknown")
                result = info.get("status", "No status")
                match_status = result if state == "Complete" else "In Progress"

                scorecards.append({
                    "match_id": info.get("matchId"),
                    "team1": team1.get("teamName", "Team A"),
                    "team2": team2.get("teamName", "Team B"),
                    "match_format": info.get("matchFormat", "Unknown"),
                    "venue": f"{ground}, {city}",
                    "team1_score": f"{team1_score.get('runs', '-')}/{team1_score.get('wickets', '-')}"
                                    f" ({team1_score.get('overs', '-')})",
                    "team2_score": f"{team2_score.get('runs', '-')}/{team2_score.get('wickets', '-')}"
                                    f" ({team2_score.get('overs', '-')})",
                    "status": match_status
                })
    return scorecards

def render_match_card(match):
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

    # Build card using Streamlit containers
    with st.container(border=True):   # ✅ Streamlit 1.31+ supports border
        st.markdown(f"### {team1} vs {team2}")
        st.caption(f"{match_format.upper()} • 📍 {venue}")
        st.write(f"**{team1}:** {match['team1_score']}")
        st.write(f"**{team2}:** {match['team2_score']}")

        # Button (this will stay inside because it's inside the same container)
        btn_clicked = st.button("📊 View Scorecard", key=f"btn_{match['match_id']}")

        # Status bar
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
    st.header("📊 Detailed Scorecard")

    if not scorecard_data or "scorecard" not in scorecard_data:
        st.warning("⚠️ Scorecard data not available")
        return

    for innings in scorecard_data["scorecard"]:
        team_name = innings.get("batteamname", f"Innings {innings.get('inningsid')}")
        with st.expander(f"{team_name} Innings"):

            # 🏏 Batting
            batsmen = innings.get("batsman", [])
            if batsmen:
                st.subheader("Batting")
                df_bat = pd.DataFrame(batsmen)
                df_bat = df_bat[["name", "runs", "balls", "fours", "sixes", "strkrate", "outdec"]]
                df_bat.columns = ["Batsman", "Runs", "Balls", "4s", "6s", "Strike Rate", "Status"]
                # st.dataframe(df_bat, use_container_width=True)

                # Convert all columns to string so alignment works uniformly
                df_bat = df_bat.astype(str)

                # Force all columns to left align
                styled_bat = df_bat.style.set_properties(**{'text-align': 'left'})
                styled_bat = styled_bat.set_table_styles(
                    [dict(selector='th', props=[('text-align', 'left')])]
                )

                st.table(styled_bat)

            # 🎯 Bowling
            bowlers = innings.get("bowler", [])
            if bowlers:
                st.subheader("Bowling")
                df_bowl = pd.DataFrame(bowlers)
                df_bowl = df_bowl[["name", "overs", "maidens", "runs", "wickets", "economy"]]
                df_bowl.columns = ["Bowler", "Overs", "Maiden", "Runs", "Wickets", "Economy"]
                # st.dataframe(df_bowl, use_container_width=True)

                # Convert all columns to string so alignment works uniformly
                df_bowl = df_bowl.astype(str)

                # Force all columns to left align
                styled_bowl = df_bowl.style.set_properties(**{'text-align': 'left'})
                styled_bowl = styled_bowl.set_table_styles(
                    [dict(selector='th', props=[('text-align', 'left')])]
                )

                st.table(styled_bowl)

            # ⚡ Fall of Wickets
            fow = innings.get("fow", {}).get("fow", [])
            if fow:
                st.subheader("Fall of Wickets")
                fow_df = pd.DataFrame(fow)
                fow_df = fow_df[["batsmanname", "runs", "overnbr"]]
                fow_df.columns = ["Batsman Out", "Score", "Over"]
                # st.table(fow_df)

                # Convert all columns to string so alignment works uniformly
                fow_df = fow_df.astype(str)

                # Force all columns to left align
                styled_fow = fow_df.style.set_properties(**{'text-align': 'left'})
                styled_fow = styled_fow.set_table_styles(
                    [dict(selector='th', props=[('text-align', 'left')])]
                )

                st.table(styled_fow)

            # 🤝 Partnerships
            partnerships = innings.get("partnership", {}).get("partnership", [])
            if partnerships:
                st.subheader("Partnerships")
                part_df = pd.DataFrame(partnerships)
                part_df = part_df[["bat1name", "bat1runs", "bat2name", "bat2runs", "totalruns", "totalballs"]]
                part_df.columns = ["Batsman 1", "Runs (B1)", "Batsman 2", "Runs (B2)", "Total Runs", "Balls Faced"]
                # st.table(part_df)

                # Convert all columns to string so alignment works uniformly
                part_df = part_df.astype(str)

                # Force all columns to left align
                styled_part = part_df.style.set_properties(**{'text-align': 'left'})
                styled_part = styled_part.set_table_styles(
                    [dict(selector='th', props=[('text-align', 'left')])]
                )

                st.table(styled_part)


            # ⚡ Powerplays
            powerplays = innings.get("pp", {}).get("powerplay", [])
            if powerplays:
                st.subheader("Powerplays")
                pp_df = pd.DataFrame(powerplays)

                # Convert to Title Case
                if "pptype" in pp_df.columns:
                    pp_df["pptype"] = pp_df["pptype"].str.title()

                pp_df = pp_df[["pptype", "ovrfrom", "ovrto", "run", "wickets"]]
                pp_df.columns = ["Type", "From", "To", "Runs", "Wkts"]
                # st.table(pp_df)

                # Convert all columns to string so alignment works uniformly
                pp_df = pp_df.astype(str)

                # Force all columns to left align
                styled_pp = pp_df.style.set_properties(**{'text-align': 'left'})
                styled_pp = styled_pp.set_table_styles(
                    [dict(selector='th', props=[('text-align', 'left')])]
                )

                st.table(styled_pp)

            # ➕ Extras
            extras = innings.get("extras", {})
            if extras:
                st.markdown(
                    f"**Extras:** {extras.get('total',0)} "
                    f"(b {extras.get('byes',0)}, lb {extras.get('legbyes',0)}, "
                    f"w {extras.get('wides',0)}, nb {extras.get('noballs',0)}, p {extras.get('penalty',0)})"
                )

            # 📌 Final Total
            st.markdown(
                f"**Total:** {innings.get('score','-')}/{innings.get('wickets','-')} "
                f"({innings.get('overs','-')} overs, RR: {innings.get('runrate','-')})"
            )

def update_page(live_response, scorecard_data):
    st.set_page_config(page_title="Live Cricket Scores", layout="wide")
    st.title("🏏 Live Cricket Scorecards")
    scorecards = extract_scorecards(live_response)

    clicked_match = None

    if not scorecards:
        st.warning("No matches found.")
    else:
        # Display cards in rows of 2
        for i in range(0, len(scorecards), 2):
            cols = st.columns(2)

            for j, col in enumerate(cols):
                if i + j < len(scorecards):
                    match = scorecards[i + j]
                    with col:
                        selected = render_match_card(match)
                        if selected:
                            clicked_match = selected
                            # Show detailed view if clicked
                            if clicked_match:
                                st.markdown("---")
                                render_detailed_scorecard(scorecard_data)