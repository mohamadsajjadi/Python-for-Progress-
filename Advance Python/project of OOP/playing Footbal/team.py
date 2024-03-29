from errors import Errors


class Team:
    teams_name = []
    teams = []
    team_id = []

    def __init__(self, name, money, index):
        self.name = name
        self.money = int(money)
        self.index = index
        self.player_index = []
        self.player = []
        self.win = 0
        self.lost = 0
        self.draw = 0
        Team.team_id.append(index)
        Team.teams_name.append(self.name)
        Team.teams.append(self)
        self.rank = [self.name, self.win, self.lost]

    def check_teamIsRepeat(teamName):
        if teamName in Team.teams_name:
            return True
        else:
            return False

    def is_exist_team(team_id):
        if team_id in Team.team_id:
            return True
        else:
            return False

    def is_exist_player(self, player_id):
        if player_id in self.player_index:
            return True
        else:
            return False

    def add_player_in_team(self, player):
        if player.status != 'free':
            Errors.player_unavailable()
        elif player.index in self.player_index:
            Errors.another_name(player.index)
        else:
            self.player_index.append(player.index)
            self.player.append(player)
            Errors.successfully_add()

    def sell_player(self, player):
        if Team.is_exist_player(self, player.index):
            self.player_index.remove(player.index)
            self.player.remove(player)
            Errors.sold_successfully(player.index)
        else:
            Errors.player_does_not_exist('sell', None)

    def print_player_of_each_team(index):
        print(Team.teams[index].player_index)

    def number_of_player(index):
        if len(Team.teams[index].player_index) >= 11:
            return True
        else:
            return False

    def increase_win(self):
        self.win += 1
        self.rank[1] += 1

    def increase_lost(self):
        self.lost += 1
        self.rank[2] += 1

    def increase_draw(self):
        self.draw += 1

    def increase_money(self):
        self.money += 1000

    def swap(lst1, index_1, index_2):
        temp = lst1[index_1]
        lst1[index_1] = lst1[index_2]
        lst1[index_2] = temp
        return lst1

    def sort_team(self):
        sorted_list = list()
        for item in Team.teams:
            sorted_list.append(item.rank)
        for i in range(len(sorted_list)):  # [  [1,4] [1,3] [1,2]  ]  min = 4
            min = sorted_list[i][1]
            min_index = i
            min_lost = sorted_list[i][2]
            for j in range(i, len(sorted_list)):
                if min > sorted_list[j][1]:
                    min = sorted_list[j][1]
                    min_lost = sorted_list[j][2]
                    min_index = j
                elif min == sorted_list[j][1]:
                    if min_lost < sorted_list[j][2]:
                        min = sorted_list[j][1]
                        min_lost = sorted_list[j][2]
                        min_index = j
            Team.swap(sorted_list, i, min_index)

        lst = sorted_list[::-1]
        for item in lst:
            print(item[0], end=' ')

    def print_team_info(team_id):
        t_id = team_id
        print(f"team : {Team.teams[t_id].name}\n"
              f"money : {Team.teams[t_id].money}\nPlayers : ", end='')
        print(*Team.teams[t_id].player_index)
        print(f'win : {Team.teams[t_id].win}\n'
              f'draw : {Team.teams[t_id].draw}\n'
              f'loose : {Team.teams[t_id].lost}')

    @staticmethod
    def print_teams():
        print(Team.teams_name)
