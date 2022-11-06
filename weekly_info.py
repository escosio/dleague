from center_of_the_football_universe import get_game_info,response

games = get_game_info()

def get_bye_teams(): 
    bye_teams = []
    teams_on_bye = response.json()["week"]["teamsOnBye"]
    for nested_item in teams_on_bye:
        team = nested_item["displayName"]
        bye_teams.append(team)
    return bye_teams

def met_life(dict):
    print("Teams playing at MetLife")
    for game in dict:
        if dict[game].get("venue")=="MetLife Stadium":
            print(dict[game].get("away"))
            print(dict[game].get("home"))

bye_teams = get_bye_teams()
print("BYE Teams")
print(bye_teams)
met_life(games)
