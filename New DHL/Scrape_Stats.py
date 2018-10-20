# Scrape Player Stats

import pickle, requests
from bs4 import BeautifulSoup
from General_Functions import team_equal

TEST = True

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)

if TEST:
    print("Test ON for Scrape Stats.py")
    plr = all_skaters[0]

def HR_Name_Fix(name):
    if name == "Alex Burmistrov":
        return "Alexander Burmistrov"
    if name == "Alexander Steen":
        return "Alex Steen"
    if name == "Michael Cammalleri":
        return "Mike Cammalleri"
    if name == "Pierre-Alexandre Parenteau":
        return "P.A. Parenteau"
    if name == "Matt Dumba":
        return "Mathew Dumba"
    if name == "Christopher Tanev":
        return "Chris Tanev"
    if name == "Jonathan Marchessault":
        return "Jon Marchessault"
    if name == "Matt Nieto":
        return "Matthew Nieto"
    if name == "Joe Morrow":
        return "Joseph Morrow"
    if name == "Nikolay Kulemin":
        return "Nikolai Kulemin"
    if name == "Michael Kostka":
        return "Mike Kostka"
    if name == "Jon Merrill":
        return "Jonathon Merrill"
    if name == "Matthew Carle":
        return "Matt Carle"
    if name == "Mitchell Marner":
        return "Mitch Marner"
    if name == "Zach Sanford":
        return "Zachary Sanford"
    if name == "Jake DeBrusk":
        return "Jake Debrusk"
    if name == "Steve Oleksy":
        return "Steven Oleksy"
    if name == "Paul LaDue":
        return "Paul Ladue"
    if name == "Griffen Molino":
        return "Griffin Molino"
    else:
        return name

def HR_Scrape_Gamelogs(skater):
    url_number = 1
    right_num = False

    # Special Cases
    if skater.name in ["Erik Gustafsson" ,"Taylor Hall", "Mike Hoffman", "Johan Larsson", "Joakim Nordstrom"]:
        url_number = 2
    if skater.name in ["Mike Green"]:
        url_number = 3
    #-------------

    while (not right_num) and url_number < 10:
        url = "http://www.hockey-reference.com/players%s/gamelog/2017" % (skater.HR_URL() + str(url_number))
        try:
            skater_page = requests.get(url)
            skater_page = BeautifulSoup(skater_page.content, "html.parser")
            page_name = str(skater_page.find_all("h1")).split(">")[1].split("<")[0]
            if page_name == HR_Name_Fix(skater.name):
                right_num = True
            else:
                url_number += 1
                if TEST:
                    print(skater.name + " is not " + page_name)
                continue
        except:
            print(skater.name + " GAMELOG PAGE ERROR")
            continue
    if TEST:
        print(skater.name + "'s URL number:", url_number)

    # Games
    game_logs = []

    for line in skater_page.find_all("tr"):
        line = str(line)
        if "gamelog" in line:
            line = line.split(">")
            # Arena
            if line[16].split("<")[0] == "@":
                arena = "Away"
            else:
                arena = "Home"
            # Goals
            goals = line[24].split("<")[0]
            if goals == "":
                goals = 0
            else:
                goals = int(goals)
            # Assists
            assists = line[26].split("<")[0]
            if assists == "":
                assists = 0
            else:
                assists = int(assists)
            # Shots
            shots_on_goal = line[48].split("<")[0]
            if shots_on_goal == "":
                shots_on_goal = 0
            else:
                shots_on_goal = int(shots_on_goal)
            # Blocks
            blocks = line[58].split("<")[0]
            if blocks == "":
                blocks = 0
            else:
                blocks = int(blocks)
            # PP Goals
            pp_goals = line[36].split("<")[0]
            if pp_goals == "":
                pp_goals = 0
            else:
                pp_goals = int(pp_goals)
            # PP Assists
            pp_assists = line[44].split("<")[0]
            if pp_assists == "":
                pp_assists = 0
            else: pp_assists = int(pp_assists)

            game = [arena, goals, assists, shots_on_goal, blocks, pp_goals, pp_assists]
            game_logs.append(game)

    skater.game_log = game_logs
    skater.url_num = url_number
    if TEST:
        print(skater.game_log)



