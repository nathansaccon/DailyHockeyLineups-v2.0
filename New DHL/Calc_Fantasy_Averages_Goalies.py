import pickle

TEST = True

readgoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readgoalies)

## Global Variables
# DraftKings
dk_win_pts = 3
dk_save_pts = 0.2
dk_ga_pts = -1
dk_shutout_pts = 2
# FanDuel
fd_win_pts = 12
fd_save_pts = 0.8
fd_ga_pts = -4
fd_shutout_pts = 8

if TEST:
    plr = all_goalies[0]
    print("Test ON for Calc_Fantasy_Averages_Goalies.py")

'''DraftKings Stats'''
# Gamelogs to Fantasy Points
def DK_Gamelog_to_Fpts(gamelog):
    if gamelog == [] or gamelog == "":
        return 0
    else:
        # Fantasy Points From Wins
        win_pts = sum(list(map(lambda x: dk_win_pts * x[1],gamelog)))
        # Fantasy Points From Goals Against
        goals_against_pts = sum(list(map(lambda x: dk_ga_pts * x[2],gamelog)))
        # Fantasy Points From Saves
        save_pts = sum(list(map(lambda x: dk_save_pts * x[3],gamelog)))

        average_pts = (win_pts + goals_against_pts + save_pts) / len(gamelog)
        return round(average_pts,2)

# Returns the average fantasy points over the last X games
def DK_Last_X(goalie, num):
    games = goalie.game_log[::-1][:num]
    return DK_Gamelog_to_Fpts(games)

# Returns the average fantasy points from either home or away games
def DK_Arena_Fpts(goalie):
    games = list(filter(lambda x: x[0] == goalie.arena, goalie.game_log))
    return DK_Gamelog_to_Fpts(games)

'''FanDuel Stats'''
# Gamelogs to Fantasy Points
def FD_Gamelog_to_Fpts(gamelog):
    if gamelog == [] or gamelog == "":
        return 0
    else:
        # Fantasy Points From Wins
        win_pts = sum(list(map(lambda x: fd_win_pts * x[1],gamelog)))
        # Fantasy Points From Goals Against
        goals_against_pts = sum(list(map(lambda x: fd_ga_pts * x[2],gamelog)))
        # Fantasy Points From Saves
        save_pts = sum(list(map(lambda x: fd_save_pts * x[3],gamelog)))

        average_pts = (win_pts + goals_against_pts + save_pts) / len(gamelog)
        return round(average_pts,2)

# Returns the average fantasy points over the last X games
def FD_Last_X(goalie, num):
    games = goalie.game_log[::-1][:num]
    return FD_Gamelog_to_Fpts(games)

# Returns the average fantasy points from either home or away games
def FD_Arena_Fpts(goalie):
    games = list(filter(lambda x: x[0] == goalie.arena, goalie.game_log))
    return FD_Gamelog_to_Fpts(games)

'''General Gamelog Stats'''
# Returns the arena win percentage
def Arena_Win_Percentage(goalie):
    games_played = list(filter(lambda x: x[0] == goalie.arena, goalie.game_log))
    if len(games_played) == 0:
        return 0
    else:
        games_with_win = list(filter(lambda x: x[1] == 1, games_played))
        win_percentage = round(len(games_with_win) / len(games_played),3)
        return win_percentage

# Returns the player's point percentage in the last X games
def Win_Percentage_Last_X(goalie, num):
    games_played = goalie.game_log[::-1][:num]
    if len(games_played) == 0:
        return 0
    else:
        games_with_win = list(filter(lambda x: x[1] == 1, games_played))
        win_percentage = round(len(games_with_win) / len(games_played),3)
        return win_percentage


# Add Fantasy Averages To goalie Class
def Add_Fantasy_Averages_G():
    for goalie in all_goalies:
        # DraftKings Stats
        goalie.dk_last_10 = DK_Last_X(goalie, 10)
        goalie.dk_last_5 = DK_Last_X(goalie, 5)
        goalie.dk_arena_fpts = DK_Arena_Fpts(goalie)
        # FanDuel Stats
        goalie.fd_last_10 = FD_Last_X(goalie, 10)
        goalie.fd_last_5 = FD_Last_X(goalie, 5)
        goalie.fd_arena_fpts = FD_Arena_Fpts(goalie)
        # General Stats
        goalie.pp_arena = Arena_Win_Percentage(goalie)
        goalie.pp_season = Win_Percentage_Last_X(goalie, 82)
        goalie.pp_last_10 = Win_Percentage_Last_X(goalie, 10)


        if TEST:
            print(goalie.name, goalie.dk_last_10, goalie.dk_last_5, goalie.dk_arena_fpts, "|", goalie.pp_arena,
                  goalie.pp_season, goalie.pp_last_10, "|", goalie.fd_last_10, goalie.fd_last_5, goalie.fd_arena_fpts)

    goalieFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "wb")
    pickle.dump(all_goalies, goalieFile)
    goalieFile.close()

