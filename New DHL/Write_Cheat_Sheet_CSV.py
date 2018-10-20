# Write Cheat Sheet CSV

import pickle, csv

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)
readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

injured = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Injured_Players.txt", "r")
injured = eval(injured.read())
starting = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/Starting_Goalies.txt", "r")
starting = eval(starting.read())

# Remove Injured / Non-Starting
all_skaters = list(filter(lambda x: x.name not in injured, all_skaters))
all_goalies = list(filter(lambda x: x.name not in injured and x.name in starting, all_goalies))


# Returns the players with the top X values in lop in form [Name, Value]
def topX_Value(lop, x):
    topx =  list(map(lambda n : str(n.name) + ", Value: " + str(n.Player_Value()) ,sorted(lop, key = lambda y : y.Player_Value())[::-1][:x]))
    if (len(topx) == x):
        return topx
    else:
        while (len(topx) < x):
            topx += [""]
        return topx

# Returns the players with the top X ceilings in form [Name, Ceiling]
def topX_Ceil(lop, x, site):
    if site == "DK":
        topx = list(map(lambda n : str(n.name) + ", Ceiling: " + str(n.dk_ceiling) ,sorted(lop, key = lambda y : y.dk_ceiling)[::-1][:x]))
    if site == "FD":
        topx = list(map(lambda n : str(n.name) + ", Ceiling: " + str(n.fd_ceiling) ,sorted(lop, key = lambda y : y.fd_ceiling)[::-1][:x]))
    if (len(topx) == x):
        return topx
    else:
        while (len(topx) < x):
            topx += [""]
        return topx

# Returns the players with the top X floor in form [Name, Floor]
def topX_Floor(lop, x, site):
    if site == "DK":
        topx = list(map(lambda n : str(n.name) + ", Floor: " + str(n.dk_floor) ,sorted(lop, key = lambda y : y.dk_floor)[::-1][:x]))
    if site == "FD":
        topx = list(map(lambda n : str(n.name) + ", Floor: " + str(n.fd_floor) ,sorted(lop, key = lambda y : y.fd_floor)[::-1][:x]))
    if (len(topx) == x):
        return topx
    else:
        while (len(topx) < x):
            topx += [""]
        return topx

# Draftkings Players by Position
dk_centers = list(filter((lambda x : x.position == "C"), all_skaters))
dk_wingers = list(filter((lambda x : x.position == "LW" or x.position == "RW"), all_skaters))
dk_defence = list(filter((lambda x : x.position == "D"), all_skaters))

# FanDuel Players by Position
fd_centers = list(filter((lambda x : x.fd_position == "C"), all_skaters))
fd_wingers = list(filter((lambda x : x.fd_position == "W"), all_skaters))
fd_defence = list(filter((lambda x : x.fd_position == "D"), all_skaters))

# DK Centers by Cost
dk_centers_tier1 = list(filter((lambda x : x.dk_salary >= 7000), dk_centers))
dk_centers_tier2 = list(filter((lambda x : 6000 <= x.dk_salary < 7000), dk_centers))
dk_centers_tier3 = list(filter((lambda x : 5000 <= x.dk_salary < 6000), dk_centers))
dk_centers_tier4 = list(filter((lambda x : 4000 <= x.dk_salary < 5000), dk_centers))
dk_centers_tier5 = list(filter((lambda x : 2500 <= x.dk_salary < 4000), dk_centers))

# DK Wingers by Cost
dk_wingers_tier1 = list(filter((lambda x : x.dk_salary >= 7000), dk_wingers))
dk_wingers_tier2 = list(filter((lambda x : 6000 <= x.dk_salary < 7000), dk_wingers))
dk_wingers_tier3 = list(filter((lambda x : 5000 <= x.dk_salary < 6000), dk_wingers))
dk_wingers_tier4 = list(filter((lambda x : 4000 <= x.dk_salary < 5000), dk_wingers))
dk_wingers_tier5 = list(filter((lambda x : 2500 <= x.dk_salary < 4000), dk_wingers))

# DK Defence by Cost
dk_defence_tier1 = list(filter((lambda x : x.dk_salary >= 7000), dk_defence))
dk_defence_tier2 = list(filter((lambda x : 6000 <= x.dk_salary < 7000), dk_defence))
dk_defence_tier3 = list(filter((lambda x : 5000 <= x.dk_salary < 6000), dk_defence))
dk_defence_tier4 = list(filter((lambda x : 4000 <= x.dk_salary < 5000), dk_defence))
dk_defence_tier5 = list(filter((lambda x : 2500 <= x.dk_salary < 4000), dk_defence))

# FD Centers by Cost
fd_centers_tier1 = list(filter((lambda x : x.fd_salary >= 7000), fd_centers))
fd_centers_tier2 = list(filter((lambda x : 6000 <= x.fd_salary < 7000), fd_centers))
fd_centers_tier3 = list(filter((lambda x : 5000 <= x.fd_salary < 6000), fd_centers))
fd_centers_tier4 = list(filter((lambda x : 4000 <= x.fd_salary < 5000), fd_centers))
fd_centers_tier5 = list(filter((lambda x : 3000 <= x.fd_salary < 4000), fd_centers))

# FD Wingers by Cost
fd_wingers_tier1 = list(filter((lambda x : x.fd_salary >= 7000), fd_wingers))
fd_wingers_tier2 = list(filter((lambda x : 6000 <= x.fd_salary < 7000), fd_wingers))
fd_wingers_tier3 = list(filter((lambda x : 5000 <= x.fd_salary < 6000), fd_wingers))
fd_wingers_tier4 = list(filter((lambda x : 4000 <= x.fd_salary < 5000), fd_wingers))
fd_wingers_tier5 = list(filter((lambda x : 3000 <= x.fd_salary < 4000), fd_wingers))

