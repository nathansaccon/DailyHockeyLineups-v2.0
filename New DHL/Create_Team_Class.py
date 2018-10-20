# Create Team Class
import pickle, requests
from Classes import Team
from bs4 import BeautifulSoup

readTeam_Times = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Start_Times.txt", "r")
readTeam_Times = eval(readTeam_Times.read())

readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

all_team_times = readTeam_Times
all_teams = list(map(lambda x: x[0],readTeam_Times)) + list(map(lambda x: x[1],readTeam_Times))

TEST = True
if TEST:
    print("Test ON for Create_Team_Class.py")

def Team_Name_Fix(name):
    if name == "LA":
        return "LAK"
    if name == "NJ":
        return "NJD"
    if name == "SJ":
        return "SJS"
    if name == "CLS":
        return "CBJ"
    if name == "TB":
        return "TBL"
    if name == "WAS":
        return "WSH"
    if name == "MON":
        return "MTL"
    if name == "ANH":
        return "ANA"
    else:
        return name


def Create_Team():
    all_team_classes = []
    for team in all_teams:
        tm = Team()
        tm.name = Team_Name_Fix(team)
        for game in all_team_times:
            if team in game:
                tm.start_time = game[2]
                if team == game[0]:
                    tm.opponent = Team_Name_Fix(game[1])
                else:
                    tm.opponent = Team_Name_Fix(game[0])
        for gol in all_goalies:
            if team == gol.team:
                tm.arena = gol.arena

        url_1 = "http://www.hockey-reference.com/teams/%s/2018_games.html" % (tm.name)

        try:
            team_gamelog = requests.get(url_1)
            team_gamelog = BeautifulSoup(team_gamelog.content, "html.parser")
        except:
            print("\nTEAM STATS ERROR: Gamelog\n")

        gamelog = []

        for line in team_gamelog.find_all("tr"):
            line = str(line)
            not_played = line.split(">")[16].split("<")[0] # AKA Goals For
            if "date_game" in line and "thead" not in line and "aria-label" not in line and not_played != "":
                # Arena
                arena = line.split(">")[10].split("<")[0]
                if arena == "@":
                    arena = "Away"
                else:
                    arena = "Home"
                # Goals For
                goals_for = int(line.split(">")[16].split("<")[0])
                # Goals Against
                goals_against = int(line.split(">")[18].split("<")[0])
                # Outcome (Win/Loss)
                outcome = line.split(">")[20].split("<")[0]
                if outcome == "W":
                    outcome = 1
                else:
                    outcome = 0
                # Shots For
                shots_for = int(line.split(">")[34].split("<")[0])
                # Penalty Minutes For
                pim_for = int(line.split(">")[36].split("<")[0])
                # Powerplay Percent
                pp_chances = int(line.split(">")[40].split("<")[0])
                pp_goals = int(line.split(">")[38].split("<")[0])
                if pp_chances != 0:
                    pp_percent = round(pp_goals / pp_chances * 100,2)
                else:
                    pp_percent = 0
                # Shots Against
                shots_against = int(line.split(">")[46].split("<")[0])
                # Penatly Minutes Against
                pim_against = int(line.split(">")[48].split("<")[0])
                # Penalty Kill Percent
                pk_chances = int(line.split(">")[52].split("<")[0])
                pk_goals_against = int(line.split(">")[50].split("<")[0])
                if pk_chances != 0:
                    pk_percent = 100 - round(pk_goals_against / pk_chances *100,2)
                else:
                    pk_percent = 100

                gamelog.append([arena, goals_for, goals_against, outcome, shots_for, pim_for, pp_percent, shots_against, pim_against, pk_percent])

        tm.game_log = gamelog
        if TEST:
            print(tm.name, gamelog)


        url_2 = "http://www.hockey-reference.com/play-index/tpbp_finder.cgi?request=1&match=single&year_min=2018&year_max=2017&situation_id=5on5&order_by=corsi_for"

        try:
            team_advanced = requests.get(url_2)
            team_advanced = BeautifulSoup(team_advanced.content, "html.parser")
        except:
            print("\nTEAM STATS ERROR: Advanced Stats\n")

        table = team_advanced.find_all(id="stats")
        table = str(table).split("<tr")

        for line in table:
            line = str(line)
            try:
                web_team = line.split(">")[4].split("<")[0]
            except:
                continue
            if web_team == Team_Name_Fix(team):
                line = line.split(">")
                # Corsi For %
                corsi_for = float(line[14].split("<")[0])
                # Fenwick For %
                fenwick_for = float(line[20].split("<")[0])
                # PDO
                pdo = float(line[26].split("<")[0])
                # Offensive Zone Start
                ozs = float(line[28].split("<")[0])

                tm.corsi_for = corsi_for
                tm.fenwick_for = fenwick_for
                tm.pdo = pdo
                tm.ozs = ozs
                if TEST:
                    print(tm.name, corsi_for, fenwick_for, pdo, ozs)
                all_team_classes.append(tm)



    teamFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "wb")
    pickle.dump(all_team_classes, teamFile)
    teamFile.close()
