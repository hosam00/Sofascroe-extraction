import requests
import json

url = "https://api.sofascore.com/api/v1/sport/football/events/live"
response = requests.request("GET", url)
json_data = json.loads(response.text)

for game in json_data['events']:
    league = game['tournament']['name']
    home_team = game['homeTeam']['name']
    away_team = game['awayTeam']['name']
    home_score = game['homeScore']['current']
    away_score = game['awayScore']['current']
    print(f'{league} | {home_team} {home_score} - {away_score} {away_team}')