# FD Defence by Cost
fd_defence_tier1 = list(filter((lambda x : x.fd_salary >= 7000), fd_defence))
fd_defence_tier2 = list(filter((lambda x : 6000 <= x.fd_salary < 7000), fd_defence))
fd_defence_tier3 = list(filter((lambda x : 5000 <= x.fd_salary < 6000), fd_defence))
fd_defence_tier4 = list(filter((lambda x : 4000 <= x.fd_salary < 5000), fd_defence))
fd_defence_tier5 = list(filter((lambda x : 3000 <= x.fd_salary < 4000), fd_defence))

# DK High Ceiling / Floor
dk_c_ceiling = topX_Ceil(dk_centers, 5, "DK")
dk_w_ceiling = topX_Ceil(dk_wingers, 5, "DK")
dk_d_ceiling = topX_Ceil(dk_defence, 5, "DK")
dk_c_floor = topX_Floor(dk_centers, 5, "DK")
dk_w_floor = topX_Floor(dk_wingers, 5, "DK")
dk_d_floor = topX_Floor(dk_defence, 5, "DK")

# FD High Ceiling / Floor
fd_c_ceiling = topX_Ceil(fd_centers, 5, "FD")
fd_w_ceiling = topX_Ceil(fd_wingers, 5, "FD")
fd_d_ceiling = topX_Ceil(fd_defence, 5, "FD")
fd_c_floor = topX_Floor(fd_centers, 5, "FD")
fd_w_floor = topX_Floor(fd_wingers, 5, "FD")
fd_d_floor = topX_Floor(fd_defence, 5, "FD")

topx_mult = 5

# DK Value Top X's
dk_cv_t1 = topX_Value(dk_centers_tier1, topx_mult)
dk_cv_t2 = topX_Value(dk_centers_tier2, topx_mult)
dk_cv_t3 = topX_Value(dk_centers_tier3, topx_mult)
dk_cv_t4 = topX_Value(dk_centers_tier4, topx_mult)
dk_cv_t5 = topX_Value(dk_centers_tier5, topx_mult)
dk_wv_t1 = topX_Value(dk_wingers_tier1, topx_mult)
dk_wv_t2 = topX_Value(dk_wingers_tier2, topx_mult)
dk_wv_t3 = topX_Value(dk_wingers_tier3, topx_mult)
dk_wv_t4 = topX_Value(dk_wingers_tier4, topx_mult)
dk_wv_t5 = topX_Value(dk_wingers_tier5, topx_mult)
dk_dv_t1 = topX_Value(dk_defence_tier1, topx_mult)
dk_dv_t2 = topX_Value(dk_defence_tier2, topx_mult)
dk_dv_t3 = topX_Value(dk_defence_tier3, topx_mult)
dk_dv_t4 = topX_Value(dk_defence_tier4, topx_mult)
dk_dv_t5 = topX_Value(dk_defence_tier5, topx_mult)
# FD Value Top X's
fd_cv_t1 = topX_Value(fd_centers_tier1, topx_mult)
fd_cv_t2 = topX_Value(fd_centers_tier2, topx_mult)
fd_cv_t3 = topX_Value(fd_centers_tier3, topx_mult)
fd_cv_t4 = topX_Value(fd_centers_tier4, topx_mult)
fd_cv_t5 = topX_Value(fd_centers_tier5, topx_mult)
fd_wv_t1 = topX_Value(fd_wingers_tier1, topx_mult)
fd_wv_t2 = topX_Value(fd_wingers_tier2, topx_mult)
fd_wv_t3 = topX_Value(fd_wingers_tier3, topx_mult)
fd_wv_t4 = topX_Value(fd_wingers_tier4, topx_mult)
fd_wv_t5 = topX_Value(fd_wingers_tier5, topx_mult)
fd_dv_t1 = topX_Value(fd_defence_tier1, topx_mult)
fd_dv_t2 = topX_Value(fd_defence_tier2, topx_mult)
fd_dv_t3 = topX_Value(fd_defence_tier3, topx_mult)
fd_dv_t4 = topX_Value(fd_defence_tier4, topx_mult)
fd_dv_t5 = topX_Value(fd_defence_tier5, topx_mult)

