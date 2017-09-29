import funcs_ship_place
import os
import time

def begin_turn(player):
    os.system("clear")
    input("{0} ready? Press Enter ".format(player.name))
    os.system("clear")
    return None

def display_last_move(last, player, other):
    ship_name = {"p" : "Patrol Boat", "b" : "Battleship", "a" :
                 "Aircraft Carrier", "d" : "Destroyer", "s" :
                 "Submarine"}  
    if len(last) == 0:
        print("   {0} missed your ships".format(other.name))
    elif len(other.hits[last[0]]) == len(player.my_ships[last[0]]):
        print("   {0} sunk your {1}".
              format(other.name, ship_name[last[0]]))
    else:
        print("   {0} hit your {1} at {2}"
              .format(other.name, ship_name[last[0]], last[1]))
    return None

def get_guess(guesses):
    confirm = "n"
    while confirm not in "yY":
        position = input("\n   Where would you like to shoot? ")
        confirm = input("   You entered {0}, confirm (y/n)? "
                        .format(position))
        if not position[0].isalpha() or not position[1 : ].isdigit():
            print("   ERROR: COORDINATE NOT IN FORM A3")
            confirm = "n"
        elif not (65 <= ord(position[0].upper()) <= 74
                  and 0 <= int(position[1 : ]) <= 9):
            print("   ERROR: COORDINATE NOT ON BOARD")
            confirm = "n"
        elif funcs_ship_place.convert_grid_space(position) in guesses:
            print("   ERROR: POSITION ALREADY GUESSED")
            confirm = "n"
    return funcs_ship_place.convert_grid_space(position)

def check_if_hit(position, ships):
    ships_1d = [coordinate for ship in ships.values() 
                for coordinate in ship]
    return position in ships_1d

def ship_hit(guess, ships):
    for key in ships:
        if guess in ships[key]:
            return (key, funcs_ship_place.convert_1d_to_2d(guess))

def update_players(is_hit, position, player, other):
    if is_hit:
        print("\n   HIT at {0}"
              .format(funcs_ship_place.convert_1d_to_2d(position)))
        last = ship_hit(position, other.my_ships)
    else:
        print("\n   MISS at {0}"
              .format(funcs_ship_place.convert_1d_to_2d(position)))
        last = ()
    player.update_boards(position, last, other)
    time.sleep(3)
    os.system("clear")
    return last