def Write_Gamelog_Update():
    for skater in all_skaters:
        try_number = 0
        while try_number <= 5:
            try:
                HR_Scrape_Gamelogs(skater)
                break
            except:
                continue

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()


def HR_Scrape_Splits(skater):
    url = "http://www.hockey-reference.com/players%s/splits/" % (skater.HR_URL() + str(skater.url_num))
    try_number = 0
    while try_number <= 5:
        try:
            skater_page = requests.get(url)
            skater_page = BeautifulSoup(skater_page.content, "html.parser")
            break
        except:
            print(skater.name + "SPLITS PAGE ERROR")

    for line in skater_page.find_all("tr"):
        line = str(line)
        if "/teams/" in line:
            team = line.split(">")[5].split("<")[0]
            if team_equal(team, skater.opponent):
                # Games Played vs Opponent
                games_played = int(line.split(">")[8].split("<")[0])
                # Average Goals Per Game vs Opponent
                goals = int(line.split(">")[10].split("<")[0])
                goals_per_game = round(goals / games_played,2)
                # Average Assists Per Game vs Opponent
                assists = int(line.split(">")[12].split("<")[0])
                assists_per_game = round(assists / games_played,2)
                # Average Points Per Game vs Opponent
                points = int(line.split(">")[14].split("<")[0])
                points_per_game = round(points / games_played,2)
                # Average Shots on Goal vs Opponent
                shots = int(line.split(">")[28].split("<")[0])
                shots_per_game = round(shots / games_played,2)
                # Shooting Percentage vs Opponent
                if shots != 0:
                    shooting_percentage = round(goals / shots, 3)
                else:
                    shooting_percentage = 0

                skater.opp_games = games_played
                skater.opp_goals = goals_per_game
                skater.opp_assists = assists_per_game
                skater.opp_points = points_per_game
                skater.opp_shots = shots_per_game
                skater.opp_shooting = shooting_percentage

                if TEST:
                    print(skater.name, games_played, goals, assists, points, shots, shooting_percentage)

def Write_Splits_Update():
    for skater in all_skaters:
        HR_Scrape_Splits(skater)

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()



def HR_Scrape_Advanced_Stats(skater):
    url = "http://www.hockey-reference.com/players%s-advanced.html" % (skater.HR_URL() + str(skater.url_num))
    try_number = 0
    while try_number <= 5:
        try:
            skater_page = requests.get(url)
            skater_page = BeautifulSoup(skater_page.content, "html.parser")
            break
        except:
            print(skater.name + "ADVANCED STATS PAGE ERROR 1")

    try:
        for line in skater_page.find(id ="all_skaters_advanced"):
            line = str(line)
            if "tr" in line and '>2016-17' in line:
                line = str(line).split('data-stat="season" >2016-17</th><td')[1].split(">")
                cfp = line[19].split("<")[0]
                pdo = line[35].split("<")[0]
                ozs = line[37].split("<")[0]
                # Corsi For Percentage
                if cfp != "" and float(cfp) > 15:
                    skater.cfp = float(cfp)
                # PDO
                if pdo != "" and float(pdo) > 0:
                    skater.pdo = float(pdo)
                # Offensive Zone Start Percentage
                if ozs != "" and float(ozs) > 0:
                    skater.ozs = float(ozs)

                if TEST:
                    print(skater.name, cfp, pdo, ozs)
    except:
        print(skater.name + "ADVANCED STATS PAGE ERROR 2")

def Write_Advanced_Stats_Update():
    for skater in all_skaters:
        HR_Scrape_Advanced_Stats(skater)

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()