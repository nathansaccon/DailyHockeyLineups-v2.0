## Write Lineup Files

import pickle, itertools

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

injured = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "r")
injured = eval(injured.read())
starting = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "r")
starting = eval(starting.read())
manual_remove = open("/Users/nathansaccon/Documents/Coding/New DHL/Input Files/Manual_Remove.txt", "r")
manual_remove = eval(manual_remove.read())

# Filter Out Injured / Non-Starting
all_skaters = list(filter(lambda x: x.name not in injured and x.name not in manual_remove, all_skaters))
all_goalies = list(filter(lambda x: x.name not in injured and x.name in starting and x.name not in manual_remove, all_goalies))

# Map So Start Time is not confused with PM
def Early_Start_Fix(lop):
    lop_output = []
    for player in lop:
        if player.start_time >= 11.6:
            player.start_time = 1
        lop_output += [player]
    return lop_output

# Return Most Occruances of a single team in a list
# listof(Team_Abbreviations) -> Nat
def count_teams(lota):
    most_so_far = 0
    for team_ab in lota:
        count = lota.count(team_ab)
        if count > most_so_far:
            most_so_far = count
        else:
            pass
    return most_so_far
# Gets important stats from a team
# Team -> Team
def get_team_stats_fd(team):
    cost = 0
    expected_points = 0
    teams_in_team = []

    for player in team:
        expected_points += player[2]
        cost += player[1]
        teams_in_team.append(player[3])

    team_set = set(teams_in_team)
    most_teams = count_teams(teams_in_team)

    valid = len(team_set) >= 3 and cost <= 55000 and most_teams <= 4
    return [round(expected_points,2), cost, valid,]


# Gets important stats from a team
# Team -> Team
def get_team_stats_dk(team):
    cost = 0
    expected_points = 0
    teams_in_team = []

    for player in team:
        expected_points += player[2]
        cost += player[1]
        if player[5] != "G":
            teams_in_team.append(player[3])

    team_set = set(teams_in_team)
    valid = len(team_set) >= 3 and cost <= 50000
    return [round(expected_points,2), cost, valid]


