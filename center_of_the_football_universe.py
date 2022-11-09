from venue_data import venue_penalties
from enter_scores import weekly_plays
import datetime
import requests

scorecard_api = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
summary_api="http://site.api.espn.com/apis/site/v2/sports/football/nfl/summary"

payload= {}
headers = {}

response = requests.request("GET", scorecard_api, headers=headers, data=payload)
week = response.json()["week"]["number"]

dleague_teams = [weekly_plays[player].get('team').title() for player in weekly_plays]

# stealing duncan's function
def get_specific_week(week_number):
    days = []
    for days_forward in range(7):
        day = (datetime.date(2022, 9, 8) + datetime.timedelta(days=(days_forward + (week_number-1)*7))).strftime('%Y%m%d')
        days.append(day)
    return days

# get home, away and venue in one fell swoop
def get_game_info():
    games = {}
    for game in range(0,16):
        try:
            teams = response.json()["events"][game]["name"].split(" at ")
            venue = response.json()["events"][game]["competitions"][0]["venue"]["fullName"]
            id = response.json()["events"][game]["id"]
            # could only return ids for games with teams but needs more work
            # if teams[0] in dleague_teams or teams[1] in dleague_teams:
            games[id]= {
                "away": teams[0],
                "home": teams[1],
                "venue": venue
                }
        except:
            break
    return games

def get_penalty(team_name, yards, venue):
    penalty = float(venue_penalties[venue])
    print("The ", team_name, "are playing at", venue, "and the penalty is", penalty)
    print("Week score:", round(yards - penalty, 2))

# to lookup the team using the keyword 
def find_team(team, dict):
    try:
        for key in dict:
            if team in dict[key].get("away"):
                team_name = dict[key].get("away")
                venue = dict[key].get("venue")
                return team_name, venue
            elif team in dict[key].get("home"):
                team_name = dict[key].get("home")
                venue = dict[key].get("venue")
                return team_name, venue
    except:
        pass

def find_dleague_teams():
    for dleaguer in weekly_plays:
        try:
            info = find_team(weekly_plays[dleaguer].get("team").title(), game_dict)
            team = info[0]
            venue = info[1]
            yards = weekly_plays[dleaguer].get("yards")
            get_penalty(team, yards, venue)
        except:
            # print(weekly_plays[dleaguer].get("team").title(), "could not be found, BYE week?")
            pass

if __name__ == '__main__':
    print("""\
        
                       ,,,,
                    ▓████████╕ ████ ,██████▌ ]███▓   ████████████████████
                   ╫███╨ ╟███⌐║███▌ ███▌▓██▌ ╫████⌐ ╫███╙╟███▌╙████└'▓███
                  ]███▌  ▀▀▀▀ ████ ▓███ ███▒ █████▌ ███▌ ▓███ ]████, ╙╙╙╙
                  ╫███¬▄▄▄▄▄▄▓███▌╫███ ]███⌐║██████╟███ ]███▌  ▓██████▓╕
                 ]███▌]██████████▐███▓▓▓███ ███▌╟█████▌ ╫███ ,,,,└╙▀███▓
                 ▓███  ╫███ ╟███▒████▀▀████▐███  █████⌐]███▌ ▓███  ║███▒
                 ████▓▓███▌ ████████   ███████▌  ▓███▓ ╫███⌐ ████▓▓███▓
                 ╙▀▀▀▀▀▀▀╙ ╚▀▀▀▀▀▀▀   '▀▀▀▀▀▀▀   ╙▀▀▀⌐ ▀▀▀▀  ╙▀▀▀▀▀▀▀`
               ]▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
               ▓█████████████████████████████████████████████████████▌
             
    
    """)
    print("Welcome to the CENTER OF THE FOOTBALL UNIVERSE","\n")
    game_dict = get_game_info()
    for dleaguer in weekly_plays:
        try:
            info = find_team(weekly_plays[dleaguer].get("team").title(), game_dict)
            team = info[0]
            venue = info[1]
            yards = weekly_plays[dleaguer].get("yards")
            get_penalty(team, yards, venue)
        except:
            # print(weekly_plays[dleaguer].get("team").title(), "could not be found, BYE week?")
            pass