# DK Ceiling Top X's
dk_cc_t1 = topX_Ceil(dk_centers_tier1, topx_mult, "DK")
dk_cc_t2 = topX_Ceil(dk_centers_tier2, topx_mult, "DK")
dk_cc_t3 = topX_Ceil(dk_centers_tier3, topx_mult, "DK")
dk_cc_t4 = topX_Ceil(dk_centers_tier4, topx_mult, "DK")
dk_cc_t5 = topX_Ceil(dk_centers_tier5, topx_mult, "DK")
dk_wc_t1 = topX_Ceil(dk_wingers_tier1, topx_mult, "DK")
dk_wc_t2 = topX_Ceil(dk_wingers_tier2, topx_mult, "DK")
dk_wc_t3 = topX_Ceil(dk_wingers_tier3, topx_mult, "DK")
dk_wc_t4 = topX_Ceil(dk_wingers_tier4, topx_mult, "DK")
dk_wc_t5 = topX_Ceil(dk_wingers_tier5, topx_mult, "DK")
dk_dc_t1 = topX_Ceil(dk_defence_tier1, topx_mult, "DK")
dk_dc_t2 = topX_Ceil(dk_defence_tier2, topx_mult, "DK")
dk_dc_t3 = topX_Ceil(dk_defence_tier3, topx_mult, "DK")
dk_dc_t4 = topX_Ceil(dk_defence_tier4, topx_mult, "DK")
dk_dc_t5 = topX_Ceil(dk_defence_tier5, topx_mult, "DK")
# FD Ceiling Top X's
fd_cc_t1 = topX_Ceil(fd_centers_tier1, topx_mult, "FD")
fd_cc_t2 = topX_Ceil(fd_centers_tier2, topx_mult, "FD")
fd_cc_t3 = topX_Ceil(fd_centers_tier3, topx_mult, "FD")
fd_cc_t4 = topX_Ceil(fd_centers_tier4, topx_mult, "FD")
fd_cc_t5 = topX_Ceil(fd_centers_tier5, topx_mult, "FD")
fd_wc_t1 = topX_Ceil(fd_wingers_tier1, topx_mult, "FD")
fd_wc_t2 = topX_Ceil(fd_wingers_tier2, topx_mult, "FD")
fd_wc_t3 = topX_Ceil(fd_wingers_tier3, topx_mult, "FD")
fd_wc_t4 = topX_Ceil(fd_wingers_tier4, topx_mult, "FD")
fd_wc_t5 = topX_Ceil(fd_wingers_tier5, topx_mult, "FD")
fd_dc_t1 = topX_Ceil(fd_defence_tier1, topx_mult, "FD")
fd_dc_t2 = topX_Ceil(fd_defence_tier2, topx_mult, "FD")
fd_dc_t3 = topX_Ceil(fd_defence_tier3, topx_mult, "FD")
fd_dc_t4 = topX_Ceil(fd_defence_tier4, topx_mult, "FD")
fd_dc_t5 = topX_Ceil(fd_defence_tier5, topx_mult, "FD")

# DK Floor Top X's
dk_cf_t1 = topX_Floor(dk_centers_tier1, topx_mult, "DK")
dk_cf_t2 = topX_Floor(dk_centers_tier2, topx_mult, "DK")
dk_cf_t3 = topX_Floor(dk_centers_tier3, topx_mult, "DK")
dk_cf_t4 = topX_Floor(dk_centers_tier4, topx_mult, "DK")
dk_cf_t5 = topX_Floor(dk_centers_tier5, topx_mult, "DK")
dk_wf_t1 = topX_Floor(dk_wingers_tier1, topx_mult, "DK")
dk_wf_t2 = topX_Floor(dk_wingers_tier2, topx_mult, "DK")
dk_wf_t3 = topX_Floor(dk_wingers_tier3, topx_mult, "DK")
dk_wf_t4 = topX_Floor(dk_wingers_tier4, topx_mult, "DK")
dk_wf_t5 = topX_Floor(dk_wingers_tier5, topx_mult, "DK")
dk_df_t1 = topX_Floor(dk_defence_tier1, topx_mult, "DK")
dk_df_t2 = topX_Floor(dk_defence_tier2, topx_mult, "DK")
dk_df_t3 = topX_Floor(dk_defence_tier3, topx_mult, "DK")
dk_df_t4 = topX_Floor(dk_defence_tier4, topx_mult, "DK")
dk_df_t5 = topX_Floor(dk_defence_tier5, topx_mult, "DK")
# FD Floor Top X's
fd_cf_t1 = topX_Floor(fd_centers_tier1, topx_mult, "FD")
fd_cf_t2 = topX_Floor(fd_centers_tier2, topx_mult, "FD")
fd_cf_t3 = topX_Floor(fd_centers_tier3, topx_mult, "FD")
fd_cf_t4 = topX_Floor(fd_centers_tier4, topx_mult, "FD")
fd_cf_t5 = topX_Floor(fd_centers_tier5, topx_mult, "FD")
fd_wf_t1 = topX_Floor(fd_wingers_tier1, topx_mult, "FD")
fd_wf_t2 = topX_Floor(fd_wingers_tier2, topx_mult, "FD")
fd_wf_t3 = topX_Floor(fd_wingers_tier3, topx_mult, "FD")
fd_wf_t4 = topX_Floor(fd_wingers_tier4, topx_mult, "FD")
fd_wf_t5 = topX_Floor(fd_wingers_tier5, topx_mult, "FD")
fd_df_t1 = topX_Floor(fd_defence_tier1, topx_mult, "FD")
fd_df_t2 = topX_Floor(fd_defence_tier2, topx_mult, "FD")
fd_df_t3 = topX_Floor(fd_defence_tier3, topx_mult, "FD")
fd_df_t4 = topX_Floor(fd_defence_tier4, topx_mult, "FD")
fd_df_t5 = topX_Floor(fd_defence_tier5, topx_mult, "FD")

# Goalie Variables
dk_gv = topX_Value(all_goalies,topx_mult)
fd_gv = topX_Value(all_goalies,topx_mult)




## Info width: 16
##      length: 69

# Write the CSV File

