# Player CSV Reader

import csv

# Get Raw CSV Info
readFDSalaries = open("FDSalaries.csv")
readFDSalaries = csv.reader(readFDSalaries, delimiter=",")
readFDSalaries = list(filter(lambda x: x[0] != "Id",list(readFDSalaries)))


def Create_FD_Player_Files():
    all_players = []
    for player in readFDSalaries:
        plr = []
        plr += [player[2] + " " + player[4]]
        plr += [int(player[7])]
        plr += [round(float(player[5]),2)]
        plr += player[1]
        all_players.append(plr)

    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/FD_Skater_Salaries.txt", "w")
    skaterFile.write(str(all_players))
    skaterFile.close()