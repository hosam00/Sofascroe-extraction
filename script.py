import requests

class sofaScoreScraper:
    def __init__(self):
        self.session = requests.session()
    
    def return_response(self):
        url = "https://api.sofascore.com/api/v1/sport/football/events/live"
        response = self.session.get(url).json()
        return response

    def extract_data(self):
        games = self.return_response()
        for game in games['events']:
            league = game['tournament']['name']
            home_team = game['homeTeam']['name']
            away_team = game['awayTeam']['name']
            home_score = game['homeScore']['current']
            away_score = game['awayScore']['current']
            print(f'{league} | {home_team} {home_score} - {away_score} {away_team}')


scraper = sofaScoreScraper()
scraper.extract_data()
