import requests
from center_of_the_football_universe import get_game_info

games = get_game_info()
event_ids = list(games.keys())

def get_game_rushing(event_id):
    url = f"http://site.api.espn.com/apis/site/v2/sports/football/nfl/summary?event={event_id}"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    away_team = response.json()["boxscore"]["teams"][0]["team"]["displayName"]
    home_team = response.json()["boxscore"]["teams"][1]["team"]["displayName"]
    try:
        away_rushing = response.json()["boxscore"]["players"][0]["statistics"][1]["athletes"]
        home_rushing = response.json()["boxscore"]["players"][1]["statistics"][1]["athletes"]

        def get_rushing_athletes(team_rushing):
            dict = {}
            for athlete in team_rushing:
                athlete_name = athlete["athlete"].get("displayName")
                stats = int(athlete["stats"][1])
                dict[athlete_name]=stats
            return dict

        home_rushers = get_rushing_athletes(home_rushing)
        away_rushers = get_rushing_athletes(away_rushing)
        # need to figure out how to choose home vs away
        print(home_team)
        for rusher,yards in home_rushers.items():
            print(rusher,yards)
        print(away_team)
        for rusher,yards in away_rushers.items():
            print(rusher,yards)
    except:
        pass
        # print(f"The {away_team} and {home_team} may not have played yet")

for event in event_ids:
    get_game_rushing(event)

