from player import Player
from team import Team
from errors import Errors


def match(character1, character2):
    team1_id = character1
    team2_id = character2
    if Team.is_exist_team(team1_id) and Team.is_exist_team(team2_id):
        if Team.number_of_player(team1_id) and Team.number_of_player(team2_id):
            sum_of_power_of_team1 = 0
            sum_of_power_of_team2 = 0
            for i in range(11):
                sum_of_power_of_team1 += Team.teams[team1_id].player[i].speed + Team.teams[team1_id].player[i].finishing
            print(sum_of_power_of_team1)
            for j in range(11):
                sum_of_power_of_team2 += Team.teams[team2_id].player[j].speed + Team.teams[team2_id].player[
                    j].defence
            print(sum_of_power_of_team2)
            if sum_of_power_of_team1 > sum_of_power_of_team2:
                Team.increase_win(Team.teams[team1_id])
                Team.increase_lost(Team.teams[team2_id])
                Team.increase_money(Team.teams[team1_id])
                print(Team.teams[team1_id].money)
                print("team 1 won the game!")
            elif sum_of_power_of_team1 < sum_of_power_of_team2:
                Team.increase_win(Team.teams[team2_id])
                Team.increase_lost(Team.teams[team1_id])
                Team.increase_money(Team.teams[team2_id])
                print(Team.teams[team2_id].money)
                print("team 2 won the game!")
            else:
                Team.increase_draw(Team.teams[team1_id])
                Team.increase_draw(Team.teams[team2_id])
                print("draw!")
        else:
            Errors.enough_player()
    else:
        if Team.is_exist_team(team1_id):
            Errors.team_does_not_exist(team1_id)
        elif Team.is_exist_team(team2_id):
            Errors.team_does_not_exist(team2_id)


i = 0
j = 0
while True:
    try:
        character = input().split()
        if character[0] == 'end':
            break
        elif character[0] == 'new' and character[1] == 'player':
            p1 = character[2]
            if Player.check_isRepeat(p1):
                Errors.another_name(p1)
            else:
                p1 = Player(character[2], character[3], character[4], character[5], character[6], i)
                i += 1
                print(p1.name, p1.index)
        elif character[0] == 'new' and character[1] == 'team':
            t1 = character[2]
            if Team.check_teamIsRepeat(t1):
                Errors.another_team_name(t1)
            else:
                t1 = Team(character[2], character[3], j)
                j += 1
                print(t1.index)
        elif character[0] == 'buy':
            team_id = int(character[2]) - 1
            player_id = int(character[1]) - 1
            if int(character[1]) > len(Player.players_name):
               er Errors.play_does_not_exist(character[0], character[1])
            elif int(character[2]) > len(Team.teams_name):
                Errors.team_does_not_exist(character[2])
            elif Team.teams[team_id].money < Player.player[player_id].price:
                Errors.not_having_enough_money()
            elif Player.player[player_id].status != "free":
                Errors.having_team()
            else:
                Team.add_player_in_team(Team.teams[team_id], Player.player[player_id])
                Team.teams[team_id].money -= Player.player[player_id].price
                Player.player[player_id].status = 'not free'
        elif character[0] == 'sell':
            team_id = int(character[2]) - 1
            player_id = int(character[1]) - 1
            if Team.is_exist_team(team_id):
                if Team.is_exist_player(Team.teams[team_id], player_id):
                    Team.sell_player(Team.teams[team_id], Player.player[player_id])
                    Player.player[player_id].status = 'free'
                else:
                    Errors.player_does_not_exist(character[0], None)
            else:
                Errors.team_does_not_exist(team_id + 1)
        elif character[0] == 'match':
            match(int(character[1]) - 1, int(character[2]) - 1)
        elif character[0] == 'show' and character[1] == 'players':
            for playerId, playerName in enumerate(Player.player):
                print(f'{playerId} : {playerName.name}')
        elif character[0] == 'show' and character[1] == 'teams':
            for teamId, teamName in enumerate(Team.teams):
                print(f'{teamId} : {teamName.name}')
        elif character[0] == 'show' and character[1] == 'player':
            p_id = int(character[2]) - 1
            Player.print_player_info(p_id)
        elif character[0] == 'show' and character[1] == 'team':
            t_id = int(character[2]) - 1
            if not Team.is_exist_team(t_id):
                Errors.team_does_not_exist(t_id + 1)
            else:
                Team.print_team_info(t_id)
        elif character[0] == 'rank':
            Team.sort_team(Team.teams)
        else:
            Errors.unavailable_command()
    except Exception as e:
        Errors.print_exception(e)
