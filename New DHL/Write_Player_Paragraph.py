# Write Player Paragraph

import pickle
from General_Functions import Team_Full_Name

readSkaters = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Skaters.txt", "rb")
all_skaters = pickle.load(readSkaters)

readGoalies = open("/Users/nathansaccon/Documents/Coding/New DHL/Data Storage/DK_Goalies.txt", "rb")
all_goalies = pickle.load(readGoalies)

readValuePlayers = open("/Users/nathansaccon/Documents/Coding/New DHL/Input Files/Value_Players.txt", "r")
value_players = eval(readValuePlayers.read())
value_skaters = list(filter(lambda x: x.name in value_players, all_skaters))
value_goalie = list(filter(lambda x: x.name in value_players, all_goalies))
value_players = value_skaters + value_goalie

for p in value_players:
    print(p.name, p.position)

def Write_Player_Paragraph(name):
    for player in all_skaters:
        if player.name == name:
            recent_pts = (sum(list(map(lambda x: x[1] + x[2],player.game_log[::-1][:10]))))
            games_counted = len(player.game_log[::-1][:10])
            if player.arena == "Home":
                para = "%s has %s points in his last %s games, which is good point production for a player that costs $%s on DraftKings. %s will be playing against the %s tonight at home. Against %s, %s averages %s points per game, as well as %s shots per game." % (player.name, recent_pts, games_counted, player.dk_salary, player.name.split(" ")[1], Team_Full_Name(player.opponent), player.opponent, player.name.split(" ")[1], player.opp_points, player.opp_shots)
            if player.arena == "Away":
                para = "%s has %s points in his last %s games, which is good point production for a player that costs $%s on DraftKings. %s will be playing against the %s tonight on the road. Against %s, %s averages %s points per game, as well as %s shots per game." % (player.name, recent_pts, games_counted, player.dk_salary, player.name.split(" ")[1], Team_Full_Name(player.opponent), player.opponent, player.name.split(" ")[1], player.opp_points, player.opp_shots)
            return para

    for player in all_goalies:
        if player.name == name:
            if player.arena == "Home":
                para = "%s has a home record of '' this season. Tonight he will be playing at home against the %s. In his career against %s, %s has a win rate of %s%%, save percentage of %s, as well as a goals against average of %s." % (player.name, Team_Full_Name(player.opponent), player.opponent, player.name.split(" ")[1], int(player.opp_win_percent), player.opp_save_percent, player.opp_gaa)
            if player.arena == "Away":
                para = "%s has an away record of '' this season. Tonight he will be playing on the road against the %s. In his career against %s, %s has a win rate of %s%%, save percentage of %s, as well as a goals against average of %s." % (player.name, Team_Full_Name(player.opponent), player.opponent, player.name.split(" ")[1], int(player.opp_win_percent), player.opp_save_percent, player.opp_gaa)
            return para

#print(Write_Player_Paragraph())

def Write_DHL_Paragraph():
    goalie = list(filter(lambda x: x.position == "G",value_players))[0]
    center = list(filter(lambda x: x.position == "C",value_players))[0]
    winger = list(filter(lambda x: x.position == "RW" or x.position == "LW",value_players))[0]
    defenceman = list(filter(lambda x: x.position == "D",value_players))[0]

    p1 = "Value players are players that are likely to receive more fantasy points than other players that cost that same amount. Keep this in mind when adding these players to your lineup. Value players are not usually players that you should build your lineups around, however they will always leave more room in your lineup for premium players. If you're looking for a longer list of value players, check out the [cheat sheet][1]. Make sure to check that a player is in the starting lineup before adding them to your lineup.\n\n[1]: /cheat-sheet\n\nWe are always looking to improve your fantasy experience. If you have any questions or suggestions we would love to hear from you on our [feedback page][0].\n\n# Low Cost Value Players\n\n## Today's Goalie:\n\n**%s**\n\nDaily Hockey Lineups Value: **%s**\n\n%s\n\nAlternative Goalies:\n\n## Today's Center:\n\n**%s**\n\nLine Number:\n\nDaily Hockey Lineups Value: **%s**\n\n%s\n\nAlternative Centers:\n\n## Today's Winger:\n\n**%s**\n\nLine Number:\n\nDaily Hockey Lineups Value: **%s**\n\n%s\n\nAlternative Wingers:\n\n## Today's Defenceman:\n\n**%s**\n\nLine Number:\n\nDaily Hockey Lineups Value: **%s**\n\n%s\n\nAlternative Defenceman:\n\n## Today's Sample Lineup\n\nWould you like more lineups for different start times? Check out the [Cheat Sheet Page][2] to get started.\n\n**DraftKings XPM Lineup**\n\n**FanDuel XPM Lineup**\n\nSupport DailyHockeyLineups.com by clicking the logo below, and creating an account!\n\n\n[0]: /feedback\n[2]: /cheat-sheet" % (str(goalie.name + " - " + goalie.team), goalie.Player_Value(), Write_Player_Paragraph(goalie.name), str(center.name + " - " + center.team), center.Player_Value(), Write_Player_Paragraph(center.name), str(winger.name + " - " + winger.team), winger.Player_Value(), Write_Player_Paragraph(winger.name), str(defenceman.name + " - " + defenceman.team), defenceman.Player_Value(), Write_Player_Paragraph(defenceman.name))

    dhl_value_post = open('/Users/nathansaccon/Documents/Coding/New DHL/Output Files/Value Player Writeup.txt', 'w')
    dhl_value_post.write(p1)
    dhl_value_post.close()