# General Functions

import pickle, requests
from bs4 import BeautifulSoup

# All Teams
Anaheim = ["Anaheim Ducks", "Anaheim", "ducks", "ANA", "Anh", "ANH"]
Arizona = ["Arizona Coyotes", "Arizona", "coyotes", "PHX", "AR", "ARZ", "Ari", "ARI"]
Boston = ["Boston Bruins", "Boston", "bruins", "BOS", "Bos"]
Buffalo = ["Buffalo Sabres", "Buffalo", "sabres", "BUF", "Buf"]
Calgary = ["Calgary Flames", "Calgary", "flames", "CGY", "CAL", "Cgy"]
Carolina = ["Carolina Hurricanes", "Carolina", "hurricanes", "CAR", "Car"]
Chicago = ["Chicago Blackhawks", "Chicago", "blackhawks", "CHI", "Chi"]
Colorado = ["Colorado Avalanche", "Colorado", "avalanche",  "COL", "Col"]
Columbus = ["Columbus Blue Jackets", "Cls", "Columbus", "blue-jackets", "CBJ" "Cls", "CLS", "CBJ"]
Dallas = ["Dallas Stars", "Dallas", "stars", "DAL", "Dal"]
Detroit = ["Detroit Red Wings", "Detroit", "red-wings", "DET", "Det"]
Edmonton = ["Edmonton Oilers", "Edmonton", "oilers", "EDM", "Edm"]
Florida = ["Florida Panthers", "Florida", "panthers", "FLA", "Fla"]
Los_Angeles = ["Los Angeles Kings", "Los Angeles", "kings", "LA", "LAK"]
Minnesota = ["Minnesota Wild", "Minnesota", "wild", "MIN", "Min"]
Montreal = ["Montreal Canadiens", "Montreal", "canadiens", "MTL", "MON", "Mon"]
Nashville = ["Nashville Predators", "Nashville", "predators", "NAS", "NSH", "Nsh"]
New_Jersey = ["New Jersey Devils", "New Jersey", "devils", "NJD", "NJ"]
New_York_I = ["New York Islanders", "NYI", "islanders"]
New_York_R = ["New York Rangers", "NYR", "rangers", "nyr", "Rangers"]
Ottawa = ["Ottawa Senators", "Ottawa", "senators", "OTT", "Ott"]
Philadelphia = ["Philadelphia Flyers", "Philadelphia", "flyers", "PHI", "Phi"]
Pittsburgh = ["Pittsburgh Penguins", "Pittsburgh", "penguins", "PIT", "Pit"]
San_Jose = ["San Jose Sharks", "San Jose", "sharks", "SJ", "SJS"]
St_Louis = ["St Louis Blues", "St Louis", "blues", "STL", "StL", "Stl", "St. Louis Blues"]
Tampa_Bay = ["Tampa Bay Lightning", "Tampa Bay", "lightning", "TB", "TBL", "Tbl"]
Toronto = ["Toronto Maple Leafs", "Toronto", "leafs", "TOR", "TML", "Tor"]
Vancouver = ["Vancouver Canucks", "Vancouver", "canucks", "VAN", "Van"]
Washington = ["Washington Capitals", "Washington", "capitals", "WAS", "WSH", "Was"]
Winnipeg = ["Winnipeg Jets", "Winnipeg", "jets", "WIN", "WPG", "Wpg"]
Vegas = []
All_Teams = [Anaheim, Arizona, Boston, Buffalo, Calgary, Carolina, Chicago, Colorado, Columbus, Dallas,
             Detroit, Edmonton, Florida, Los_Angeles, Minnesota, Montreal, Nashville, New_Jersey,
             New_York_I, New_York_R, Ottawa, Philadelphia, Pittsburgh, San_Jose, St_Louis, Tampa_Bay,
             Toronto, Vancouver, Washington, Winnipeg]

# Checks if the two teams are the same
# str, str -> Bool
def team_equal(team1, team2):
    team_equal = False
    for team in All_Teams:
        if team1 in team and team2 in team:
            team_equal = True
    return team_equal

# Returns a team's full name
def Team_Full_Name(abv):
    for team in All_Teams:
        if abv in team:
            return team[0]


# Writes a file with all teams and their start time
def Write_Start_Time_File():
    readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
    all_goalies = pickle.load(readGoalies)

    start_times = list(map(lambda x: [x.team, x.opponent, x.start_time], all_goalies))
    unique_times = []
    teams_accounted = []
    for game in start_times:
        if game[0] not in teams_accounted:
            unique_times += [game]
            teams_accounted += [game[0]]
            teams_accounted += [game[1]]
        else:
            pass
    startTimeFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Start_Times.txt", "w")
    startTimeFile.write(str(unique_times))
    startTimeFile.close()

# Function to convert team to start time
def Team_to_Time(team):
    startTimeFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Start_Times.txt", "r")
    times = eval(startTimeFile.read())
    for game in times:
        if team_equal(team, game[0]) or team_equal(team, game[1]):
            return game[2]
    return "Invalid Team: Team Not Playing"

# Writes a file containing a list of all injured players
def Injured_Players():
    injuries_page = requests.get("http://www.rotoworld.com/teams/injuries/nhl/all/")
    injuries_page = BeautifulSoup(injuries_page.content, "html.parser")

    injured_players = []

    for line in injuries_page.find_all("td"):
        if "/player/nhl/" in str(line):
            name = str(line).split(">")[2]
            name = name.split("<")[0]
            injured_players.append(name)

    injuredFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "w")
    injuredFile.write(str(injured_players))
    injuredFile.close()


#Writes a file with a list of all the starting goalies.
def Write_Starting_Goalies():
    starting_goalies = []
    multi_day = str(input("Multi Day Contests y/n?: "))

    date = str(input("Enter Contest Date As (m)m-dd: "))
    if multi_day == "y":
        date2 = str(input("Enter Contest Date #2 As (m)m-dd: "))

    url_1 = "http://www.chirphockey.com/nhl-starting-goalies/%s-2017/" %(date)
    url_tries = 5
    while url_tries > 0:
        try:
            starters_page_1 = requests.get(url_1)
            starters_page_1 = BeautifulSoup(starters_page_1.content, "html.parser")
            url_tries = 0
        except:
            url_tries -= 1
            continue

    for line in starters_page_1.find_all("g1"):
        line = str(line)
        name = line.split(">")[1].split("<")[0]
        starting_goalies.append(name)

    if multi_day == "n":
        startingGoaliesFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "w")
        startingGoaliesFile.write(str(starting_goalies))
        startingGoaliesFile.close()

    if multi_day == "y":
        url_2 = "http://www.chirphockey.com/nhl-starting-goalies/%s-2017/" %(date2)
        url_tries = 5
        while url_tries > 0:
            try:
                starters_page_1 = requests.get(url_2)
                starters_page_1 = BeautifulSoup(starters_page_1.content, "html.parser")
                url_tries = 0
            except:
                url_tries -= 1
                continue

        for line in starters_page_1.find_all("g1"):
            line = str(line)
            name = line.split(">")[1].split("<")[0]
            starting_goalies.append(name)

        startingGoaliesFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "w")
        startingGoaliesFile.write(str(starting_goalies))
        startingGoaliesFile.close()



