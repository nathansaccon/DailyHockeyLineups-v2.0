import pickle, requests
from bs4 import BeautifulSoup
from General_Functions import team_equal

TEST = True

readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

if TEST:
    print("Test ON for Scrape Stats Goalies.py")
    plr = all_goalies[0]


def HR_Name_Fix(name):
    if name == "Edward Pasquale":
        return "Eddie Pasquale"
    if name == "Matthew O'Connor":
        return "Matt O'Connor"
    if name == "Matt Murray":
        return "Matthew Murray"
    else:
        return name

# Get Goalie Gamelogs
def HR_Scrape_Gamelogs_G(goalie):
    url_number = 1
    right_num = False
    # Special Cases
    if goalie.name in ["John Gibson"]:
        url_number = 2
    #-------------

    while (not right_num) and url_number < 10:
        url = "http://www.hockey-reference.com/players%s/gamelog/2017" % (goalie.HR_URL() + str(url_number))
        try:
            goalie_page = requests.get(url)
            goalie_page = BeautifulSoup(goalie_page.content, "html.parser")
            page_name = str(goalie_page.find_all("h1")).split(">")[1].split("<")[0]
            if page_name == HR_Name_Fix(goalie.name):
                right_num = True
            else:
                url_number += 1
                if TEST:
                    print(goalie.name + " is not " + page_name)
                continue
        except:
            print(goalie.name + " GAMELOG PAGE ERROR")
            continue
    if TEST:
        print(goalie.name + "'s URL number:", url_number)

    # Games
    game_logs = []

    for line in goalie_page.find_all("tr"):
        line = str(line)
        if "gamelog" in line:
            line = line.split(">")
            # Arena
            if line[16].split("<")[0] == "@":
                arena = "Away"
            else:
                arena = "Home"
            # Win/Loss
            if line[24].split("<")[0] == "W":
                outcome = 1
            else:
                outcome = 0
            # Goals Against
            goals_against = line[26].split("<")[0]
            if goals_against == "":
                goals_against = 10
            else:
                goals_against = int(goals_against)
            # Saves
            saves = line[30].split("<")[0]
            if saves == "":
                saves = 0
            else:
                saves = int(saves)

            game = [arena, outcome, goals_against, saves]
            game_logs.append(game)

    goalie.game_log = game_logs
    goalie.url_num = url_number

    if TEST:
        print(goalie.game_log)


def Write_Gamelog_Update_G():
    for goalie in all_goalies:
        try_number = 0
        while try_number <= 5:
            try:
                HR_Scrape_Gamelogs_G(goalie)
                break
            except:
                continue

    goalieFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "wb")
    pickle.dump(all_goalies, goalieFile)
    goalieFile.close()




def HR_Scrape_Splits_G(goalie):
    url = "http://www.hockey-reference.com/players%s/splits/" % (goalie.HR_URL() + str(goalie.url_num))
    try_number = 0
    while try_number <= 5:
        try:
            goalie_page = requests.get(url)
            goalie_page = BeautifulSoup(goalie_page.content, "html.parser")
            break
        except:
            print(goalie.name + "SPLITS PAGE ERROR")

    for line in goalie_page.find_all("tr"):
        line = str(line)
        if "/teams/" in line:
            team = line.split(">")[5].split("<")[0]
            if team_equal(team, goalie.opponent):
                # Games Played vs Opponent
                games_played = int(line.split(">")[8].split("<")[0])
                # Wins vs Opponent
                try:
                    wins = int(line.split(">")[10].split("<")[0])
                    win_percent = round(wins / games_played *100,1)
                except:
                    wins = 0
                    win_percent = 0
                # Save Percent vs Opponent
                save_percent = float(line.split(">")[22].split("<")[0])
                # Goals Against Average vs Opponent
                goals_against_avg = float(line.split(">")[24].split("<")[0])

                goalie.opp_games = games_played
                goalie.opp_win_percent = win_percent
                goalie.opp_save_percent = save_percent
                goalie.opp_gaa = goals_against_avg
                if TEST:
                    print(goalie.name, games_played, win_percent, save_percent, goals_against_avg)


def Write_Splits_Update_G():
    for goalie in all_goalies:
        HR_Scrape_Splits_G(goalie)

    goalieFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "wb")
    pickle.dump(all_goalies, goalieFile)
    goalieFile.close()