def Write_DK_Lineups(skaters, goalies, st, stu, turbo, tag):
    # Early Start Time Fix
    skaters = Early_Start_Fix(skaters)
    goalies = Early_Start_Fix(goalies)
    # Filter Skaters By Start Time
    if turbo == "y":
        all_skaters = list(filter(lambda x: st <= x.start_time <= stu, skaters))
        all_goalies = list(filter(lambda x: st <= x.start_time <= stu, goalies))
    if turbo == "n":
        all_skaters = list(filter(lambda x: st <= x.start_time, skaters))
        all_goalies = list(filter(lambda x: st <= x.start_time, goalies))

    # Sort Players By Projected Points
    all_skaters = sorted(all_skaters, key = lambda x: x.DK_Projected_Points())[::-1]
    all_goalies = sorted(all_goalies, key = lambda x: x.DK_Projected_Points())[::-1]

    # Filter Players By Position
    all_centers = list(filter(lambda x: x.position == "C", all_skaters))
    all_wingers = list(filter(lambda x: x.position == "RW" or x.position == "LW", all_skaters))
    all_defence = list(filter(lambda x: x.position == "D", all_skaters))

    # Filter Out
    include_num = 13
    all_centers = all_centers[:include_num]
    all_wingers = all_wingers[:include_num]
    all_defence = all_defence[:include_num]

    # Write Players as small lists of relevant information
    all_centers = list(map(lambda x: [x.name, x.dk_salary, x.DK_Projected_Points(), x.team, x.opponent, x.position], all_centers))
    all_wingers = list(map(lambda x: [x.name, x.dk_salary, x.DK_Projected_Points(), x.team, x.opponent, x.position], all_wingers))
    all_defence = list(map(lambda x: [x.name, x.dk_salary, x.DK_Projected_Points(), x.team, x.opponent, x.position], all_defence))
    all_goalies = list(map(lambda x: [x.name, x.dk_salary, x.DK_Projected_Points(), x.team, x.opponent, x.position], all_goalies))

    # Goalie Combos
    goalie_combos = all_goalies[:3]
    # Combos set 1/2 FLEX W
    set1_C_combos = list(itertools.combinations(all_centers,2))
    set1_W_combos = list(itertools.combinations(all_wingers,4))
    # Combos set 2/2 FLEX C
    set2_C_combos = list(itertools.combinations(all_centers,3))
    set2_W_combos = list(itertools.combinations(all_wingers,3))
    set_D_combos = list(itertools.combinations(all_defence,2))

    # Write Player Lineups
    all_teams = []
    # Make Teams With Combo set 1/2
    for goalie in goalie_combos:
        this_team = []
        goalie_opponent = goalie[4]
        goalie = [goalie]
        # Filter Out Lines That Play Against The Goalie
        set_D_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set_D_combos)))
        set1_W_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set1_W_combos)))
        set1_C_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set1_C_combos)))
        for defencemen in set_D_combos_use:
            for wingers in set1_W_combos_use:
                for centers in set1_C_combos_use:
                    this_team = list(goalie) + list(defencemen) + list(wingers) + list(centers)
                    this_team = list(this_team) + get_team_stats_dk(this_team)
                    if this_team[11]:
                        all_teams += [this_team]
    # Make Teams With Combo set 2/2
    for goalie in goalie_combos:
        this_team = []
        goalie_opponent = goalie[4]
        goalie = [goalie]
        # Filter Out Lines That Play Against The Goalie
        set_D_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set_D_combos)))
        set2_W_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set2_W_combos)))
        set2_C_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set2_C_combos)))
        for defencemen in set_D_combos_use:
            for wingers in set2_W_combos_use:
                for centers in set2_C_combos_use:
                    this_team = list(goalie) + list(defencemen) + list(wingers) + list(centers)
                    this_team = list(this_team) + get_team_stats_dk(this_team)
                    if this_team[11]:
                        all_teams += [this_team]

    # Sort and reduce list to top 100 lineups
    top_100_teams = sorted(all_teams, key = lambda x: x[9])[::-1][:100]

    # Write Strings for .txt doc
    document_str = ""
    lineup_number = 1
    for team in top_100_teams:
        header = "Lineup %s\n\n" % (lineup_number)
        players_str = ""
        footer = "Team Cost: %s\n\nProjected Points: %s\n\n" % (str(team[10]), str(team[9]))
        for player in team[:9]:
            name = player[0]
            points = str(player[2])
            cost = str(player[1])
            position = player[5]
            players_str += "%s, %s | Projected Points: %s | Cost: %s\n\n" % (position, name, points, cost)
        doc_team = header + players_str + footer
        lineup_number += 1
        document_str += doc_team
    # Write File
    daily_skater = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/DraftKings_Lineups %s.txt" % (tag), 'w')
    daily_skater.write(document_str)
    daily_skater.close()


