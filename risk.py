from Territory import Territory
from Player import Player
from random import shuffle

rmap = [Territory("Iceland", ["Great Britan"]),
       Territory("Great Britan", ["France", "Iceland"]),
       Territory("France", ["Great Britan"]]

def print_game_status():
    print(rmap[0].name + ':  ', rmap[0].troops,'troops, owner is', rmap[0].owner.name)
    print(rmap[1].name + ':  ', rmap[1].troops,'troops, owner is', rmap[1].owner.name)
    print(rmap[2].name + ':  ', rmap[2].troops,'troops, owner is', rmap[2].owner.name)
    print()

Players = [Player('King The Fox 25', 'red'),
           Player('ThePope', 'green'),
           Player('xPaul', 'blue')]
shuffle(Players)

rmap[0].owner = Players[0]
rmap[1].owner = Players[1]
rmap[2].owner = Players[2]

rmap[0].troops = 8
rmap[1].troops = 15
rmap[2].troops = 7

run = True
while run:
    for player in Players:
        print("It's " + player.name + "'s turn. \n")
        player.turn_troops = 3
        phase = 'draft'
        print(phase)
        
        print_game_status()
        player.draft(rmap)
        
        phase = 'attack'
        print(phase)

        print_game_status()
        player.attack(rmap)
        
        phase = 'fortify'
        print(phase)

        print_game_status()
        player.fortify(rmap)
        
        print_game_status()
    run = False