row1 = ["DHL Daily Fantasy Cheet Sheet","","DailyHockeyLineups.com","","","","","","","","","","","","",""]
row2 = ["","DraftKings","","","","","","","FanDuel","","","","","","Legend",""]
row3 = ["","","","","","","","","","","","","","","Tier 1: a player that costs >= 7000",""]
row4 = ["","Tier 1","Tier 2","Tier 3","Tier 4","Tier 5","","","Tier 1","Tier 2","Tier 3","Tier 4","Tier 5","","Tier 2: a player where (6000 <= costs < 7000)",""]
row5 = ["","Top 5 Centers (PV)","","","","","","","Top 5 Centers (PV)","","","","","","Tier 3: a player where (5000 <= costs < 6000)",""]
row6 = ["",dk_cv_t1[0],dk_cv_t2[0],dk_cv_t3[0],dk_cv_t4[0],dk_cv_t5[0],"","",
        fd_cv_t1[0],fd_cv_t2[0],fd_cv_t3[0],fd_cv_t4[0],fd_cv_t5[0],"","Tier 4: a player where (4000 <= costs < 5000)",""]
row7 = ["",dk_cv_t1[1],dk_cv_t2[1],dk_cv_t3[1],dk_cv_t4[1],dk_cv_t5[1],"","",
        fd_cv_t1[1],fd_cv_t2[1],fd_cv_t3[1],fd_cv_t4[1],fd_cv_t5[1],"","Tier 5: a player where (2500 <= costs < 4000)",""]
row8 = ["",dk_cv_t1[2],dk_cv_t2[2],dk_cv_t3[2],dk_cv_t4[2],dk_cv_t5[2],"","",
        fd_cv_t1[2],fd_cv_t2[2],fd_cv_t3[2],fd_cv_t4[2],fd_cv_t5[2],"","PV : Player Value (Calculated as expected points / cost)",""]
row9 = ["",dk_cv_t1[3],dk_cv_t2[3],dk_cv_t3[3],dk_cv_t4[3],dk_cv_t5[3],"","",
        fd_cv_t1[3],fd_cv_t2[3],fd_cv_t3[3],fd_cv_t4[3],fd_cv_t5[3],"","Ceiling : The average of the top 10% of the games the player has played this season.",""]
row10 = ["",dk_cv_t1[4],dk_cv_t2[4],dk_cv_t3[4],dk_cv_t4[4],dk_cv_t5[4],"","",
        fd_cv_t1[4],fd_cv_t2[4],fd_cv_t3[4],fd_cv_t4[4],fd_cv_t5[4],"","Floor : The worst a player has preformed in their last ten games.",""]
row11 = ["","Top 5 Wingers (PV)","","","","","","","Top 5 Wingers (PV)","","","","","","",""]
row12 = ["",dk_wv_t1[0],dk_wv_t2[0],dk_wv_t3[0],dk_wv_t4[0],dk_wv_t5[0],"","",
         fd_wv_t1[0],fd_wv_t2[0],fd_wv_t3[0],fd_wv_t4[0],fd_wv_t5[0],"","",""]
row13 = ["",dk_wv_t1[1],dk_wv_t2[1],dk_wv_t3[1],dk_wv_t4[1],dk_wv_t5[1],"","",
         fd_wv_t1[1],fd_wv_t2[1],fd_wv_t3[1],fd_wv_t4[1],fd_wv_t5[1],"","",""]
row14 = ["",dk_wv_t1[2],dk_wv_t2[2],dk_wv_t3[2],dk_wv_t4[2],dk_wv_t5[2],"","",
         fd_wv_t1[2],fd_wv_t2[2],fd_wv_t3[2],fd_wv_t4[2],fd_wv_t5[2],"","",""]
row15 = ["",dk_wv_t1[3],dk_wv_t2[3],dk_wv_t3[3],dk_wv_t4[3],dk_wv_t5[3],"","",
         fd_wv_t1[3],fd_wv_t2[3],fd_wv_t3[3],fd_wv_t4[3],fd_wv_t5[3],"","",""]
row16 = ["",dk_wv_t1[4],dk_wv_t2[4],dk_wv_t3[4],dk_wv_t4[4],dk_wv_t5[4],"","",
         fd_wv_t1[4],fd_wv_t2[4],fd_wv_t3[4],fd_wv_t4[4],fd_wv_t5[4],"","",""]
row17 = ["","Top 5 Defenceman (PV)","","","","","","","Top 5 Defenceman (PV)","","","","","","",""]
row18 = ["",dk_dv_t1[0],dk_dv_t2[0],dk_dv_t3[0],dk_dv_t4[0],dk_dv_t5[0],"","",
         fd_dv_t1[0],fd_dv_t2[0],fd_dv_t3[0],fd_dv_t4[0],fd_dv_t5[0],"","",""]
row19 = ["",dk_dv_t1[1],dk_dv_t2[1],dk_dv_t3[1],dk_dv_t4[1],dk_dv_t5[1],"","",
         fd_dv_t1[1],fd_dv_t2[1],fd_dv_t3[1],fd_dv_t4[1],fd_dv_t5[1],"","",""]
row20 = ["",dk_dv_t1[2],dk_dv_t2[2],dk_dv_t3[2],dk_dv_t4[2],dk_dv_t5[2],"","",
         fd_dv_t1[2],fd_dv_t2[2],fd_dv_t3[2],fd_dv_t4[2],fd_dv_t5[2],"","",""]
row21 = ["",dk_dv_t1[3],dk_dv_t2[3],dk_dv_t3[3],dk_dv_t4[3],dk_dv_t5[3],"","",
         fd_dv_t1[3],fd_dv_t2[3],fd_dv_t3[3],fd_dv_t4[3],fd_dv_t5[3],"","",""]
row22 = ["",dk_dv_t1[4],dk_dv_t2[4],dk_dv_t3[4],dk_dv_t4[4],dk_dv_t5[4],"","",
         fd_dv_t1[4],fd_dv_t2[4],fd_dv_t3[4],fd_dv_t4[4],fd_dv_t5[4],"","",""]
