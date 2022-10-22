from venue_data import venue_penalties
from enter_scores import weekly_plays

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
        try:
            teams = response.json()["events"][game]["name"].split(" at ")
            venue = response.json()["events"][game]["competitions"][0]["venue"]["fullName"]
            dict[teams[0]]=venue
            dict[teams[1]]=venue
        except:
            pass
    return dict 

def met_life(dict):
    for team,venue in dict.items():
        if venue == 'MetLife Stadium':
            print(team)

def get_penalty(team_name, yards, lookup_venue):
    venue = lookup_venue[team_name]
    penalty = float(venue_penalties[venue])
    print("The ", team_name, "are playing at", venue, "and the penalty is", penalty)
    # print("penalty is", penalty)
    print("Week score:", round(yards - penalty, 2))
    
def find_team(team, dict):
    for key in dict:
        if team in key:
            return key

def get_bye_teams(): 
    teams_on_bye = response.json()["week"]["teamsOnBye"]
    print("Teams on BYE this week:")
    for nested_item in teams_on_bye:
        print(nested_item["displayName"])
    print("\n")


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
    get_bye_teams()
    weekly_venues = get_venue_dict()
    for player in weekly_plays:
        team_name = str(weekly_plays[player].get("team"))
        team = find_team(team_name.title(), weekly_venues)
        print(player, "plays", team_name)
        if team in list(weekly_venues.keys()):
            get_penalty(team, weekly_plays[player].get("yards"),weekly_venues)
            print("\n")
        else:
            print(f"Could not find a game for the {team_name} this week. Do they have a bye?", '\n')


