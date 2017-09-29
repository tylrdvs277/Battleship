import funcs_ship_place
import funcs_start
import funcs_driver
import time
import os

def main():
    funcs_start.display_intro()
    players = funcs_start.get_players()
    funcs_start.place_ships(players)
    counter = 0
    while (players[0].sunk_ships < 5 and
           players[1].sunk_ships < 5):
        turn = counter % 2
        other = 1 - turn
        funcs_driver.begin_turn(players[turn])
        if counter != 0:
            funcs_driver.display_last_move(last_move, players[turn], 
                                           players[other])
        last_move = None
        players[turn].print_object()
        guess = funcs_driver.get_guess(players[turn].my_guesses)
        is_hit = funcs_driver.check_if_hit(guess, 
                              players[other].my_ships)
        last_move = funcs_driver.update_players(
                    is_hit, guess, players[turn], players[other]) 
        players[turn].print_object()
        time.sleep(5)
        counter += 1
    os.system("clear")
    if players[0].sunk_ships == 5:
        print("\n\n\n\n\n   {0} wins".format(players[0].name))
        time.sleep(3)
    else:
        print("\n\n\n\n\n   {0} wins".format(players[1].name))
        time.sleep(3)

if __name__ == "__main__":
    main()
