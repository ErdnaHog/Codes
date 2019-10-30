from q3Classes import *

basketballTeam = input("Enter the basket ball team name: ")
players = []

for position in BasketballPlayer.positions:
    name_of_player = input(f"Which player is playing as a {position.capitalize()}: ")
    player = BasketballPlayer(name_of_player, position)
    players.append(player)

print(f"{basketballTeam} consists of the following players:")
for player in players:
    print(player)