row23 = ["","","","","","","","","","","","","","","",""]
row24 = ["","High Ceiling Centers","","","","","","","High Ceiling Centers","","","","","","",""]
row25 = ["",dk_cc_t1[0],dk_cc_t2[0],dk_cc_t3[0],dk_cc_t4[0],dk_cc_t5[0],"","",
         fd_cc_t1[0],fd_cc_t2[0],fd_cc_t3[0],fd_cc_t4[0],fd_cc_t5[0],"","",""]
row26 = ["",dk_cc_t1[1],dk_cc_t2[1],dk_cc_t3[1],dk_cc_t4[1],dk_cc_t5[1],"","",
         fd_cc_t1[1],fd_cc_t2[1],fd_cc_t3[1],fd_cc_t4[1],fd_cc_t5[1],"","",""]
row27 = ["",dk_cc_t1[2],dk_cc_t2[2],dk_cc_t3[2],dk_cc_t4[2],dk_cc_t5[2],"","",
         fd_cc_t1[2],fd_cc_t2[2],fd_cc_t3[2],fd_cc_t4[2],fd_cc_t5[2],"","",""]
row28 = ["",dk_cc_t1[3],dk_cc_t2[3],dk_cc_t3[3],dk_cc_t4[3],dk_cc_t5[3],"","",
         fd_cc_t1[3],fd_cc_t2[3],fd_cc_t3[3],fd_cc_t4[3],fd_cc_t5[3],"","",""]
row29 = ["",dk_cc_t1[4],dk_cc_t2[4],dk_cc_t3[4],dk_cc_t4[4],dk_cc_t5[4],"","",
         fd_cc_t1[4],fd_cc_t2[4],fd_cc_t3[4],fd_cc_t4[4],fd_cc_t5[4],"","",""]
row30 = ["","High Ceiling Wingers","","","","","","","High Ceiling Wingers","","","","","","",""]
row31 = ["",dk_wc_t1[0],dk_wc_t2[0],dk_wc_t3[0],dk_wc_t4[0],dk_wc_t5[0],"","",
         fd_wc_t1[0],fd_wc_t2[0],fd_wc_t3[0],fd_wc_t4[0],fd_wc_t5[0],"","",""]
row32 = ["",dk_wc_t1[1],dk_wc_t2[1],dk_wc_t3[1],dk_wc_t4[1],dk_wc_t5[1],"","",
         fd_wc_t1[1],fd_wc_t2[1],fd_wc_t3[1],fd_wc_t4[1],fd_wc_t5[1],"","",""]
row33 = ["",dk_wc_t1[2],dk_wc_t2[2],dk_wc_t3[2],dk_wc_t4[2],dk_wc_t5[2],"","",
         fd_wc_t1[2],fd_wc_t2[2],fd_wc_t3[2],fd_wc_t4[2],fd_wc_t5[2],"","",""]
row34 = ["",dk_wc_t1[3],dk_wc_t2[3],dk_wc_t3[3],dk_wc_t4[3],dk_wc_t5[3],"","",
         fd_wc_t1[3],fd_wc_t2[3],fd_wc_t3[3],fd_wc_t4[3],fd_wc_t5[3],"","",""]
row35 = ["",dk_wc_t1[4],dk_wc_t2[4],dk_wc_t3[4],dk_wc_t4[4],dk_wc_t5[4],"","",
         fd_wc_t1[4],fd_wc_t2[4],fd_wc_t3[4],fd_wc_t4[4],fd_wc_t5[4],"","",""]
row36 = ["","High Ceiling Defenceman","","","","","","","High Ceiling Defenceman","","","","","","",""]
row37 = ["",dk_dc_t1[0],dk_dc_t2[0],dk_dc_t3[0],dk_dc_t4[0],dk_dc_t5[0],"","",
         fd_dc_t1[0],fd_dc_t2[0],fd_dc_t3[0],fd_dc_t4[0],fd_dc_t5[0],"","",""]
row38 = ["",dk_dc_t1[1],dk_dc_t2[1],dk_dc_t3[1],dk_dc_t4[1],dk_dc_t5[1],"","",
         fd_dc_t1[1],fd_dc_t2[1],fd_dc_t3[1],fd_dc_t4[1],fd_dc_t5[1],"","",""]
row39 = ["",dk_dc_t1[2],dk_dc_t2[2],dk_dc_t3[2],dk_dc_t4[2],dk_dc_t5[2],"","",
         fd_dc_t1[2],fd_dc_t2[2],fd_dc_t3[2],fd_dc_t4[2],fd_dc_t5[2],"","",""]
row40 = ["",dk_dc_t1[3],dk_dc_t2[3],dk_dc_t3[3],dk_dc_t4[3],dk_dc_t5[3],"","",
         fd_dc_t1[3],fd_dc_t2[3],fd_dc_t3[3],fd_dc_t4[3],fd_dc_t5[3],"","",""]
row41 = ["",dk_dc_t1[4],dk_dc_t2[4],dk_dc_t3[4],dk_dc_t4[4],dk_dc_t5[4],"","",
         fd_dc_t1[4],fd_dc_t2[4],fd_dc_t3[4],fd_dc_t4[4],fd_dc_t5[4],"","",""]
row42 = ["","","","","","","","","","","","","","","",""]
row43 = ["","High Floor Centers","","","","","","","High Floor Centers","","","","","","",""]
row44 = ["",dk_cf_t1[0],dk_cf_t2[0],dk_cf_t3[0],dk_cf_t4[0],dk_cf_t5[0],"","",
         fd_cf_t1[0],fd_cf_t2[0],fd_cf_t3[0],fd_cf_t4[0],fd_cf_t5[0],"","",""]
