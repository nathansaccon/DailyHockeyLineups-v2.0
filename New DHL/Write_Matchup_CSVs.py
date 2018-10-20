# Write Player Matchup Stats

import pickle, csv
from General_Functions import Team_Full_Name

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)
readTeams = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "rb")
all_teams = pickle.load(readTeams)

games = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Start_Times.txt", "r")
games = eval(games.read())


def Write_Goalie_Matchup_CSV():
    # Remove empty list for sorting purpose
    for goalie in all_goalies:
        if goalie.opp_games == "":
            goalie.opp_games = 0
    # Sort By # Of Games vs Opponent / By Team
    goalies = sorted(all_goalies, key = lambda x: x.opp_games)[::-1]
    goalies = sorted(goalies, key = lambda x: x.team)
    goalies = list(map(lambda x: [x.name, x.position, str(x.dk_salary) + "/" + str(x.fd_salary), x.arena, round(x.pp_arena *100,1),
                                  x.team, x.opponent, x.opp_games, x.opp_win_percent, x.opp_save_percent, x.opp_gaa],goalies))

    # Write CSV Document
    header = ["DailyHockeyLineups.com Daily Matchup Stats", "", "", "", "", "", "DailyHockeyLineups.com", "", "", "", "", ""]
    stat_header = ["Player Name", "Position", "DraftKings/FanDuel Cost", "Arena", "Arena Win Percent", "Team", "Opponent (Opp)",
                   "Games Played vs Opp", "Win % vs Opp", "Save % vs Opp", "Goals Against Avg vs Opp"]

    goalie_matchup_doc = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Matchup Stats Goalies.csv', 'w')
    goalie_matchup_doc_writer = csv.writer(goalie_matchup_doc)
    goalie_matchup_doc_writer.writerow(header)
    goalie_matchup_doc_writer.writerow(stat_header)

    total_index = 1
    max_index = len(goalies)
    index = 1
    cur_team = ""
    for goalie in goalies:
        if index >= 20 and cur_team != goalie[5] and (max_index - total_index) >= 5:
            goalie_matchup_doc_writer.writerow(stat_header)
            index = 1

        goalie_matchup_doc_writer.writerow(goalie)
        cur_team = goalie[5]
        index += 1
        total_index += 1

    goalie_matchup_doc.close()


def Write_Player_Matchup_CSV():
    # Sort Players By Name and Then Team
    skaters = sorted(all_skaters, key = lambda x: x.name.split(" ")[1])
    skaters = sorted(skaters, key = lambda x: x.team)
    # Create List Of Skaters in CSV Format
    skaters = list(map(lambda x: [x.name, x.position, str(x.dk_salary) + "/" + str(x.fd_salary), x.arena, round(x.pp_arena *100,1),
                                  x.team, x.opponent, x.opp_games, x.opp_points, x.opp_shots, x.opp_shooting*100, x.pp_season*100, x.ozs,
                                  x.cfp, x.pdo],skaters))
    # Fix Rounding To Avoid Empty Strings
    for skater in skaters:
        if skater[10] != "":
            skater[10] = round(skater[10],1)
        if skater[11] != "":
            skater[11] = round(skater[11],1)
    # Write CSV Document
    header = ["DailyHockeyLineups.com Daily Matchup Stats", "", "", "", "", "", "DailyHockeyLineups.com", "", "", "", "", ""]
    stat_header = ["Player Name", "Position", "DraftKings/FanDuel Cost", "Arena", "Arena Point Percent", "Team", "Opponent (Opp)",
                   "Games Played vs Opp", "Avg Points vs Opp", "Avg Shots vs Opp", "Shooting % vs Opp", "Point % This Season",
                   "Offesive Zone Starts", "Corsi For %", "PDO"]

    skater_matchup_doc = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Matchup Stats Skaters.csv', 'w')
    skater_matchup_doc_writer = csv.writer(skater_matchup_doc)
    skater_matchup_doc_writer.writerow(header)
    skater_matchup_doc_writer.writerow(stat_header)

    cur_team = skaters[0][5]
    for skater in skaters:
        if cur_team != skater[5]:
            skater_matchup_doc_writer.writerow(stat_header)

        skater_matchup_doc_writer.writerow(skater)
        cur_team = skater[5]

    skater_matchup_doc.close()


def Category_Winners(team, opponent):
    positive_cat = [3,5,8,9,10,11,12,13,14]
    negative_cat = [4,6,7]

    index = 2
    while index <= 14:
        if team[index] == opponent[index]:
            index += 1
            continue
        if index in positive_cat:
            if team[index] > opponent[index]:
                team[15] += 1
            else:
                opponent[15] += 1
        if index in negative_cat:
            if team[index] > opponent[index]:
                opponent[15] += 1
            else:
                team[15] += 1
        index += 1
    return [team, opponent]




def Write_Team_Matchup_CSV():
    teams = sorted(all_teams, key = lambda x: x.start_time)
    teams = list(map(lambda x: [x.name, x.opponent, x.arena, x.avg_shots, x.avg_shots_against, x.avg_goals, x.avg_goals_against,
                                x.avg_pim, x.avg_pim_against, x.avg_pp_percent, x.avg_pk_percent, x.corsi_for, x.fenwick_for,
                                x.ozs, x.pdo, 0], teams))

    # Sort Teams So Opponents are Next To Each Other
    team_pairs = []
    for team in teams:
        team_pairs += [team]
        for opponent in teams:
            if team[1] == opponent[0]:
                team_pairs += [opponent]
                teams.remove(opponent)

    # Adds Who Wins Each Category
    index = 0
    teams_updated = []
    for i in team_pairs[::2]:
        teams_updated += Category_Winners(i, team_pairs[index + 1])
        index += 2
    # Make First Name, Full Name
    for team in teams_updated:
        team[0] = Team_Full_Name(team[0])

    header = ["DailyHockeyLineups.com Daily Matchup Stats", "", "", "", "", "", "DailyHockeyLineups.com", "", "", "", "", ""]
    stat_header = ["Team Name", "Opponent", "Arena", "Avg Shots", "Avg Shots Against", "Avg Goals", "Avg Goals Against", "Avg PIM",
                   "Avg PIM Against", "Avg Powerplay %", "Avg Penalty Kill %", "Corsi For %", "Fenwick For %",
                   "Offensive Zone Start", "PDO", "Categories Won"]

    team_matchup_doc = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Matchup Stats Teams.csv', 'w')
    team_matchup_doc_writer = csv.writer(team_matchup_doc)
    team_matchup_doc_writer.writerow(header)
    team_matchup_doc_writer.writerow(stat_header)

    index = 0
    for team in teams_updated:
        if index != 0 and index % 2 == 0:
            team_matchup_doc_writer.writerow("")

        team_matchup_doc_writer.writerow(team)
        index += 1
    team_matchup_doc.close()


def Write_All_Matchup_CSV():
    #Write_Goalie_Matchup_CSV()
    #Write_Player_Matchup_CSV()
    Write_Team_Matchup_CSV()




