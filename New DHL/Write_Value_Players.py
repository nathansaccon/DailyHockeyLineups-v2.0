# Write Value Players

import pickle

TEST = False

if TEST:
    print("Test ON for Write_Value_Players.py")

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

injured = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "r")
injured = eval(injured.read())
starting = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "r")
starting = eval(starting.read())

# Remove Injured / Non-Starter / Low Cost / Too Early
all_skaters = list(filter(lambda x: x.name not in injured and x.dk_salary > 2800 and x.start_time >= 7, all_skaters))
all_goalies = list(filter(lambda x: x.name not in injured and x.name in starting, all_goalies))


# Seperate By Position and Filter Out High Cost
centers = list(filter(lambda x: x.position == "C" and x.dk_salary < 5000, all_skaters))
wingers = list(filter(lambda x: (x.position == "RW" or x.position == "LW") and x.dk_salary < 5000, all_skaters))
defenceman = list(filter(lambda x: x.position == "D" and x.dk_salary < 5000, all_skaters))


# Sort By Value
goalies = sorted(all_goalies, key = lambda x : x.Player_Value())[::-1][:10]
centers = sorted(centers, key = lambda x : x.Player_Value())[::-1][:10]
wingers = sorted(wingers, key = lambda x : x.Player_Value())[::-1][:10]
defenceman = sorted(defenceman, key = lambda x : x.Player_Value())[::-1][:10]

# Write In String Format
goalies = list(map(lambda x: x.name + " - " + x.team + " [" + str(x.Player_Value()) + ", " + str(x.dk_salary) + "]\n",goalies))
centers = list(map(lambda x: x.name + " - " + x.team + " [" + str(x.Player_Value()) + ", " + str(x.dk_salary) + "]\n",centers))
wingers = list(map(lambda x: x.name + " - " + x.team + " [" + str(x.Player_Value()) + ", " + str(x.dk_salary) + "]\n",wingers))
defenceman = list(map(lambda x: x.name + " - " + x.team + " [" + str(x.Player_Value()) + ", " + str(x.dk_salary) + "]\n",defenceman))

def Write_Strs(lst):
    full_str = ""
    for item in lst:
        full_str += item
    return full_str


def Write_Value_Lists():
    write_value_doc = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Value_Players.txt", "w")
    write_value_doc.write("Value Goalies\n\n" + Write_Strs(goalies) +
                          "\nValue Centers \n\n" + Write_Strs(centers) +
                          "\nValue Wingers \n\n" + Write_Strs(wingers) +
                          "\nValue Defenceman\n\n" + Write_Strs(defenceman))
    write_value_doc.close()


if TEST:
    print(goalies)
    print(centers)
    print(wingers)
    print(defenceman)