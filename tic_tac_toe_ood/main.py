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

winner = Winner()
game_end = False


def initialize():
    chart = Chart()
    block = [chart.row1, chart.row2, chart.row3]
    chart.print_ttt()

    player_response = Player(block)
    player1_selection = player_response.player1_selection
    player2_selection = player_response.player2_selection

    return player_response, player1_selection, player2_selection, chart


def play_game(player_response, player1_selection, player2_selection, chart):
    count = 1
    while count < 10:
        repeat = True

        if count % 2 == 0:
            player = 2
        else:
            player = 1

        try:
            while repeat:
                repeat = player_response.mark_position(player)

            got_winner = winner.decide_winner(player, count, player1_selection, player2_selection, chart)
            if not got_winner:
                if player == 2:
                    chart.print_ttt()
            else:
                break

            count += 1

        except Exception as err:
            print('Error!! Please try again')
            logging.exception(err)


while not game_end:
    if input("Do you want to play a game of TicTacToe? Enter 'Y or 'N: ").upper() == 'Y':
        plyr_response, plyr1_selection, plyr2_selection, chrt = initialize()
        play_game(plyr_response, plyr1_selection, plyr2_selection, chrt)
    else:
        print("Thank you. Hope you enjoined the game!!")
        game_end = True
