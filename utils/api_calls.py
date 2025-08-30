import requests

def perform_api_call(url, api_key, query_strings=None):
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "cricbuzz-cricket.p.rapidapi.com"
    }
    # print(f"inside the api call: {query_strings}")
    response = requests.get(url, headers=headers, params=query_strings)
    if response.status_code == 200:
        return response.json()
    return {}