row45 = ["",dk_cf_t1[1],dk_cf_t2[1],dk_cf_t3[1],dk_cf_t4[1],dk_cf_t5[1],"","",
         fd_cf_t1[1],fd_cf_t2[1],fd_cf_t3[1],fd_cf_t4[1],fd_cf_t5[1],"","",""]
row46 = ["",dk_cf_t1[2],dk_cf_t2[2],dk_cf_t3[2],dk_cf_t4[2],dk_cf_t5[2],"","",
         fd_cf_t1[2],fd_cf_t2[2],fd_cf_t3[2],fd_cf_t4[2],fd_cf_t5[2],"","",""]
row47 = ["",dk_cf_t1[3],dk_cf_t2[3],dk_cf_t3[3],dk_cf_t4[3],dk_cf_t5[3],"","",
         fd_cf_t1[3],fd_cf_t2[3],fd_cf_t3[3],fd_cf_t4[3],fd_cf_t5[3],"","",""]
row48 = ["",dk_cf_t1[4],dk_cf_t2[4],dk_cf_t3[4],dk_cf_t4[4],dk_cf_t5[4],"","",
         fd_cf_t1[4],fd_cf_t2[4],fd_cf_t3[4],fd_cf_t4[4],fd_cf_t5[4],"","",""]
row49 = ["","High Floor Wingers","","","","","","","High Floor Wingers","","","","","","",""]
row50 = ["",dk_wf_t1[0],dk_wf_t2[0],dk_wf_t3[0],dk_wf_t4[0],dk_wf_t5[0],"","",
         fd_wf_t1[0],fd_wf_t2[0],fd_wf_t3[0],fd_wf_t4[0],fd_wf_t5[0],"","",""]
row51 = ["",dk_wf_t1[1],dk_wf_t2[1],dk_wf_t3[1],dk_wf_t4[1],dk_wf_t5[1],"","",
         fd_wf_t1[1],fd_wf_t2[1],fd_wf_t3[1],fd_wf_t4[1],fd_wf_t5[1],"","",""]
row52 = ["",dk_wf_t1[2],dk_wf_t2[2],dk_wf_t3[2],dk_wf_t4[2],dk_wf_t5[2],"","",
         fd_wf_t1[2],fd_wf_t2[2],fd_wf_t3[2],fd_wf_t4[2],fd_wf_t5[2],"","",""]
row53 = ["",dk_wf_t1[3],dk_wf_t2[3],dk_wf_t3[3],dk_wf_t4[3],dk_wf_t5[3],"","",
         fd_wf_t1[3],fd_wf_t2[3],fd_wf_t3[3],fd_wf_t4[3],fd_wf_t5[3],"","",""]
row54 = ["",dk_wf_t1[4],dk_wf_t2[4],dk_wf_t3[4],dk_wf_t4[4],dk_wf_t5[4],"","",
         fd_wf_t1[4],fd_wf_t2[4],fd_wf_t3[4],fd_wf_t4[4],fd_wf_t5[4],"","",""]
row55 = ["","High Floor Defenceman","","","","","","","High Floor Defenceman","","","","","","",""]
row56 = ["",dk_df_t1[0],dk_df_t2[0],dk_df_t3[0],dk_df_t4[0],dk_df_t5[0],"","",
         fd_df_t1[0],fd_df_t2[0],fd_df_t3[0],fd_df_t4[0],fd_df_t5[0],"","",""]
row57 = ["",dk_df_t1[1],dk_df_t2[1],dk_df_t3[1],dk_df_t4[1],dk_df_t5[1],"","",
         fd_df_t1[1],fd_df_t2[1],fd_df_t3[1],fd_df_t4[1],fd_df_t5[1],"","",""]
row58 = ["",dk_df_t1[2],dk_df_t2[2],dk_df_t3[2],dk_df_t4[2],dk_df_t5[2],"","",
         fd_df_t1[2],fd_df_t2[2],fd_df_t3[2],fd_df_t4[2],fd_df_t5[2],"","",""]
row59 = ["",dk_df_t1[3],dk_df_t2[3],dk_df_t3[3],dk_df_t4[3],dk_df_t5[3],"","",
         fd_df_t1[3],fd_df_t2[3],fd_df_t3[3],fd_df_t4[3],fd_df_t5[3],"","",""]
row60 = ["",dk_df_t1[4],dk_df_t2[4],dk_df_t3[4],dk_df_t4[4],dk_df_t5[4],"","",
         fd_df_t1[4],fd_df_t2[4],fd_df_t3[4],fd_df_t4[4],fd_df_t5[4],"","",""]
row61 = ["","","","","","","","","","","","","","","",""]
row62 = ["","Goalies","","","","","","","Goalies","","","","","","",""]
row63 = ["","Top 5 Goalies (PV)","","","","","","","Top 5 Goalies (PV)","","","","","","",""]
row64 = ["",dk_gv[0],"","","","","","",dk_gv[0],"","","","","","",""]
row65 = ["",dk_gv[1],"","","","","","",dk_gv[1],"","","","","","",""]
row66 = ["",dk_gv[2],"","","","","","",dk_gv[2],"","","","","","",""]
row67 = ["",dk_gv[3],"","","","","","",dk_gv[3],"","","","","","",""]
row68 = ["",dk_gv[4],"","","","","","",dk_gv[4],"","","","","","",""]
row69 = ["","","","","","","","","","","","","","",""," "]

