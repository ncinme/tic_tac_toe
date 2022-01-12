# This program is to build a text-based version of the Tic Tac Toe game - playable in the command line
# This is a Two players version

# Logging into a file on the server
import logging
LOG_FORMAT = "%(levelname)s %(asctime)s -- %(message)s"
logging.basicConfig(filename='ttt.log', level=logging.INFO, format=LOG_FORMAT, filemode='a')

# We can either hardcode or calculate the winning combination
# winning_combination = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
#                        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
#                        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

winning_rows = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
winning_cols = [[(j, i) for j in range(0, 3)] for i in range(0, 3)]
winning_diagonal_1 = [[item[winning_rows.index(item)] for item in winning_rows]]
winning_diagonal_2 = [[item[len(item) - winning_rows.index(item) - 1] for item in winning_rows]]
winning_combination = winning_rows + winning_cols + winning_diagonal_1 + winning_diagonal_2

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


def mark_position(player):
    try:
        row = int(input('Choose a row 1, 2 or 3: ')) - 1
        col = int(input('Choose a column 1, 2 or 3: ')) - 1
        player_selection = [(row, col)]

        if set(player_selection).issubset(set(player1_selection)) or set(player_selection).issubset(set(player2_selection)):
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


while count < 10:
    print_ttt()
    player = 1
    game_end = False
    if count % 2 == 0:
        player = 2
    print(f'Player {player} turn:')
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
        count += 1

    except Exception as err:
        print('Error!! Please try again')
        logging.exception(err)

