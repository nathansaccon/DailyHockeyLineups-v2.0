# NHL Player Classes

class Skater:
    # Basic Stats
    name = ""
    position = ""
    fd_position = ""
    dk_salary = ""
    fd_salary = ""
    team = ""
    opponent = ""
    arena = ""
    start_time = ""
    average_fpoints = ""
    fd_average_fpoints = ""
    website = ""
    game_log = ""
    url_num = ""
    # Opponent Specific Stats
    opp_games = ""
    opp_goals = ""
    opp_assists = ""
    opp_points = ""
    opp_shots = ""
    opp_shooting = ""
    # Advanced Stats
    ozs = ""
    pdo = ""
    cfp = ""
    # DraftKings Fantasy Averages
    dk_last_10 = ""
    dk_last_5 = ""
    dk_arena_fpts = ""
    dk_floor = ""
    dk_ceiling = ""
    # FanDuel Fantasy Averages
    fd_last_10 = ""
    fd_last_5 = ""
    fd_arena_fpts = ""
    fd_floor = ""
    fd_ceiling = ""
    # Point Percent Stats
    pp_arena = ""
    pp_season = ""
    pp_last_10 = ""


    # Returns the part of the players name needed for the url
    def HR_URL(self):
        name = self.name
        first = name.split(" ")[0]
        first = first.replace(".", "")
        first = first.replace("'", "")
        last = name.split(" ")[1]
        last = last.replace(".","")
        last = last.replace("'","")
        if len(name.split(" ")) >= 3:
            last = name.split(" ")[1] + name.split(" ")[2]
        # Special Cases
        if name == "P.A. Parenteau":
            first = "Pierre-Alexandre"
        if name == "Jonathan Marchessault":
            last = "AudyMarchessault"
        return "/" + last[0].lower() + "/" + last[:5].lower() + first[:2].lower() + "0"

    # DK Projected Points
    def DK_Projected_Points(self):
        try:
            return round(((self.dk_last_10 + self.dk_last_5 + self.dk_arena_fpts) / 3) + self.opp_points,2)
        except:
            return 0

    # FD Projected Points
    def FD_Projected_Points(self):
        try:
            return round(((self.fd_last_10 + self.fd_last_5 + self.fd_arena_fpts) / 3) + self.opp_points * 3.75,2)
        except:
            return 0

    # Player Value
    def Player_Value(self):
        try:
            return round((self.DK_Projected_Points() * 100000) / self.dk_salary, 1)
        except:
            return 0


class Goalie:
    # Basic Stats
    name = ""
    position = ""
    dk_salary = ""
    fd_salary = ""
    team = ""
    opponent = ""
    arena = ""
    start_time = ""
    average_fpoints = ""
    fd_average_fpoints = ""
    website = ""
    game_log = ""
    url_num = ""
    # Opponent Specific Stats
    opp_games = ""
    opp_win_percent = ""
    opp_save_percent = ""
    opp_gaa = ""
    # DraftKings Stats
    dk_last_10 = ""
    dk_last_5 = ""
    dk_arena_fpts = ""
    # FanDuel Stats
    fd_last_10 = ""
    fd_last_5 = ""
    fd_arena_fpts = ""
    # General Stats pp = win percent
    pp_arena = ""
    pp_season = ""
    pp_last_10 = ""

    def HR_URL(self):
        name = self.name
        first = name.split(" ")[0]
        first = first.replace(".", "")
        first = first.replace("'", "")
        last = name.split(" ")[1]
        last = last.replace(".","")
        last = last.replace("'","")
        if len(name.split(" ")) >= 3:
            last = name.split(" ")[1] + name.split(" ")[2]
        #Special Cases
        if name == "Jimmy Howard":
            first = "Jammy"
        if name == "Semyon Varlamov":
            first = "Simyon"
        return "/" + last[0].lower() + "/" + last[:5].lower() + first[:2].lower() + "0"

    # DK Projected Points
    def DK_Projected_Points(self):
        try:
            return round((self.dk_last_10 + self.dk_last_5 + self.dk_arena_fpts) / 3 + self.opp_win_percent /100,2)
        except:
            return 0

    # FD Prjected Points
    def FD_Projected_Points(self):
        try:
            return round((self.fd_last_10 + self.fd_last_5 + self.fd_arena_fpts) / 3 + self.opp_win_percent/100 * 7.5,2)
        except:
            return 0

    # Player Value
    def Player_Value(self):
        try:
            return round((self.DK_Projected_Points() * 100000) / self.dk_salary, 1)
        except:
            return 0

class Team:
    # Basic Stats
    name = ""
    opponent = ""
    arena = ""
    game_log = ""
    start_time = ""
    # Stats From Gamelog
    avg_shots = ""
    avg_shots_against = ""
    avg_goals = ""
    avg_goals_against = ""
    avg_pim = ""
    avg_pim_against = ""
    avg_pp_percent = ""
    avg_pk_percent = ""
    # Advanced Stats
    corsi_for = ""
    fenwick_for = ""
    pdo = ""
    ozs = ""

