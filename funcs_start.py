import class_battleship
import funcs_driver
import time
import os

def display_intro():
    os.system("clear")
    print("\nThank you for playing Battleship\n\n"
          "   This is a two player game. Please report\n" 
          "   all coordinates with row first then column\n" 
          "   (i.e. A3 for first row third column).\n\n"
          "   Good luck and may the force be with you")
    return None

def get_players():
    players = []
    for player_num in range(1, 3):
        confirm = "n"
        while confirm not in "Yy":
            player_name = input("\nPlayer {0}, enter your name: "
                                .format(player_num))
            confirm = input("You entered {0}, confirm (y/n)? "
                            .format(player_name))
        players.append(class_battleship.Player(player_name))
    return players

def place_ships(players):
    print("\nIt is now time to place ships".format(players[0].name))
    time.sleep(3)
    for player in players:
        os.system("clear")
        funcs_driver.begin_turn(player)
        player.place_ships()
    return None

