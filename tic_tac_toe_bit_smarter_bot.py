# This program is to build a text-based version of the Tic Tac Toe game - playable in the command line
# This is a Smarter Bot version - bot occupies central or corner position in the first go
# Allows the user to play again, Keeps the score
# This is procedural programming approach. Refactored some code but can be further refactored,
# especially the code that initialises the variables (this was done in the OOD version of the code).

from random import randint
from bot import winning_combination, bot_response

# Logging into a file on the server
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s -- %(message)s"
logging.basicConfig(filename='ttt.log', level=logging.INFO, format=LOG_FORMAT, filemode='a')

# Initialize variables
count = 1
game_end = False
player1_score = 0
player2_score = 0
player1_selection = []
player2_selection = []
row1 = ['___', '___', '___']
row2 = ['___', '___', '___']
row3 = ['   ', '   ', '   ']
block = [row1, row2, row3]


def print_ttt():
    print(*row1, sep="|")
    print(*row2, sep="|")
    print(*row3, sep="|")


def play_again():
    again = input("Do you want to continue? Enter 'Y or 'N: ").upper()
    if again == 'Y':
        counter = 1
    else:
        # End the While loop
        counter = 100
    return counter


def mark_position(player):
    try:
        if player == 1:
            row = int(input('Choose a row 1, 2 or 3: ')) - 1
            col = int(input('Choose a column 1, 2 or 3: ')) - 1
            player_selection = [(row, col)]
        else:
            # Bot's response
            player_selection = bot_response(player2_selection, player1_selection)   # check if bot can win
            if not player_selection:
                player_selection = bot_response(player1_selection, player2_selection)   # prevent other player win
                if not player_selection:
                    player_selection = [(randint(0, 2), randint(0, 2))]     # randomly generate selection

            row = player_selection[0][0]
            col = player_selection[0][1]

        # Check if the position is already taken by a player
        if set(player_selection).issubset(set(player1_selection)) or set(player_selection).issubset(set(player2_selection)):
            if player == 1:
                print(f"This option is already taken. Player {player}, please choose again!")
            mark_position(player)
        else:
            # Mark new position on the chart
            if player == 1:
                block[row][col] = '_X_'
                player1_selection.append(player_selection[0])
            else:
                block[row][col] = '_O_'
                player2_selection.append(player_selection[0])

    except ValueError as err:
        print(f"Please enter numeric value 1, 2 and 3. Player {player}, please enter again!")
        logging.exception(err)
        mark_position(player)

    except IndexError as err:
        print(f"Only number 1, 2 and 3 are allowed. Player {player}, please enter again!")
        logging.exception(err)
        mark_position(player)


def decide_winner(player, count):
    global player1_score
    global player2_score
    global game_end
    for item in winning_combination:
        if set(item).issubset(set(player1_selection)) or set(item).issubset(set(player2_selection)):
            print_ttt()
            if player == 1:
                player1_score += 1
            else:
                player2_score += 1
            print(f"Game Over!! Player {player} is the winner!!")
            print(f"Score: Player1 = {player1_score} ; Player2 = {player2_score}")
            game_end = True

    if count == 9 and not game_end:
        print_ttt()
        print(f"It's a Draw!!")
        print(f"Score: Player1 = {player1_score} ; Player2 = {player2_score}")
        game_end = True

# Play the game
print_ttt()
while count < 10:
    player = 1
    if count % 2 == 0:
        player = 2
    try:
        mark_position(player)
        decide_winner(player, count)
        if game_end:
            count = play_again()
            if count == 1:
                # reset the variables
                game_end = False
                player1_selection = []
                player2_selection = []
                row1 = ['___', '___', '___']
                row2 = ['___', '___', '___']
                row3 = ['   ', '   ', '   ']
                block = [row1, row2, row3]
                print_ttt()
                mark_position(1)
            else:
                print("Thank you. Hope you enjoined the game!!")
                break
        else:
            if player == 2:
                print_ttt()

        count += 1

    except Exception as err:
        print('Error!! Please try again')
        logging.exception(err)