def write_Cheat_Sheet():
    cs_doc = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/DHL Cheat Sheet.csv", 'w')
    cs_doc_writer = csv.writer(cs_doc)
    cs_doc_writer.writerow(row1)
    cs_doc_writer.writerow(row2)
    cs_doc_writer.writerow(row3)
    cs_doc_writer.writerow(row4)
    cs_doc_writer.writerow(row5)
    cs_doc_writer.writerow(row6)
    cs_doc_writer.writerow(row7)
    cs_doc_writer.writerow(row8)
    cs_doc_writer.writerow(row9)
    cs_doc_writer.writerow(row10)
    cs_doc_writer.writerow(row11)
    cs_doc_writer.writerow(row12)
    cs_doc_writer.writerow(row13)
    cs_doc_writer.writerow(row14)
    cs_doc_writer.writerow(row15)
    cs_doc_writer.writerow(row16)
    cs_doc_writer.writerow(row17)
    cs_doc_writer.writerow(row18)
    cs_doc_writer.writerow(row19)
    cs_doc_writer.writerow(row20)
    cs_doc_writer.writerow(row21)
    cs_doc_writer.writerow(row22)
    cs_doc_writer.writerow(row23)
    cs_doc_writer.writerow(row24)
    cs_doc_writer.writerow(row25)
    cs_doc_writer.writerow(row26)
    cs_doc_writer.writerow(row27)
    cs_doc_writer.writerow(row28)
    cs_doc_writer.writerow(row29)
    cs_doc_writer.writerow(row30)
    cs_doc_writer.writerow(row31)
    cs_doc_writer.writerow(row32)
    cs_doc_writer.writerow(row33)
    cs_doc_writer.writerow(row34)
    cs_doc_writer.writerow(row35)
    cs_doc_writer.writerow(row36)
    cs_doc_writer.writerow(row37)
    cs_doc_writer.writerow(row38)
    cs_doc_writer.writerow(row39)
    cs_doc_writer.writerow(row40)
    cs_doc_writer.writerow(row41)
    cs_doc_writer.writerow(row42)
    cs_doc_writer.writerow(row43)
    cs_doc_writer.writerow(row44)
    cs_doc_writer.writerow(row45)
    cs_doc_writer.writerow(row46)
    cs_doc_writer.writerow(row47)
    cs_doc_writer.writerow(row48)
    cs_doc_writer.writerow(row49)
    cs_doc_writer.writerow(row50)
    cs_doc_writer.writerow(row51)
    cs_doc_writer.writerow(row52)
    cs_doc_writer.writerow(row53)
    cs_doc_writer.writerow(row54)
    cs_doc_writer.writerow(row55)
    cs_doc_writer.writerow(row56)
    cs_doc_writer.writerow(row57)
    cs_doc_writer.writerow(row58)
    cs_doc_writer.writerow(row59)
    cs_doc_writer.writerow(row60)
    cs_doc_writer.writerow(row61)
    cs_doc_writer.writerow(row62)
    cs_doc_writer.writerow(row63)
    cs_doc_writer.writerow(row64)
    cs_doc_writer.writerow(row65)
    cs_doc_writer.writerow(row66)
    cs_doc_writer.writerow(row67)
    cs_doc_writer.writerow(row68)
    cs_doc_writer.writerow(row69)
    cs_doc.close

