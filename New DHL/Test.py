# TEST
import pickle

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)

readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

readTeams = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/NHL_Teams.txt", "rb")
all_teams = pickle.load(readTeams)

plr = all_skaters[0]
gol = all_goalies[0]
tm = all_teams[0]

