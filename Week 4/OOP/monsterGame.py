from monsterSubClasses import *
from random import randint

class MonsterGame:

    player_monster = ""
    computer_monster = ""
    monster_dict = {"F": FireMonster(), "W": WaterMonster(), "G": GrassMonster()}
    def __init__(self):
        self.choose_monster()
        self.generate_monster()

    def choose_monster(self):
        player_monster = input("Choose your monster (F, W or G): ").upper()
        while player_monster not in self.monster_dict.keys():
            player_monster = input("Invalid choice. Choose your monster (F, W or G): ")
        self.player_monster = self.monster_dict[player_monster]

    def generate_monster(self):
        self.computer_monster = list(self.monster_dict.values())[randint(0, 2)]

    # def get_player_monster(self):
    #     return self.player_monster
    #
    # def get_computer_monster(self):
    #     return self.computer_monster

game = MonsterGame()
while game.computer_monster.get_health() > 0 and game.player_monster.get_health() > 0:
    #your turn
    computer_health = game.computer_monster.get_health()
    player_attack = game.player_monster.get_attack()-game.computer_monster.get_defence()
    new_computer_health = computer_health - player_attack
    game.computer_monster.set_health(new_computer_health)
    print(f"{game.computer_monster.get_name()} suffers {player_attack} damage, the health is {new_computer_health} now")
    if new_computer_health <= 0:
        print("You won!")
        break
    #computer turn
    player_health = game.player_monster.get_health()
    computer_attack = game.computer_monster.get_attack()-game.player_monster.get_defence()
    new_player_health = player_health - computer_attack
    game.player_monster.set_health(new_player_health)
    print(f"{game.player_monster.get_name()} suffers {computer_attack} damage, the health is {new_player_health} now")
if player_health < computer_health:
    print("You lost!")
