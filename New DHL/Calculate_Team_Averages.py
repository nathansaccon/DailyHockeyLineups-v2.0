# Calculate Team Averages

import pickle

readTeams = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "rb")
all_teams = pickle.load(readTeams)

TEST = True
if TEST:
    print("Test ON for Calculate_Team_Averages.py")

def Team_Averages():
    for team in all_teams:
        gamelog = list(filter(lambda x: x[0] == team.arena,team.game_log))
        length = len(gamelog)
        # Shots For Per Game
        shots_for = round(sum(list(map(lambda x: x[4], gamelog))) / length,1)
        # Shots Against Per Game
        shots_against = round(sum(list(map(lambda x: x[7], gamelog))) / length,1)
        # Goals For Per Game
        goals_for = round(sum(list(map(lambda x: x[1], gamelog))) / length,1)
        # Goals Against Per Game
        goals_against = round(sum(list(map(lambda x: x[2], gamelog))) / length,1)
        # Penatly Minutes For
        pim_for = round(sum(list(map(lambda x: x[5], gamelog))) / length,1)
        # Penalty Minutes Against
        pim_against = round(sum(list(map(lambda x: x[8], gamelog))) / length,1)
        # Powerplay Percent
        pp_percent = round(sum(list(map(lambda x: x[6], gamelog))) / length,1)
        # Penalty Kill Percent
        pk_percent = round(sum(list(map(lambda x: x[9], gamelog))) / length,1)
        # Win Percentage
        win_percent = round(sum(list(map(lambda x: x[3], gamelog))) / length *100,1)

        team.avg_shots = shots_for
        team.avg_shots_against = shots_against
        team.avg_goals = goals_for
        team.avg_goals_against = goals_against
        team.avg_pim = pim_for
        team.avg_pim_against = pim_against
        team.avg_pp_percent = pp_percent
        team.avg_pk_percent = pk_percent

        if TEST:
            print(team.name, shots_for, shots_against, goals_for, goals_against, pim_for, pim_against, pp_percent, pk_percent)
    teamFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "wb")
    pickle.dump(all_teams, teamFile)
    teamFile.close()