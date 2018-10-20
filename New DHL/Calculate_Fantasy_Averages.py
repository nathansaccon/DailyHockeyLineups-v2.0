# Calculate Fantasy Averages

import pickle

TEST = True

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)

## Global Variables
# DraftKings
dk_goal_pts = 3
dk_assist_pts = 2
dk_shot_pts = 0.5
dk_block_pts = 0.5
#FanDuel
fd_goal_pts = 12
fd_pp_goal_add = 0.5
fd_assist_pts = 8
fd_pp_assist_add = 0.5
fd_shot_pts = 1.6
fd_block_pts = 1.6

if TEST:
    plr = all_skaters[0]
    print("Test ON for Calculate_Fantasy_Averages.py")

'''DraftKings Stats'''
# Gamelogs to Fantasy Points
def DK_Gamelog_to_Fpts(gamelog):
    if gamelog == [] or gamelog == "":
        return 0
    else:
        # Fantasy Points From Goals
        goal_pts = sum(list(map(lambda x: dk_goal_pts * x[1],gamelog)))
        # Fantasy Points From Assists
        assist_pts = sum(list(map(lambda x: dk_assist_pts * x[2],gamelog)))
        # Fantasy Points From Shots
        shot_pts = sum(list(map(lambda x: dk_shot_pts * x[3],gamelog)))
        #Fantasy Points From Blocks
        block_pts = sum(list(map(lambda x: dk_block_pts * x[4],gamelog)))
        average_pts = (goal_pts + assist_pts + shot_pts + block_pts) / len(gamelog)
        return round(average_pts,2)

# Returns the average fantasy points over the last X games
def DK_Last_X(skater, num):
    games = skater.game_log[::-1][:num]
    return DK_Gamelog_to_Fpts(games)

# Returns the average fantasy points from either home or away games
def DK_Arena_Fpts(skater):
    games = list(filter(lambda x: x[0] == skater.arena, skater.game_log))
    return DK_Gamelog_to_Fpts(games)

# Returns the players floor
def DK_Floor(skater):
    games = skater.game_log[::-1][:5]
    games = list(map(lambda x: x[1] * dk_goal_pts + x[2] * dk_assist_pts +
                     x[3] * dk_shot_pts + x[4] * dk_block_pts, games))
    if len(games) == 0:
        return 0
    else:
        minimum = round(min(games),2)
        return minimum

# Returns the players ceiling
def DK_Ceiling(skater):
    games = skater.game_log
    games = list(map(lambda x: x[1] * dk_goal_pts + x[2] * dk_assist_pts +
                     x[3] * dk_shot_pts + x[4] * dk_block_pts, games))
    if len(games) == 0:
        return 0
    else:
        maximum = round(max(games),2)
        return maximum


'''FanDuel Stats'''
# Gamelogs to Fantasy Points
def FD_Gamelog_to_Fpts(gamelog):
    if gamelog == [] or gamelog == "":
        return 0
    else:
        # Fantasy Points From Goals
        goal_pts = sum(list(map(lambda x: fd_goal_pts * x[1],gamelog)))
        # Fantasy Points From Assists
        assist_pts = sum(list(map(lambda x: fd_assist_pts * x[2],gamelog)))
        # Fantasy Points From Shots
        shot_pts = sum(list(map(lambda x: fd_shot_pts * x[3],gamelog)))
        #Fantasy Points From Blocks
        block_pts = sum(list(map(lambda x: fd_block_pts * x[4],gamelog)))
        # Fantasy Points From PP Goals
        pp_goal_pts = sum(list(map(lambda x: fd_pp_goal_add * x[5],gamelog)))
        # Fantasy Points From PP Assists
        pp_assist_pts = sum(list(map(lambda x: fd_pp_assist_add * x[6],gamelog)))
        average_pts = (goal_pts + assist_pts + shot_pts + block_pts + pp_goal_pts + pp_assist_pts) / len(gamelog)
        return round(average_pts,2)

# Returns the average fantasy points over the last X games
def FD_Last_X(skater, num):
    games = skater.game_log[::-1][:num]
    return FD_Gamelog_to_Fpts(games)

# Returns the average fantasy points from either home or away games
def FD_Arena_Fpts(skater):
    games = list(filter(lambda x: x[0] == skater.arena, skater.game_log))
    return FD_Gamelog_to_Fpts(games)

# Returns the players floor
def FD_Floor(skater):
    games = skater.game_log[::-1][:5]
    games = list(map(lambda x: x[1] * fd_goal_pts + x[2] * fd_assist_pts + x[3] * fd_shot_pts +
                     x[4] * fd_block_pts + x[5] * fd_pp_goal_add + x[6] * fd_pp_assist_add, games))
    if len(games) == 0:
        return 0
    else:
        minimum = round(min(games),2)
        return minimum

# Returns the players ceiling
def FD_Ceiling(skater):
    games = skater.game_log
    games = list(map(lambda x: x[1] * fd_goal_pts + x[2] * fd_assist_pts + x[3] * fd_shot_pts +
                     x[4] * fd_block_pts + x[5] * fd_pp_goal_add + x[6] * fd_pp_assist_add, games))
    if len(games) == 0:
        return 0
    else:
        maximum = round(max(games),2)
        return maximum

'''General Gamelog Stats'''
# Returns the arena point percentage
def Arena_Point_Percentage(skater):
    games_played = list(filter(lambda x: x[0] == skater.arena, skater.game_log))
    if len(games_played) == 0:
        return 0
    else:
        games_with_point = list(filter(lambda x: x[1] != 0 or x[2] != 0, games_played))
        point_percentage = round(len(games_with_point) / len(games_played),2)
        return point_percentage

# Returns the player's point percentage in the last X games
def Point_Percentage_Last_X(skater, num):
    games_played = skater.game_log[::-1][:num]
    if len(games_played) == 0:
        return 0
    else:
        games_with_point = list(filter(lambda x: x[1] != 0 or x[2] != 0, games_played))
        point_percentage = round(len(games_with_point) / len(games_played),3)
        return point_percentage


# Add Fantasy Averages To Skater Class
def Add_Fantasy_Averages():
    for skater in all_skaters:
        # DraftKings Stats
        skater.dk_last_10 = DK_Last_X(skater, 10)
        skater.dk_last_5 = DK_Last_X(skater, 5)
        skater.dk_arena_fpts = DK_Arena_Fpts(skater)
        skater.dk_floor = DK_Floor(skater)
        skater.dk_ceiling = DK_Ceiling(skater)
        # FanDuel Stats
        skater.fd_last_10 = FD_Last_X(skater, 10)
        skater.fd_last_5 = FD_Last_X(skater, 5)
        skater.fd_arena_fpts = FD_Arena_Fpts(skater)
        skater.fd_floor = FD_Floor(skater)
        skater.fd_ceiling = FD_Ceiling(skater)
        # General Stats
        skater.pp_arena = Arena_Point_Percentage(skater)
        skater.pp_season = Point_Percentage_Last_X(skater, 82)
        skater.pp_last_10 = Point_Percentage_Last_X(skater, 10)


        if TEST:
            print(skater.name, skater.dk_last_10, skater.dk_last_5, skater.dk_arena_fpts, skater.dk_floor, "|",
                  skater.dk_ceiling, skater.pp_arena, skater.pp_season, skater.pp_last_10, "|", skater.fd_last_10,
                  skater.fd_last_5, skater.fd_last_10, skater.fd_arena_fpts, skater.fd_floor)

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()
