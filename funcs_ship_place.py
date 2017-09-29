import itertools

def get_ship(current_ships):
    confirm = "n"
    while confirm not in "yY":
        valid = True
        ship = input("\n   Would you like to place your "
                 "(p)atrol boat, (d)estroyer, "
                 "(s)ubmarine, (b)attleship, or "
                 "(a)ircraft carrier? ").lower()
        if ship not in "pdsba" or len(ship) != 1:
            print("   ERROR: SHIP NOT DEFINED")
            confirm = "n"
            valid = False
        elif len(current_ships[ship]) != 0:
            print("   ERROR: SHIP ALREADY PLACED")
            confirm = "n"
            valid = False
        if valid:
            confirm = input("   You entered {0}, confirm (y/n)? "
                            .format(ship))
    return ship

def convert_grid_space(grid_space):
    return int(grid_space[1]) + 10 * (ord(grid_space[0].upper()) - 65)

def convert_1d_to_2d(position):
    return chr(position // 10 + 65) + str(position % 10)

def get_ship_position(ships):
    confirm = "n"
    while confirm not in "yY":
        valid = True
        position = input("\n   Where would you like to place the ship? ")
        ships_1d = list(itertools.chain(*ships))
        if not position[0].isalpha() or not position[1 : ].isdigit():
            print("   ERROR: COORDINATE NOT IN FORM A3")
            confirm = "n"
            valid = False
        elif not (65 <= ord(position[0].upper()) <= 74 
                  and 0 <= int(position[1 : ]) <= 9):
            print("   ERROR: COORDINATE NOT ON BOARD")
            confirm = "n"
            valid = False
        elif convert_grid_space(position) in ships_1d:
            print("   ERROR: SHIPS OVERLAP")
            confirm = "n"
            valid = False
        if valid:
            confirm = input("   You entered {0}, confirm (y/n)? "
                            .format(position))
    return convert_grid_space(position)
    
def get_direction(ships, ship, position):
    confirm = "n"
    while confirm not in "yY":
        valid = True
        direction = input("\n   Place this ship going " 
                          "(r)ight, (l)eft, (u)p, or (d)own? ")
        if direction.lower() not in "rlud":
            print("   ERROR: DIRECTION NOT DEFINED")
            confirm = "n"
            valid = False
        elif not is_ship_placement_valid(ship_placement(direction, position, ship), 
                                         ships):
            confirm = "n"
            valid = False
        if valid:
            confirm = input("   You entered {0}, confirm (y/n)? "
                            .format(direction))
    return ship_placement(direction, position, ship)


def ship_placement(direction, position, ship):
    direction = "rldu".index(direction.lower())
    ship_length = {"p" : 2, "d" : 3, "s" : 3, 
                   "b" : 4, "a" : 5}
    placements = ([right_position for right_position in range(position, position + ship_length[ship])],
            [left_position for left_position in range(position - ship_length[ship] + 1, position + 1)],
                  [down_position for down_position in range(position, position + 10 * ship_length[ship], 10)],
                  [up_position for up_position in range(position - 10 * (ship_length[ship] - 1), position + 1, 10)])
    return placements[direction]

def is_ship_placement_valid(ship_to_place, current_ships):
    rows = [position_1d // 10 for position_1d in ship_to_place]
    columns = [position_1d % 10 for position_1d in ship_to_place]
    ships_1d = [ship_1d for ship in current_ships for ship_1d in ship]
    if (min(ship_to_place) < 0 or max(ship_to_place) > 99 or 
       (min(rows) != max(rows) and columns[1] != columns[0])):
            print("   ERROR: SHIP NOT ON BOARD")
            for position in ship_to_place:
                if position in ships_1d:
                    print("   ERROR: SHIPS OVERLAP")
                    return False
            return False
    else:
        for position in ship_to_place:
            if position in ships_1d:
                print("   ERROR: SHIPS OVERLAP")
                return False
    return True

def update_my_board(board, ship):
    for position_1d in ship:
        board[position_1d // 10][position_1d % 10] = "_"
    return board
