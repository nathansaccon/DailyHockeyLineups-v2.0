# Player CSV Reader

import csv, pickle
from Classes import Skater, Goalie
from General_Functions import Write_Start_Time_File

# Get Raw CSV Info
readDKSalaries = open("DKSalaries.csv")
readDKSalaries = csv.reader(readDKSalaries, delimiter=",")
readDKSalaries = list(filter(lambda x: x[0] != "Position",list(readDKSalaries)))

def Create_DK_Player_Files():
    all_players = []
    for player in readDKSalaries:
        if player[0] != "G":
            plr = Skater()
            plr.name = player[1]
            plr.position = player[0]
            plr.dk_salary = int(player[2])
            plr.team = player[5].upper()

            teams = [player[3].split("@")[0].upper(), player[3].split("@")[1].split(" ")[0].upper()]
            plr.opponent = list(filter(lambda x: x != player[5].upper(),teams))[0]
            if player[5].upper() == teams[0]:
                plr.arena = "Away"
            else:
                plr.arena = "Home"

            times = player[3].split(" ")[1].split(":")
            times[0] = int(times[0])
            times[1] = int(times[1][:2])
            plr.start_time = times[0] + times[1]/60

            plr.average_fpoints = float(player[4])
            plr.website = "DK"
            all_players += [plr]
        else:
            gol = Goalie()
            gol.name = player[1]
            gol.position = player[0]
            gol.dk_salary = int(player[2])
            gol.team = player[5].upper()
            teams = [player[3].split("@")[0].upper(), player[3].split("@")[1].split(" ")[0].upper()]
            gol.opponent = list(filter(lambda x: x != player[5].upper(),teams))[0]
            if player[5].upper() == teams[0]:
                gol.arena = "Away"
            else:
                gol.arena = "Home"

            times = player[3].split(" ")[1].split(":")
            times[0] = int(times[0])
            times[1] = int(times[1][:2])
            gol.start_time = times[0] + times[1]/60

            gol.average_fpoints = float(player[4])
            gol.website = "DK"
            all_players += [gol]

    all_skaters = list(filter(lambda x: x.position != "G", all_players))
    all_goalies = list(filter(lambda x: x.position == "G", all_players))

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()

    goalieFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "wb")
    pickle.dump(all_goalies, goalieFile)
    goalieFile.close()