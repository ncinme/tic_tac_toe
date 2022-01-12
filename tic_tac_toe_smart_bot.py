# This program is to build a text-based version of the Tic Tac Toe game - playable in the command line
# This is a Smart Bot version. However, gives ample opportunities to the other player to win
# Allows the user to play again, Keeps the score
# This is procedural programming approach. Code can be further refactored,
# especially the code within the While loop (this was done in the OOD version of the code).

from random import randint

# Logging into a file on the server
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s -- %(message)s"
logging.basicConfig(filename='ttt.log', level=logging.INFO, format=LOG_FORMAT, filemode='a')

# Calculate the winning combinations
winning_rows = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
winning_cols = [[(j, i) for j in range(0, 3)] for i in range(0, 3)]
winning_diagonal_1 = [[item[winning_rows.index(item)] for item in winning_rows]]
winning_diagonal_2 = [[item[len(item) - winning_rows.index(item) - 1] for item in winning_rows]]
winning_combination = winning_rows + winning_cols + winning_diagonal_1 + winning_diagonal_2


def print_ttt():
    print(*row1, sep="|")
    print(*row2, sep="|")
    print(*row3, sep="|")


def play_again():
    again = input("Do you want to continue? Enter 'Y or 'N: ").upper()
    if again == 'Y':
        counter = 1
    else:
        counter = 100
    return counter


def bot_response(list1, list2):
    player_sub = []
    if len(list1) > 1:
        for item in winning_combination:
            for selection in list1:
                if selection in item:
                    player_sub.append(selection)
                    if len(player_sub) == 2:
                        player_selection = list(set(item) ^ set(player_sub))
                        if not set(player_selection).issubset(set(list2)):
                            return player_selection
            player_sub = []
    return []


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

        if set(player_selection).issubset(set(player1_selection)) or set(player_selection).issubset(set(player2_selection)):
            if player == 1:
                print(f"This option is already taken. Player {player}, please choose again!")
            mark_position(player)
        else:
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

# Initialize variables
count = 1
player1_selection = []
player2_selection = []
player1_score = 0
player2_score = 0
row1 = ['___', '___', '___']
row2 = ['___', '___', '___']
row3 = ['   ', '   ', '   ']
block = [row1, row2, row3]
print_ttt()

while count < 10:
    game_end = False
    player = 1
    if count % 2 == 0:
        player = 2
    try:
        mark_position(player)
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

        if game_end:
            count = play_again()
            if count == 1:
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
