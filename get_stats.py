import requests
import nfl_data_py as nfl

# nfl.see_weekly_cols()

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
    for team,venue in team_locations.items():
        if venue == 'MetLife Stadium':
            print(team)


team_locations = get_venue_dict()
# print(team_locations)
rushing = nfl.import_ngs_data("rushing", [2022])
print(rushing.columns)
week5 = rushing.loc[rushing['week'] == 5, ['team_abbr','player_display_name','player_position','rush_yards']]
# week5['season','week'] = rushing['season','week']
nyg = week5.loc[week5['team_abbr'] == 'NYG']