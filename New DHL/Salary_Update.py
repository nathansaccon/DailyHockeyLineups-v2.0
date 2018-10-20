# SALARY Update File

import pickle

TEST = True

# Open binary skater class file.
readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
#Open binary goalie class file
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)
# Open text FD Salary file.
fd_salary_lst = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/FD_Skater_Salaries.txt", "r")
fd_salary_lst = eval(fd_salary_lst.read())

if TEST:
    print("Test ON for Salary_Update.py")
    plr = all_skaters[0]

# Gets the salary of one player
def Get_FD_Salary(skater):
    price_found = False

    for player in fd_salary_lst:
        if skater.name == player[0]:
            if TEST:
                pass
                print(skater.name, skater.dk_salary, player[1], skater.position, player[3])
            price_found = True
            return [player[1],player[2], player[3]]

    if not price_found and TEST:
        print(skater.name, "NO MATCH FOUND-----------")



# Updates the salaries for all skaters
def Update_FD_salary():
    for skater in all_skaters:
        stats = Get_FD_Salary(skater)
        if stats != None:
            skater.fd_average_fpoints = stats[1]
            skater.fd_position = stats[2]
            skater.fd_salary = stats[0]
    skaterFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "wb")
    pickle.dump(all_skaters, skaterFile)
    skaterFile.close()

    for goalie in all_goalies:
        try:
            salary = Get_FD_Salary(goalie)[0]
            fpoints = Get_FD_Salary(goalie)[1]
        except:
            salary = Get_FD_Salary(goalie)
            fpoints = Get_FD_Salary(goalie)
        if salary != None:
            goalie.fd_salary = salary
            goalie.fd_average_fpoints = fpoints
    goalieFile = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "wb")
    pickle.dump(all_goalies, goalieFile)
    goalieFile.close()

