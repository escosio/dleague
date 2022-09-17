import unittest
from venue_data import venue_distances,schedule

current_week = 2

def get_home_team(team, week):
    for game in schedule:
        # if it is the current week and the team is either home or away
        if game[0] == str(week) and team in game:
            # should be 3rd in the list
            home_team = game[-1]
            # print("home team is:", home_team)
            return home_team

def get_penalty(team, yards):
    home_team = get_home_team(team, current_week)
    print("The home team is",home_team,"and the game is being played in",venue_distances[home_team].get("venue"))
    penalty = float(venue_distances[home_team].get("distance")) * .01
    print("Weekly score:", round(yards - penalty, 2))
    # print((team, venue_distances[team].get("venue")), round(yards - penalty, 2), sep=" => ")

weekly_plays = {
    "Duncan": {
        "team":"Philadelphia Eagles",
        "yards": 87
    },
    "Evan": {
        "team":"Carolina Panthers",
        "yards": 65
    },
    "Phil": {
        "team":"New York Giants",
        "yards": 164
    },
    "Scott":{
        "team":"Indianapolis Colts",
        "yards": 112
    }
}

print("Welcome to the CENTER OF THE FOOTBALL UNIVERSE")
for player in weekly_plays:
    print(player)
    get_penalty(weekly_plays[player].get("team"),weekly_plays[player].get("yards"))
    print("\n")