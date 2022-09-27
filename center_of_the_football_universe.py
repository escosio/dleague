from venue_data import venue_penalties
from enter_scores import current_week,weekly_plays

import requests

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
week = response.json()["week"]["number"]

# create a dict of where a team is playing each given week
def get_venue_dict():
    dict = {}
    print("Week", week)
    for game in range(0,16):
        teams = response.json()["events"][game]["name"].split(" at ")
        venue = response.json()["events"][game]["competitions"][0]["venue"]["fullName"]
        dict[teams[0]]=venue
        dict[teams[1]]=venue
    return dict 

def met_life(dict):
    for team,venue in dict.items():
        if venue == 'MetLife Stadium':
            print(team)

# don't need this anymore
def is_international(week,team):
    is_international = bool()
    #  week 4 vikings saints
    if week == 4 and team in ("Minnesota Vikings","New Orleans Saints"):
        is_international = True
    # week 5 giants packers
    elif week == 5 and team in ("New York Giants","Green Bay Packers"):
        is_international = True
    # week 8 broncos jags
    elif week == 8 and team in ("Denver Broncos","Jacksonville Jaguars"):
        is_international = True
    # week 10 seahawks bucs
    elif week == 10 and team in ("Seattle Seahawks","Tampa Bay Buccaneers"):
        is_international = True
    # week 11 49ers Cardinals 
    elif week == 11 and team in ("San Francisco 49ers","Arizona Cardinals"):
        is_international = True
    else:
        is_international = False
    return is_international

def get_penalty(team, yards, lookup_venue):
    venue = lookup_venue[team]
    penalty = float(venue_penalties[venue])
    print("The ", team, "are playing at", venue, "and the penalty is", penalty)
    print("penalty is", penalty)
    print("Week score:", round(yards - penalty, 2))
    
def find_team(team, dict):
    for key in dict:
        if team in key:
            return key

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
    weekly_venues = get_venue_dict()
    for player in weekly_plays:
        team = find_team(weekly_plays[player].get("team"), weekly_venues)
        print(player, "plays", team)
        get_penalty(team, weekly_plays[player].get("yards"),weekly_venues)
        print("\n")