def Write_FD_Lineups(skaters, goalies, st, stu, turbo, tag):
    skaters = list(filter(lambda x: x.fd_position != "",skaters))
    # Early Start Time Fix
    skaters = Early_Start_Fix(skaters)
    goalies = Early_Start_Fix(goalies)
    # Filter Skaters By Start Time
    if turbo == "y":
        all_skaters = list(filter(lambda x: st <= x.start_time <= stu, skaters))
        all_goalies = list(filter(lambda x: st <= x.start_time <= stu, goalies))
    if turbo == "n":
        all_skaters = list(filter(lambda x: st <= x.start_time, skaters))
        all_goalies = list(filter(lambda x: st <= x.start_time, goalies))

    # Sort Players By Projected Points
    all_skaters = sorted(all_skaters, key = lambda x: x.FD_Projected_Points())[::-1]
    all_goalies = sorted(all_goalies, key = lambda x: x.FD_Projected_Points())[::-1]

    # Filter Players By Position
    all_centers = list(filter(lambda x: x.fd_position == "C", all_skaters))
    all_wingers = list(filter(lambda x: x.fd_position == "W", all_skaters))
    all_defence = list(filter(lambda x: x.fd_position == "D", all_skaters))

    # Filter Out
    include_num = 13
    all_centers = all_centers[:include_num]
    all_wingers = all_wingers[:include_num]
    all_defence = all_defence[:include_num]

    # Write Players as small lists of relevant information
    all_centers = list(map(lambda x: [x.name, x.fd_salary, x.FD_Projected_Points(), x.team, x.opponent, x.fd_position], all_centers))
    all_wingers = list(map(lambda x: [x.name, x.fd_salary, x.FD_Projected_Points(), x.team, x.opponent, x.fd_position], all_wingers))
    all_defence = list(map(lambda x: [x.name, x.fd_salary, x.FD_Projected_Points(), x.team, x.opponent, x.fd_position], all_defence))
    all_goalies = list(map(lambda x: [x.name, x.fd_salary, x.FD_Projected_Points(), x.team, x.opponent, x.position], all_goalies))

    # Goalie Combos
    goalie_combos = all_goalies[:3]
    # Combos set 1/2 FLEX W
    set1_C_combos = list(itertools.combinations(all_centers,2))
    set1_W_combos = list(itertools.combinations(all_wingers,4))
    set_D_combos = list(itertools.combinations(all_defence,2))

    # Write Player Lineups
    all_teams = []
    # Make Teams With Combo Set
    for goalie in goalie_combos:
        this_team = []
        goalie_opponent = goalie[4]
        goalie = [goalie]
        # Filter Out Lines That Play Against The Goalie
        set_D_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set_D_combos)))
        set1_W_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set1_W_combos)))
        set1_C_combos_use = list((filter(lambda x: goalie_opponent not in list(map(lambda y: y[3], x)), set1_C_combos)))
        for defencemen in set_D_combos_use:
            for wingers in set1_W_combos_use:
                for centers in set1_C_combos_use:
                    this_team = list(goalie) + list(defencemen) + list(wingers) + list(centers)
                    this_team = list(this_team) + get_team_stats_fd(this_team)
                    if this_team[11]:
                        all_teams += [this_team]

    # Sort and reduce list to top 100 lineups
    top_100_teams = sorted(all_teams, key = lambda x: x[9])[::-1][:100]

    # Write Strings for .txt doc
    document_str = ""
    lineup_number = 1
    for team in top_100_teams:
        header = "Lineup %s\n\n" % (lineup_number)
        players_str = ""
        footer = "Team Cost: %s\n\nProjected Points: %s\n\n" % (str(team[10]), str(team[9]))
        for player in team[:9]:
            name = player[0]
            points = str(player[2])
            cost = str(player[1])
            position = player[5]
            players_str += "%s, %s | Projected Points: %s | Cost: %s\n\n" % (position, name, points, cost)
        doc_team = header + players_str + footer
        lineup_number += 1
        document_str += doc_team
    # Write File
    daily_skater = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/FanDuel_Lineups %s.txt" % (tag), 'w')
    daily_skater.write(document_str)
    daily_skater.close()


def Write_Lineup_Files():
    print("Manual Excludes Are: " + str(manual_remove))
    site = input("Type 'FD' or 'DK' or 'both': ")
    tag = "[%s]" % (input("Insert Lineup Tag: "))
    turbo = input("Turbo Lineup? y/n?: ")

    if turbo == "y":
        start_time_low = float(input("Input Start Time Lower Bound: "))
        start_time_up = float(input("Input Start Time Upper Bound: "))
    if turbo == "n":
        start_time_low = float(input("Input Start Time: "))
        start_time_up = ""



    if site == "DK" or site == "both":
        Write_DK_Lineups(all_skaters, all_goalies, start_time_low, start_time_up, turbo, tag)
    if site == "FD" or site == "both":
        Write_FD_Lineups(all_skaters, all_goalies, start_time_low, start_time_up, turbo, tag)
