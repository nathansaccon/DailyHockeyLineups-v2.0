# Main Function

from DK_CSV_Reader import Create_DK_Player_Files
from FD_CSV_Reader import Create_FD_Player_Files
from General_Functions import Injured_Players, Write_Start_Time_File, Write_Starting_Goalies
from Scrape_Stats import Write_Gamelog_Update, Write_Splits_Update, Write_Advanced_Stats_Update
from Scrape_Stats_Goalies import Write_Gamelog_Update_G, Write_Splits_Update_G
from Calculate_Fantasy_Averages import Add_Fantasy_Averages
from Calc_Fantasy_Averages_Goalies import Add_Fantasy_Averages_G
from Calculate_Team_Averages import Team_Averages
from Salary_Update import Update_FD_salary
from Write_Value_Players import Write_Value_Lists
from Write_Matchup_Lists import Write_Matchup_Lists
from Write_Tweets import Write_Tweet_Files
from Create_Team_Class import Create_Team
from Write_Matchup_CSVs import Write_All_Matchup_CSV
from Write_Cheat_Sheet_CSV import Print_Cheat_Sheets
from Write_Lineup_Files import Write_Lineup_Files



def Main():
    ''' RUN IN THIS ORDER AND REFRESH IN BETWEEN
    Run_1()
    Run_2()
    Run_3()
    Run_4()
    Run_5()
    Run_6()
    Run_7()
    Run_8()

    Write_Lineup_Files()

    '''
    pass


def Run_1():
    Create_FD_Player_Files()
    Create_DK_Player_Files()
    print("\nRun One Complete\n")

def Run_2():
    Update_FD_salary()
    Write_Start_Time_File()
    Write_Starting_Goalies()
    Injured_Players()
    print("\nRun Two Complete\n")

def Run_3():
    Create_Team()
    print("\nRun Three Complete\n")

def Run_4():
    Team_Averages()
    Write_Gamelog_Update()
    Write_Gamelog_Update_G()
    print("\nRun Four Complete\n")

def Run_5():
    Write_Splits_Update()
    Write_Splits_Update_G()
    print("\nRun Five Complete\n")

def Run_6():
    Write_Advanced_Stats_Update()
    print("\nRun Six Complete\n")

def Run_7():
    Add_Fantasy_Averages()
    Add_Fantasy_Averages_G()
    print("\nRun Seven Complete\n")

def Run_8():
    Write_Value_Lists()
    Write_Matchup_Lists()
    Write_Tweet_Files()
    Write_All_Matchup_CSV()
    Print_Cheat_Sheets()
    print("\nRun Eight Complete\n")