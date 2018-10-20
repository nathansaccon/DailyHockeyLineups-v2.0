# Write Matchup Tweets

import pickle
from General_Functions import Team_Full_Name

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)
readTeams = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "rb")
all_teams = pickle.load(readTeams)

injured = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "r")
injured = eval(injured.read())
starting = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "r")
starting = eval(starting.read())

# Remove Injured / Null
all_skaters = list(filter(lambda x: x.name not in injured and x.opp_points != "" and x.opp_shots != ""
                          and x.opp_games >= 3 and x.start_time >=6 and x.pp_arena != "", all_skaters))
all_goalies = list(filter(lambda x: x.name not in injured and x.name in starting and x.opp_games != "" and x.pp_arena != "", all_goalies))

point_players = sorted(all_skaters, key = lambda x : x.opp_points)[::-1]
point_players = list(filter(lambda x: x.opp_points >= 0.7, point_players))
shot_players = sorted(all_skaters, key = lambda x : x.opp_shots)[::-1]
shot_players = list(filter(lambda x: x.opp_shots >= 2.5, shot_players))
arena_players = sorted(all_skaters, key = lambda x : x.pp_arena)[::-1]
arena_players = list(filter(lambda x: x.pp_arena >= 0.55, arena_players))
all_teams = sorted(all_teams, key = lambda x : x.avg_shots)[::-1]

def Write_Tweets(stat, ht1):
    tweets = ""
    if stat == "points":
        for plr in point_players:
            tweet = "#%s %s averages %s points per game in %s career games against %s. #FantasyHockey #NHL #%s\n\n" % (ht1, plr.name, plr.opp_points, plr.opp_games, plr.opponent, plr.team)
            tweets += tweet
    if stat == "shots":
        for plr in shot_players:
            tweet = "#%s %s averages %s shots per game in %s career games against %s. #FantasyHockey #NHL #%s\n\n" % (ht1, plr.name, plr.opp_shots, plr.opp_games, plr.opponent, plr.team)
            tweets += tweet
    if stat == "arena":
        for plr in arena_players:
            if plr.arena == "Home":
                tweet = "#%s %s averages %s points per game at home this season. #FantasyHockey #NHL #%s\n\n" % (ht1, plr.name, plr.pp_arena, plr.team)
            if plr.arena == "Away":
                tweet = "#%s %s averages %s points per game on the road this season. #FantasyHockey #NHL #%s\n\n" % (ht1, plr.name, plr.pp_arena, plr.team)
            tweets += tweet
    if stat == "goalie":
        for gol in all_goalies:
            tweet = "%s will be starting tonight. Against %s he has a career win rate of %s%%, GAA of %s, and SV%% of %s #FantasyHockey #NHL #%s\n\n" % (gol.name, gol.opponent, int(gol.opp_win_percent), gol.opp_gaa, gol.opp_save_percent, gol.team)
            tweets += tweet
    if stat == "team":
        for tm in all_teams:
            if tm.arena == "Home":
                tweet = "The %s average %s shots for and %s shots against when playing at home this season. #FantasyHockey #NHL #%s #%s\n\n" % (Team_Full_Name(tm.name), tm.avg_shots, tm.avg_shots_against, tm.name, ht1)
                tweets += tweet
            if tm.arena == "Away":
                tweet = "The %s average %s shots for and %s shots against when playing on the road this season. #FantasyHockey #NHL #%s #%s\n\n" % (Team_Full_Name(tm.name), tm.avg_shots, tm.avg_shots_against, tm.name, ht1)
                tweets += tweet
    return tweets

def Write_Tweet_Files():
    ## Hashtag Control
    hashtag_control = input("Custom Hashtag y/n: ")
    if hashtag_control == "n":
        ht1 = "NHLFantasy"
    if hashtag_control == "y":
        ht1 = input("Enter Today's Hashtag: #")

    point_tweet_file = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Hockey Point Tweets.txt', 'w')
    point_tweet_file.write(Write_Tweets("points", ht1))
    point_tweet_file.close()

    shot_tweet_file = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Hockey Shot Tweets.txt', 'w')
    shot_tweet_file.write(Write_Tweets("shots", ht1))
    shot_tweet_file.close()

    goalie_tweet_file = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Hockey Goalie Tweets.txt', 'w')
    goalie_tweet_file.write(Write_Tweets("goalie", ht1))
    goalie_tweet_file.close()

    team_tweet_file = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Hockey Team Tweets.txt', 'w')
    team_tweet_file.write(Write_Tweets("team", ht1))
    team_tweet_file.close()

    arena_tweet_file = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Hockey Arena Tweets.txt', 'w')
    arena_tweet_file.write(Write_Tweets("arena", ht1))
    arena_tweet_file.close()
