import csv 

def create_venue_dict():
    csv_path = "dleague/venue_distances.csv"
    dict = {}
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dict[row["team"]] = {"venue":row["venue"],"distance":row["distance"]}
    return dict

def get_schedule():
    schedule_csv = "dleague/schedule.csv"
    schedule = []
    with open(schedule_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row_data = list([row["Week"],row["Away"],row["Home"]])
            schedule.append(row_data)
    return schedule
# to import from CSVs, hardcoded below
# venue_distances = create_venue_dict()
# schedule = get_schedule()

# converted dicts
venue_distances = { 
    'Pittsburgh Steelers': {'venue': 'Acrisure Stadium', 'distance': '311.46'},
    'Las Vegas Raiders': {'venue': 'Allegiant Stadium', 'distance': '2228.14'},
    'Kansas City Chiefs': {'venue': 'GEHA Field at Arrowhead Stadium', 'distance': '1084.81'},
    'Dallas Cowboys': {'venue': 'AT&T Stadium', 'distance': '1384.49'},
    'Carolina Panthers': {'venue': 'Bank of America Stadium', 'distance': '533.67'},
    'New Orleans Saints': {'venue': 'Caesars Superdome', 'distance': '1169.6'},
    'Denver Broncos': {'venue': 'Empower Field at Mile High', 'distance': '1623.2'},
    'Washington Commanders': {'venue': 'FedExField', 'distance': '199.89'},
    'Cleveland Browns': {'venue': 'FirstEnergy Stadium', 'distance': '398.23'},
    'Detroit Lions': {'venue': 'Ford Field', 'distance': '474.07'},
    'New England Patriots': {'venue': 'Gillette Stadium', 'distance': '170.5'},
    'Miami Dolphins': {'venue': 'Hard Rock Stadium', 'distance': '1087.01'},
    'Buffalo Bills': {'venue': 'Highmark Stadium', 'distance': '276.52'},
    'Green Bay Packers': {'venue': 'Lambeau Field', 'distance': '752.46'},
    'San Francisco 49ers': {'venue': "Levi's Stadium", 'distance': '2545.49'},
    'Philadelphia Eagles': {'venue': 'Lincoln Financial Field', 'distance': '81.82'},
    'Indianapolis Colts': {'venue': 'Lucas Oil Stadium', 'distance': '639.76'},
    'Seattle Seahawks': {'venue': 'Lumen Field', 'distance': '2394.2'},
    'Baltimore Ravens': {'venue': 'M&T Bank Stadium', 'distance': '171.39'},
    'Atlanta Falcons': {'venue': 'Mercedes-Benz Stadium', 'distance': '747.35'},
    'New York Giants': {'venue': 'MetLife Stadium', 'distance': '0'},
    'New York Jets': {'venue': 'MetLife Stadium', 'distance': '0'},
    'Tennessee Titans': {'venue': 'Nissan Stadium', 'distance': '756.56'},
    'Houston Texans': {'venue': 'NRG Stadium', 'distance': '1421.72'},
    'Cincinnati Bengals': {'venue': 'Paycor Stadium', 'distance': '563.45'},
    'Tampa Bay Buccaneers': {'venue': 'Raymond James Stadium', 'distance': '998.2'},
    'Los Angeles Rams': {'venue': 'SoFi Stadium', 'distance': '2448.1'},
    'Los Angeles Chargers': {'venue': 'SoFi Stadium', 'distance': '2448.1'},
    'Chicago Bears': {'venue': 'Soldier Field', 'distance': '704.37'},
    'Arizona Cardinals': {'venue': 'State Farm Stadium', 'distance': '2142.88'},
    'Jacksonville Jaguars': {'venue': 'TIAA Bank Field', 'distance': '841.57'},
    'Minnesota Vikings': {'venue': 'U.S. Bank Stadium', 'distance': '1008.66'},
    'London': {'venue':'Tottenham Hotspur Stadium', 'distance': '3460.09'},
    'London2':	{'venue':"Wembley Stadium", 'distance':"3452.49"},
    'Munich':	{'venue':"Allianz Arena",'distance':"4029.54"},	
    'Mexico City': {'venue':"Estadio Azteca",'distance':"2096.26"} 		
    }

# week, Away, Home
schedule = [
    ['1', 'Buffalo Bills', 'Los Angeles Rams'],
    ['1', 'Cleveland Browns', 'Carolina Panthers'],
    ['1', 'Chicago Bears', 'San Francisco 49ers'],
    ['1', 'Pittsburgh Steelers', 'Cincinnati Bengals'],
    ['1', 'Houston Texans', 'Indianapolis Colts'],
    ['1', 'New Orleans Saints', 'Atlanta Falcons'],
    ['1', 'Baltimore Ravens', 'New York Jets'],
    ['1', 'Philadelphia Eagles', 'Detroit Lions'],
    ['1', 'Miami Dolphins', 'New England Patriots'],
    ['1', 'Washington Commanders', 'Jacksonville Jaguars'],
    ['1', 'Los Angeles Chargers', 'Las Vegas Raiders'],
    ['1', 'New York Giants', 'Tennessee Titans'],
    ['1', 'Minnesota Vikings', 'Green Bay Packers'],
    ['1', 'Kansas City Chiefs', 'Arizona Cardinals'],
    ['1', 'Tampa Bay Buccaneers', 'Dallas Cowboys'],
    ['1', 'Seattle Seahawks', 'Denver Broncos'],
    ['2', 'Kansas City Chiefs', 'Los Angeles Chargers'],
    ['2', 'Carolina Panthers', 'New York Giants'],
    ['2', 'Indianapolis Colts', 'Jacksonville Jaguars'],
    ['2', 'Miami Dolphins', 'Baltimore Ravens'],
    ['2', 'New England Patriots', 'Pittsburgh Steelers'],
    ['2', 'New York Jets', 'Cleveland Browns'],
    ['2', 'Tampa Bay Buccaneers', 'New Orleans Saints'],
    ['2', 'Washington Commanders', 'Detroit Lions'],
    ['2', 'Atlanta Falcons', 'Los Angeles Rams'],
    ['2', 'Seattle Seahawks', 'San Francisco 49ers'],
    ['2', 'Cincinnati Bengals', 'Dallas Cowboys'],
    ['2', 'Arizona Cardinals', 'Las Vegas Raiders'],
    ['2', 'Houston Texans', 'Denver Broncos'],
    ['2', 'Chicago Bears', 'Green Bay Packers'],
    ['2', 'Tennessee Titans', 'Buffalo Bills'],
    ['2', 'Minnesota Vikings', 'Philadelphia Eagles'],
    ['3', 'Pittsburgh Steelers', 'Cleveland Browns'],
    ['3', 'Buffalo Bills', 'Miami Dolphins'],
    ['3', 'Cincinnati Bengals', 'New York Jets'],
    ['3', 'Detroit Lions', 'Minnesota Vikings'],
    ['3', 'Houston Texans', 'Chicago Bears'],
    ['3', 'Kansas City Chiefs', 'Indianapolis Colts'],
    ['3', 'New Orleans Saints', 'Carolina Panthers'],
    ['3', 'Philadelphia Eagles', 'Washington Commanders'],
    ['3', 'Las Vegas Raiders', 'Tennessee Titans'],
    ['3', 'Baltimore Ravens', 'New England Patriots'],
    ['3', 'Jacksonville Jaguars', 'Los Angeles Chargers'],
    ['3', 'Atlanta Falcons', 'Seattle Seahawks'],
    ['3', 'Green Bay Packers', 'Tampa Bay Buccaneers'],
    ['3', 'Los Angeles Rams', 'Arizona Cardinals'],
    ['3', 'San Francisco 49ers', 'Denver Broncos'],
    ['3', 'Dallas Cowboys', 'New York Giants'],
    ['4', 'Miami Dolphins', 'Cincinnati Bengals'],
    ['4', 'Minnesota Vikings', 'New Orleans Saints'],
    ['4', 'Buffalo Bills', 'Baltimore Ravens'],
    ['4', 'Chicago Bears', 'New York Giants'],
    ['4', 'Cleveland Browns', 'Atlanta Falcons'],
    ['4', 'Jacksonville Jaguars', 'Philadelphia Eagles'],
    ['4', 'New York Jets', 'Pittsburgh Steelers'],
    ['4', 'Tennessee Titans', 'Indianapolis Colts'],
    ['4', 'Los Angeles Chargers', 'Houston Texans'],
    ['4', 'Seattle Seahawks', 'Detroit Lions'],
    ['4', 'Washington Commanders', 'Dallas Cowboys'],
    ['4', 'Arizona Cardinals', 'Carolina Panthers'],
    ['4', 'Denver Broncos', 'Las Vegas Raiders'],
    ['4', 'New England Patriots', 'Green Bay Packers'],
    ['4', 'Kansas City Chiefs', 'Tampa Bay Buccaneers'],
    ['4', 'Los Angeles Rams', 'San Francisco 49ers'],
    ['5', 'Indianapolis Colts', 'Denver Broncos'],
    ['5', 'New York Giants', 'Green Bay Packers'],
    ['5', 'Atlanta Falcons', 'Tampa Bay Buccaneers'],
    ['5', 'Chicago Bears', 'Minnesota Vikings'],
    ['5', 'Detroit Lions', 'New England Patriots'],
    ['5', 'Houston Texans', 'Jacksonville Jaguars'],
    ['5', 'Miami Dolphins', 'New York Jets'],
    ['5', 'Tennessee Titans', 'Washington Commanders'],
    ['5', 'Pittsburgh Steelers', 'Buffalo Bills'],
    ['5', 'Los Angeles Chargers', 'Cleveland Browns'],
    ['5', 'Seattle Seahawks', 'New Orleans Saints'],
    ['5', 'San Francisco 49ers', 'Carolina Panthers'],
    ['5', 'Dallas Cowboys', 'Los Angeles Rams'],
    ['5', 'Philadelphia Eagles', 'Arizona Cardinals'],
    ['5', 'Cincinnati Bengals', 'Baltimore Ravens'],
    ['5', 'Las Vegas Raiders', 'Kansas City Chiefs'],
    ['6', 'Washington Commanders', 'Chicago Bears'],
    ['6', 'Cincinnati Bengals', 'New Orleans Saints'],
    ['6', 'Jacksonville Jaguars', 'Indianapolis Colts'],
    ['6', 'Minnesota Vikings', 'Miami Dolphins'],
    ['6', 'New England Patriots', 'Cleveland Browns'],
    ['6', 'New York Jets', 'Green Bay Packers'],
    ['6', 'Baltimore Ravens', 'New York Giants'],
    ['6', 'San Francisco 49ers', 'Atlanta Falcons'],
    ['6', 'Tampa Bay Buccaneers', 'Pittsburgh Steelers'],
    ['6', 'Carolina Panthers', 'Los Angeles Rams'],
    ['6', 'Arizona Cardinals', 'Seattle Seahawks'],
    ['6', 'Buffalo Bills', 'Kansas City Chiefs'],
    ['6', 'Dallas Cowboys', 'Philadelphia Eagles'],
    ['6', 'Denver Broncos', 'Los Angeles Chargers'],
    ['7', 'New Orleans Saints', 'Arizona Cardinals'],
    ['7', 'Atlanta Falcons', 'Cincinnati Bengals'],
    ['7', 'Cleveland Browns', 'Baltimore Ravens'],
    ['7', 'Indianapolis Colts', 'Tennessee Titans'],
    ['7', 'Detroit Lions', 'Dallas Cowboys'],
    ['7', 'Green Bay Packers', 'Washington Commanders'],
    ['7', 'New York Giants', 'Jacksonville Jaguars'],
    ['7', 'Tampa Bay Buccaneers', 'Carolina Panthers'],
    ['7', 'Houston Texans', 'Las Vegas Raiders'],
    ['7', 'New York Jets', 'Denver Broncos'],
    ['7', 'Kansas City Chiefs', 'San Francisco 49ers'],
    ['7', 'Seattle Seahawks', 'Los Angeles Chargers'],
    ['7', 'Pittsburgh Steelers', 'Miami Dolphins'],
    ['7', 'Chicago Bears', 'New England Patriots'],
    ['8', 'Baltimore Ravens', 'Tampa Bay Buccaneers'],
    ['8', 'Denver Broncos', 'Jacksonville Jaguars'],
    ['8', 'Carolina Panthers', 'Atlanta Falcons'],
    ['8', 'Chicago Bears', 'Dallas Cowboys'],
    ['8', 'Arizona Cardinals', 'Minnesota Vikings'],
    ['8', 'Miami Dolphins', 'Detroit Lions'],
    ['8', 'New England Patriots', 'New York Jets'],
    ['8', 'Pittsburgh Steelers', 'Philadelphia Eagles'],
    ['8', 'Las Vegas Raiders', 'New Orleans Saints'],
    ['8', 'Tennessee Titans', 'Houston Texans'],
    ['8', 'New York Giants', 'Seattle Seahawks'],
    ['8', 'San Francisco 49ers', 'Los Angeles Rams'],
    ['8', 'Washington Commanders', 'Indianapolis Colts'],
    ['8', 'Green Bay Packers', 'Buffalo Bills'],
    ['8', 'Cincinnati Bengals', 'Cleveland Browns'],
    ['9', 'Philadelphia Eagles', 'Houston Texans'],
    ['9', 'Buffalo Bills', 'New York Jets'],
    ['9', 'Carolina Panthers', 'Cincinnati Bengals'],
    ['9', 'Indianapolis Colts', 'New England Patriots'],
    ['9', 'Green Bay Packers', 'Detroit Lions'],
    ['9', 'Miami Dolphins', 'Chicago Bears'],
    ['9', 'Minnesota Vikings', 'Washington Commanders'],
    ['9', 'Las Vegas Raiders', 'Jacksonville Jaguars'],
    ['9', 'Los Angeles Chargers', 'Atlanta Falcons'],
    ['9', 'Seattle Seahawks', 'Arizona Cardinals'],
    ['9', 'Los Angeles Rams', 'Tampa Bay Buccaneers'],
    ['9', 'Tennessee Titans', 'Kansas City Chiefs'],
    ['9', 'Baltimore Ravens', 'New Orleans Saints'],
    ['10', 'Atlanta Falcons', 'Carolina Panthers'],
    ['10', 'Seattle Seahawks', 'Tampa Bay Buccaneers'],
    ['10', 'Cleveland Browns', 'Miami Dolphins'],
    ['10', 'Denver Broncos', 'Tennessee Titans'],
    ['10', 'Detroit Lions', 'Chicago Bears'],
    ['10', 'Houston Texans', 'New York Giants'],
    ['10', 'Jacksonville Jaguars', 'Kansas City Chiefs'],
    ['10', 'Minnesota Vikings', 'Buffalo Bills'],
    ['10', 'New Orleans Saints', 'Pittsburgh Steelers'],
    ['10', 'Indianapolis Colts', 'Las Vegas Raiders'],
    ['10', 'Arizona Cardinals', 'Los Angeles Rams'],
    ['10', 'Dallas Cowboys', 'Green Bay Packers'],
    ['10', 'Los Angeles Chargers', 'San Francisco 49ers'],
    ['10', 'Washington Commanders', 'Philadelphia Eagles'],
    ['11', 'Tennessee Titans', 'Green Bay Packers'],
    ['11', 'Carolina Panthers', 'Baltimore Ravens'],
    ['11', 'Chicago Bears', 'Atlanta Falcons'],
    ['11', 'Cleveland Browns', 'Buffalo Bills'],
    ['11', 'Detroit Lions', 'New York Giants'],
    ['11', 'New York Jets', 'New England Patriots'],
    ['11', 'Philadelphia Eagles', 'Indianapolis Colts'],
    ['11', 'Los Angeles Rams', 'New Orleans Saints'],
    ['11', 'Washington Commanders', 'Houston Texans'],
    ['11', 'Las Vegas Raiders', 'Denver Broncos'],
    ['11', 'Dallas Cowboys', 'Minnesota Vikings'],
    ['11', 'Kansas City Chiefs', 'Los Angeles Chargers'],
    ['11', 'Cincinnati Bengals', 'Pittsburgh Steelers'],
    ['11', 'San Francisco 49ers', 'Arizona Cardinals'],
    ['12', 'Buffalo Bills', 'Detroit Lions'],
    ['12', 'New York Giants', 'Dallas Cowboys'],
    ['12', 'New England Patriots', 'Minnesota Vikings'],
    ['12', 'Atlanta Falcons', 'Washington Commanders'],
    ['12', 'Chicago Bears', 'New York Jets'],
    ['12', 'Cincinnati Bengals', 'Tennessee Titans'],
    ['12', 'Denver Broncos', 'Carolina Panthers'],
    ['12', 'Houston Texans', 'Miami Dolphins'],
    ['12', 'Baltimore Ravens', 'Jacksonville Jaguars'],
    ['12', 'Tampa Bay Buccaneers', 'Cleveland Browns'],
    ['12', 'Las Vegas Raiders', 'Seattle Seahawks'],
    ['12', 'Los Angeles Chargers', 'Arizona Cardinals'],
    ['12', 'New Orleans Saints', 'San Francisco 49ers'],
    ['12', 'Los Angeles Rams', 'Kansas City Chiefs'],
    ['12', 'Green Bay Packers', 'Philadelphia Eagles'],
    ['12', 'Pittsburgh Steelers', 'Indianapolis Colts'],
    ['13', 'Buffalo Bills', 'New England Patriots'],
    ['13', 'Cleveland Browns', 'Houston Texans'],
    ['13', 'Denver Broncos', 'Baltimore Ravens'],
    ['13', 'Green Bay Packers', 'Chicago Bears'],
    ['13', 'Jacksonville Jaguars', 'Detroit Lions'],
    ['13', 'New York Jets', 'Minnesota Vikings'],
    ['13', 'Tennessee Titans', 'Philadelphia Eagles'],
    ['13', 'Pittsburgh Steelers', 'Atlanta Falcons'],
    ['13', 'Washington Commanders', 'New York Giants'],
    ['13', 'Miami Dolphins', 'San Francisco 49ers'],
    ['13', 'Seattle Seahawks', 'Los Angeles Rams'],
    ['13', 'Kansas City Chiefs', 'Cincinnati Bengals'],
    ['13', 'Los Angeles Chargers', 'Las Vegas Raiders'],
    ['13', 'Indianapolis Colts', 'Dallas Cowboys'],
    ['13', 'New Orleans Saints', 'Tampa Bay Buccaneers'],
    ['14', 'Las Vegas Raiders', 'Los Angeles Rams'],
    ['14', 'Cleveland Browns', 'Cincinnati Bengals'],
    ['14', 'Houston Texans', 'Dallas Cowboys'],
    ['14', 'Jacksonville Jaguars', 'Tennessee Titans'],
    ['14', 'Minnesota Vikings', 'Detroit Lions'],
    ['14', 'New York Jets', 'Buffalo Bills'],
    ['14', 'Philadelphia Eagles', 'New York Giants'],
    ['14', 'Baltimore Ravens', 'Pittsburgh Steelers'],
    ['14', 'Miami Dolphins', 'Los Angeles Chargers'],
    ['14', 'Carolina Panthers', 'Seattle Seahawks'],
    ['14', 'Tampa Bay Buccaneers', 'San Francisco 49ers'],
    ['14', 'Kansas City Chiefs', 'Denver Broncos'],
    ['14', 'New England Patriots', 'Arizona Cardinals'],
    ['15', 'San Francisco 49ers', 'Seattle Seahawks'],
    ['15', 'Atlanta Falcons', 'New Orleans Saints'],
    ['15', 'Indianapolis Colts', 'Minnesota Vikings'],
    ['15', 'Dallas Cowboys', 'Jacksonville Jaguars'],
    ['15', 'Detroit Lions', 'New York Jets'],
    ['15', 'Kansas City Chiefs', 'Houston Texans'],
    ['15', 'Miami Dolphins', 'Buffalo Bills'],
    ['15', 'New York Giants', 'Washington Commanders'],
    ['15', 'Philadelphia Eagles', 'Chicago Bears'],
    ['15', 'Pittsburgh Steelers', 'Carolina Panthers'],
    ['15', 'Baltimore Ravens', 'Cleveland Browns'],
    ['15', 'Arizona Cardinals', 'Denver Broncos'],
    ['15', 'Cincinnati Bengals', 'Tampa Bay Buccaneers'],
    ['15', 'Tennessee Titans', 'Los Angeles Chargers'],
    ['15', 'New England Patriots', 'Las Vegas Raiders'],
    ['15', 'Los Angeles Rams', 'Green Bay Packers'],
    ['16', 'Jacksonville Jaguars', 'New York Jets'],
    ['16', 'Atlanta Falcons', 'Baltimore Ravens'],
    ['16', 'Buffalo Bills', 'Chicago Bears'],
    ['16', 'Cincinnati Bengals', 'New England Patriots'],
    ['16', 'Detroit Lions', 'Carolina Panthers'],
    ['16', 'Houston Texans', 'Tennessee Titans'],
    ['16', 'New Orleans Saints', 'Cleveland Browns'],
    ['16', 'New York Giants', 'Minnesota Vikings'],
    ['16', 'Seattle Seahawks', 'Kansas City Chiefs'],
    ['16', 'Washington Commanders', 'San Francisco 49ers'],
    ['16', 'Philadelphia Eagles', 'Dallas Cowboys'],
    ['16', 'Las Vegas Raiders', 'Pittsburgh Steelers'],
    ['16', 'Green Bay Packers', 'Miami Dolphins'],
    ['16', 'Denver Broncos', 'Los Angeles Rams'],
    ['16', 'Tampa Bay Buccaneers', 'Arizona Cardinals'],
    ['16', 'Los Angeles Chargers', 'Indianapolis Colts'],
    ['17', 'Dallas Cowboys', 'Tennessee Titans'],
    ['17', 'Carolina Panthers', 'Tampa Bay Buccaneers'],
    ['17', 'Chicago Bears', 'Detroit Lions'],
    ['17', 'Cleveland Browns', 'Washington Commanders'],
    ['17', 'Indianapolis Colts', 'New York Giants'],
    ['17', 'Arizona Cardinals', 'Atlanta Falcons'],
    ['17', 'Denver Broncos', 'Kansas City Chiefs'],
    ['17', 'Jacksonville Jaguars', 'Houston Texans'],
    ['17', 'Miami Dolphins', 'New England Patriots'],
    ['17', 'New Orleans Saints', 'Philadelphia Eagles'],
    ['17', 'Pittsburgh Steelers', 'Baltimore Ravens'],
    ['17', 'New York Jets', 'Seattle Seahawks'],
    ['17', 'San Francisco 49ers', 'Las Vegas Raiders'],
    ['17', 'Minnesota Vikings', 'Green Bay Packers'],
    ['17', 'Los Angeles Rams', 'Los Angeles Chargers'],
    ['17', 'Buffalo Bills', 'Cincinnati Bengals'],
    ['18', 'Carolina Panthers', 'New Orleans Saints'],
    ['18', 'Cleveland Browns', 'Pittsburgh Steelers'],
    ['18', 'Arizona Cardinals', 'San Francisco 49ers'],
    ['18', 'Dallas Cowboys', 'Washington Commanders'],
    ['18', 'Detroit Lions', 'Green Bay Packers'],
    ['18', 'Houston Texans', 'Indianapolis Colts'],
    ['18', 'Kansas City Chiefs', 'Las Vegas Raiders'],
    ['18', 'Minnesota Vikings', 'Chicago Bears'],
    ['18', 'New England Patriots', 'Buffalo Bills'],
    ['18', 'New York Giants', 'Philadelphia Eagles'],
    ['18', 'New York Jets', 'Miami Dolphins'],
    ['18', 'Tennessee Titans', 'Jacksonville Jaguars'],
    ['18', 'Los Angeles Rams', 'Seattle Seahawks'],
    ['18', 'Baltimore Ravens', 'Cincinnati Bengals'],
    ['18', 'Los Angeles Chargers', 'Denver Broncos'],
    ['18', 'Tampa Bay Buccaneers', 'Atlanta Falcons']
]