from errors import Errors


class Player:
    players_name = []
    player = []
    player_id = []

    def __init__(self, name, price, speed, finishing, defence, index):
        self.name = name
        self.price = int(price)
        self.speed = int(speed)
        self.finishing = int(finishing)
        self.defence = int(defence)
        self.index = index
        self.status = 'free'
        Player.player_id.append(index)
        Player.players_name.append(self.name)
        Player.player.append(self)

    def check_isRepeat(player_name):
        if player_name in Player.players_name:
            return True
        else:
            return False

    def print_player_info(character):
        p_id = character
        if not p_id in Player.player_id:
            Errors.player_does_not_exist('buy', p_id)
        else:
            print(f'player : {Player.player[p_id].name}\n'
                  f'price : {Player.player[p_id].price}\n'
                  f'state : {Player.player[p_id].status}\n'
                  f'speed : {Player.player[p_id].speed}\n'
                  f'finishing : {Player.player[p_id].finishing}\n'
                  f'defence : {Player.player[p_id].defence}\n')
