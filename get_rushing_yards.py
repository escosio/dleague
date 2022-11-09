import requests
from center_of_the_football_universe import get_game_info,response,dleague_teams

games = get_game_info()
event_ids = list(games.keys())

def get_game_rushing(event_id,home_away):
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
        if home_away == True:
            print(home_team, ":")
            for rusher,yards in home_rushers.items():
                print(rusher,yards, sep=",")
        elif home_away == False:
            print(away_team, ":")
            for rusher,yards in away_rushers.items():
                print(rusher, yards, sep=",")
    except:
        pass
        # print(f"The {away_team} and {home_team} may not have played yet")

def create_yards_dict():
    rush_stat_dict = {}
    for event in event_ids:
        team_rush_stats = get_game_rushing(event)
        # rush_stat_dict[home]

# filter 
def get_relevant_game_ids(dleague_teams):
    games = {}
    for game in range(0,16):
        try:
            teams = response.json()["events"][game]["name"].split(" at ")
            venue = response.json()["events"][game]["competitions"][0]["venue"]["fullName"]
            id = response.json()["events"][game]["id"]
            for team in dleague_teams:
                if team in teams[0]:
                    games[id]= {
                        "team": team,
                        "home_game": False,
                        "venue": venue
                        }
                elif team in teams[1]:
                    games[id] = {
                        "team": team,
                        "home_game": True,
                        "venue": venue
                        }
        except:
            break
    return games

game_ids = get_relevant_game_ids(dleague_teams)
for id in game_ids:
    get_game_rushing(id, game_ids[id].get("home_game"))
