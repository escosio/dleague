import unittest
from venue_data import venue_distances,schedule,intl_games

current_week = 2

#  enter scores here
weekly_plays = {
    "Duncan": {
        "team":"Philadelphia Eagles",
        "yards": 0
    },
    "Evan": {
        "team":"Carolina Panthers",
        "yards": 0
    },
    "Phil": {
        "team":"New York Giants",
        "yards": 0
    },
    "Scott":{
        "team":"Indianapolis Colts",
        "yards": 0
    }
}

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
    elif week == 4 and team in ("Minnesota Vikings","New Orleans Saints"):
        is_international = True
    else:
        is_international = False
    return is_international


def get_home_team(team, week):
    is_intl_game = is_international(week,team)
    if is_intl_game == True:
        return intl_games[str(week)]
    elif is_intl_game == False:
        for game in schedule:
            # if it is the current week and the team is either home or away
            if game[0] == str(week) and team in game:
                # should be 3rd in the list
                home_team = game[-1]
                # print("home team is:", home_team)
                return home_team

def get_penalty(team, yards):
    home_team = get_home_team(team, current_week)
    print("The home team is",home_team,"and game being played in",venue_distances[home_team].get("venue"))
    penalty = float(venue_distances[home_team].get("distance")) * .01
    print("penalty is", penalty)
    print("Week score:", round(yards - penalty, 2))

if __name__ == '__main__':
    print("""\
            
                            
                    .-'||'-.
                  .'   ||   '.
                 /   __||__   \\
                 | /`-    -`\ |
                 | | 6    6 | |
                 \/\____7___/\/
        .--------:\:I:II:I:/;--------.
        /          \`:I::I:`/           \\
        |            `------'            |
        |             \____/             |
        |      ,    __     ___    ,      |
        |======|   /  |   / _ \   |======|
        |======|   ^| |  | | | |  |======|
        |~~~~~|     | |  | |_| |   |~~~~~|
        |     |\   [___]  \___/   /|     |
        \    \|                  |/    /
        `\    \  _ _.-=""=-._ _  /    /'
        `\   '`_)\\-++++-//(_`'   /'
            ;   (__||      ||__)   ;
            ;   ___\      /___   ;
            '. ---/-=..=-\--- .'
                `""`        `""`

            """)
    print("Welcome to the CENTER OF THE FOOTBALL UNIVERSE","\n")
    for player in weekly_plays:
        print(player, "plays", weekly_plays[player].get("team"))
        get_penalty(weekly_plays[player].get("team"),weekly_plays[player].get("yards"))
        print("\n")