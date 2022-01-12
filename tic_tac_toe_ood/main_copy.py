# This program is to build a text-based version of the Tic Tac Toe game - playable in the command line
# This is a Smarter Bot version - bot occupies central or corner position in the first go
# Allows the user to play again
# Keeps the score

from chart import Chart
from player_response import Player
from winner import Winner

# Logging into a file on the server
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s -- %(message)s"
logging.basicConfig(filename='ttt.log', level=logging.INFO, format=LOG_FORMAT, filemode='a')

chart = Chart()
winner = Winner()
block = [chart.row1, chart.row2, chart.row3]

player_response = Player(block)
player1_selection = player_response.player1_selection
player2_selection = player_response.player2_selection
chart.print_ttt()

# Play the game
count = 1
while count < 10:
    player = 1
    repeat = True
    if count % 2 == 0:
        player = 2
    try:
        while repeat:
            repeat = player_response.mark_position(player)

        game_end = winner.decide_winner(player, count, player1_selection, player2_selection, chart)
        if game_end:
            count = player_response.play_again()
            if count == 1:
                # reset the variables
                player = 1
                game_end = False
                chart = Chart()
                block = [chart.row1, chart.row2, chart.row3]

                player_response = Player(block)
                player1_selection = player_response.player1_selection
                player2_selection = player_response.player2_selection

                chart.print_ttt()
                player_response.mark_position(player)
            else:
                print("Thank you. Hope you enjoined the game!!")
                break
        else:
            if player == 2:
                chart.print_ttt()

        count += 1

    except Exception as err:
        print('Error!! Please try again')
        logging.exception(err)
