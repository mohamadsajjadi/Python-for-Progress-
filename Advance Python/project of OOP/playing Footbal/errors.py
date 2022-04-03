from termcolor import colored


class Errors:

    def another_name(p1):
        print(colored(f'{p1} is exist! Enter another name!', 'red'))

    def another_team_name(t1):
        print(colored(f'{t1} is exist:( Enter another team name!', 'red'))

    def player_does_not_exist(character, character1):
        if character == 'buy':
            print(colored(f"player with the id {character1} doesn't exist", 'red'))
        elif character == 'sell':
            print(colored("team doest have this player", 'red'))

    def team_does_not_exist(character):
        print(colored(f"team with the id {character} doesnt exist", 'red'))

    @staticmethod
    def not_having_enough_money():
        print(colored("the team don't have enough money to buy this player", 'red'))

    @staticmethod
    def having_team():
        print(colored("player already has team", 'red'))

    @staticmethod
    def unavailable_command():
        print(colored(f"this command not available! Please Enter another command", 'red'))

    def print_exception(e):
        print(colored(f"this command not available, Because {e}! Please Enter another command", 'red'))

    @staticmethod
    def enough_player():
        print(colored("the game can not be held due to loss of the players", 'red'))

    @staticmethod
    def player_unavailable():
        print(colored("this player is unavailable", 'red'))

    @staticmethod
    def successfully_add():
        print(colored("player added to the team successfully", 'green'))

    def sold_successfully(player_index):
        print(colored(f"player{player_index} sold successfully", 'blue'))
