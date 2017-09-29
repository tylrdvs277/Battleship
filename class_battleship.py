import funcs_ship_place
import os
import time

class Player:

    def __init__(self, name):
        self.name = name
        self.target_board = [["O" for i in range(10)]
                              for j in range(10)]
        self.my_board = [["O" for i in range(10)]
                          for j in range(10)]
        self.hits = {"p" : [], "d" : [], "s" : [], 
                     "b" : [], "a" : []}
        self.my_ships = {"p" : [], "d" : [], "s" : [], 
                         "b" : [], "a" : []}
        self.my_guesses = []
        self.sunk_ships = 0

    def place_ships(self):
        ships_placed = 0
        os.system("clear")
        while ships_placed < 5:
            self.print_object()
            ship = funcs_ship_place.get_ship(self.my_ships)
            position = funcs_ship_place.get_ship_position(tuple(self.my_ships.values()))
            ship_placement = funcs_ship_place.get_direction(tuple(self.my_ships.values()),
                                                            ship, position)
            self.my_ships[ship].extend(ship_placement)
            self.my_board = list(funcs_ship_place.update_my_board(self.my_board, 
                                 ship_placement))
            os.system("clear")
            ships_placed += 1
        self.print_object()
        time.sleep(3)

    def update_boards(self, position, last, other):
        self.my_guesses.append(position)
        ships = {"p" : "Patrol Boat", "d" : "Destroyer", 
                 "s" : "Submarine", "b" : "Battleship", 
                 "a" : "Aircraft Carrrier"}
        if len(last) != 0:
            self.target_board[position // 10][position % 10] = "X" 
            other.my_board[position // 10][position % 10] = "X"
            self.hits[last[0]].append(position)
            if len(self.hits[last[0]]) == len(other.my_ships[last[0]]):
                self.sunk_ships += 1
                print("\n   You sunk {0}'s {1}".format(other.name,
                      ships[last[0]]))
        else:
            self.target_board[position // 10][position % 10] = "_" 
            other.my_board[position // 10][position % 10] = "|"


    def print_object(self):
        ships = (("Patrol Boat", "p"), ( "Destroyer", "d"), ("Submarine", "s"),
                 ("Battleship", "b"), ("Aircraft Carrier", "a"))
        letters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J")
        title =   "                    Target Board            "
        title2 =  "                      My Board              "
        numbers = "       0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9"
        print("\n" + title2 + title)
        print("\n" + numbers * 2 + "\n")
        for (idx, row_1, row_2) in zip(letters, self.target_board, self.my_board):
            print("   " + idx + "   " + " | ".join(row_2) + 
                  "   " + idx + "   " + " | ".join(row_1))
        print("")
        for (name, key) in ships:
            print("   {0:>16}: {1:>14}".format(name, 
                  " ".join([funcs_ship_place.convert_1d_to_2d(coordinates) 
                  for coordinates in self.my_ships[key]])))