def write_Cheat_Sheet_Printable():
    cs_doc = open("/Users/nathansaccon/Documents/Coding/New DHL/Output Files/DHL Cheat Sheet PRINTABLE.csv", 'w')
    cs_doc_writer = csv.writer(cs_doc)
    cs_doc_writer.writerow(row1[:7])
    cs_doc_writer.writerow(row2[:7])
    cs_doc_writer.writerow(row3[:7])
    cs_doc_writer.writerow(row4[:7])
    cs_doc_writer.writerow(row5[:7])
    cs_doc_writer.writerow(row6[:7])
    cs_doc_writer.writerow(row7[:7])
    cs_doc_writer.writerow(row8[:7])
    cs_doc_writer.writerow(row9[:7])
    cs_doc_writer.writerow(row10[:7])
    cs_doc_writer.writerow(row11[:7])
    cs_doc_writer.writerow(row12[:7])
    cs_doc_writer.writerow(row13[:7])
    cs_doc_writer.writerow(row14[:7])
    cs_doc_writer.writerow(row15[:7])
    cs_doc_writer.writerow(row16[:7])
    cs_doc_writer.writerow(row17[:7])
    cs_doc_writer.writerow(row18[:7])
    cs_doc_writer.writerow(row19[:7])
    cs_doc_writer.writerow(row20[:7])
    cs_doc_writer.writerow(row21[:7])
    cs_doc_writer.writerow(row22[:7])
    cs_doc_writer.writerow(row23[:7])
    cs_doc_writer.writerow(row24[:7])
    cs_doc_writer.writerow(row25[:7])
    cs_doc_writer.writerow(row26[:7])
    cs_doc_writer.writerow(row27[:7])
    cs_doc_writer.writerow(row28[:7])
    cs_doc_writer.writerow(row29[:7])
    cs_doc_writer.writerow(row30[:7])
    cs_doc_writer.writerow(row31[:7])
    cs_doc_writer.writerow(row32[:7])
    cs_doc_writer.writerow(row33[:7])
    cs_doc_writer.writerow(row34[:7])
    cs_doc_writer.writerow(row35[:7])
    cs_doc_writer.writerow(row36[:7])
    cs_doc_writer.writerow(row37[:7])
    cs_doc_writer.writerow(row38[:7])
    cs_doc_writer.writerow(row39[:7])
    cs_doc_writer.writerow(row40[:7])
    cs_doc_writer.writerow(row41[:7])
    cs_doc_writer.writerow(row42[:7])
    cs_doc_writer.writerow(row43[:7])
    cs_doc_writer.writerow(row44[:7])
    cs_doc_writer.writerow(row45[:7])
    cs_doc_writer.writerow(row46[:7])
    cs_doc_writer.writerow(row47[:7])
    cs_doc_writer.writerow(row48[:7])
    cs_doc_writer.writerow(row49[:7])
    cs_doc_writer.writerow(row50[:7])
    cs_doc_writer.writerow(row51[:7])
    cs_doc_writer.writerow(row52[:7])
    cs_doc_writer.writerow(row53[:7])
    cs_doc_writer.writerow(row54[:7])
    cs_doc_writer.writerow(row55[:7])
    cs_doc_writer.writerow(row56[:7])
    cs_doc_writer.writerow(row57[:7])
    cs_doc_writer.writerow(row58[:7])
    cs_doc_writer.writerow(row59[:7])
    cs_doc_writer.writerow(row60[:7])
    cs_doc_writer.writerow(row61[:7])
    cs_doc_writer.writerow(row62[:7])
    cs_doc_writer.writerow(row63[:7])
    cs_doc_writer.writerow(row64[:7])
    cs_doc_writer.writerow(row65[:7])
    cs_doc_writer.writerow(row66[:7])
    cs_doc_writer.writerow(row67[:7])
    cs_doc_writer.writerow(row68[:7])
    cs_doc_writer.writerow(row69[:7])
    cs_doc_writer.writerow(row2[7:14])
    cs_doc_writer.writerow(row3[7:14])
    cs_doc_writer.writerow(row4[7:14])
    cs_doc_writer.writerow(row5[7:14])
    cs_doc_writer.writerow(row6[7:14])
    cs_doc_writer.writerow(row7[7:14])
    cs_doc_writer.writerow(row8[7:14])
    cs_doc_writer.writerow(row9[7:14])
    cs_doc_writer.writerow(row10[7:14])
    cs_doc_writer.writerow(row11[7:14])
    cs_doc_writer.writerow(row12[7:14])
    cs_doc_writer.writerow(row13[7:14])
    cs_doc_writer.writerow(row14[7:14])
    cs_doc_writer.writerow(row15[7:14])
    cs_doc_writer.writerow(row16[7:14])
    cs_doc_writer.writerow(row17[7:14])
    cs_doc_writer.writerow(row18[7:14])
    cs_doc_writer.writerow(row19[7:14])
    cs_doc_writer.writerow(row20[7:14])
    cs_doc_writer.writerow(row21[7:14])
    cs_doc_writer.writerow(row22[7:14])
    cs_doc_writer.writerow(row23[7:14])
    cs_doc_writer.writerow(row24[7:14])
    cs_doc_writer.writerow(row25[7:14])
    cs_doc_writer.writerow(row26[7:14])
    cs_doc_writer.writerow(row27[7:14])
    cs_doc_writer.writerow(row28[7:14])
    cs_doc_writer.writerow(row29[7:14])
    cs_doc_writer.writerow(row30[7:14])
    cs_doc_writer.writerow(row31[7:14])
    cs_doc_writer.writerow(row32[7:14])
    cs_doc_writer.writerow(row33[7:14])
    cs_doc_writer.writerow(row34[7:14])
    cs_doc_writer.writerow(row35[7:14])
    cs_doc_writer.writerow(row36[7:14])
    cs_doc_writer.writerow(row37[7:14])
    cs_doc_writer.writerow(row38[7:14])
    cs_doc_writer.writerow(row39[7:14])
    cs_doc_writer.writerow(row40[7:14])
    cs_doc_writer.writerow(row41[7:14])
    cs_doc_writer.writerow(row42[7:14])
    cs_doc_writer.writerow(row43[7:14])
    cs_doc_writer.writerow(row44[7:14])
    cs_doc_writer.writerow(row45[7:14])
    cs_doc_writer.writerow(row46[7:14])
    cs_doc_writer.writerow(row47[7:14])
    cs_doc_writer.writerow(row48[7:14])
    cs_doc_writer.writerow(row49[7:14])
    cs_doc_writer.writerow(row50[7:14])
    cs_doc_writer.writerow(row51[7:14])
    cs_doc_writer.writerow(row52[7:14])
    cs_doc_writer.writerow(row53[7:14])
    cs_doc_writer.writerow(row54[7:14])
    cs_doc_writer.writerow(row55[7:14])
    cs_doc_writer.writerow(row56[7:14])
    cs_doc_writer.writerow(row57[7:14])
    cs_doc_writer.writerow(row58[7:14])
    cs_doc_writer.writerow(row59[7:14])
    cs_doc_writer.writerow(row60[7:14])
    cs_doc_writer.writerow(row61[7:14])
    cs_doc_writer.writerow(row62[7:14])
    cs_doc_writer.writerow(row63[7:14])
    cs_doc_writer.writerow(row64[7:14])
    cs_doc_writer.writerow(row65[7:14])
    cs_doc_writer.writerow(row66[7:14])
    cs_doc_writer.writerow(row67[7:14])
    cs_doc_writer.writerow(row68[7:14])
    cs_doc_writer.writerow(row69[7:14])
    cs_doc.close

def Print_Cheat_Sheets():
    write_Cheat_Sheet()
    write_Cheat_Sheet_Printable()
