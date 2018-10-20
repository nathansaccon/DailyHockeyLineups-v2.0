# Write Matchup Lists

import pickle

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)

injured = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "r")
injured = eval(injured.read())

# Remove Injured / Null
all_skaters = list(filter(lambda x: x.name not in injured and x.opp_points != "" and x.opp_games >= 3, all_skaters))

point_players = sorted(all_skaters, key = lambda x : x.opp_points)[::-1][:7]
shot_players = sorted(all_skaters, key = lambda x : x.opp_shots)[::-1][:7]

def String_Writer(stat):
    finished_string = ""
    if stat == "points":
        for player in point_players:
            line = "%s averages %s points per game across %s games against %s.\n" % (player.name, str(player.opp_points),
                                                                                   str(player.opp_games), player.opponent)
            finished_string += line
    if stat == "shots":
        for player in shot_players:
            line = "%s averages %s shots per game across %s games against %s.\n" % (player.name, str(player.opp_shots),
                                                                                     str(player.opp_games), player.opponent)
            finished_string += line
    return finished_string

def Write_Matchup_Lists():
    write_doc = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Matchup_Lists.txt", "w")
    write_doc.write(String_Writer("points") + "\n\n" + String_Writer("shots"))
    write_doc.close()