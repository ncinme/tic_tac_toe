import logging
from random import randint
from bot import Bot

LOG_FORMAT = "%(levelname)s %(asctime)s -- %(message)s"
logging.basicConfig(filename='ttt.log', level=logging.INFO, format=LOG_FORMAT, filemode='a')

bot = Bot()


class Player:
    def __init__(self, block):
        self.player1_selection = []
        self.player2_selection = []
        self.block = block
        self.counter = 0
        self.repeat = False

    def capture_response(self, player):
        self.repeat = False
        player_selection = []
        if player == 1:
            try:
                input_list = [1, 2, 3]
                row = input('Choose a row 1, 2 or 3: ')
                col = input('Choose a column 1, 2 or 3: ')
                if not (row.isnumeric() or col.isnumeric()):
                    print(f"Please enter numeric value 1, 2 and 3. Player {player}, please enter again!")
                    self.repeat = True
                elif not (int(row) in input_list or int(col) in input_list):
                    print(f"Please enter numeric value 1, 2 and 3. Player {player}, please enter again!")
                    self.repeat = True
                else:
                    player_selection = [(int(row) - 1, int(col) - 1)]

            except ValueError as err:
                print(f"Please enter numeric value 1, 2 and 3. Player {player}, please enter again!")
                logging.exception(err)
                self.repeat = True

            except IndexError as err:
                print(f"Only number 1, 2 and 3 are allowed. Player {player}, please enter again!")
                logging.exception(err)
                self.repeat = True
        else:
            # Bot's response
            player_selection = bot.response(self.player2_selection, self.player1_selection)   # check if bot can win
            if not player_selection:
                player_selection = bot.response(self.player1_selection, self.player2_selection)   # prevent other player win
                if not player_selection:
                    player_selection = [(randint(0, 2), randint(0, 2))]     # randomly generate selection

        # Check if the position is already taken by a player
        if player_selection:
            if set(player_selection).issubset(set(self.player1_selection)) or set(player_selection).issubset(set(self.player2_selection)):
                if player == 1:
                    print(f"This option is already taken. Player {player}, please choose again!")
                self.repeat = True
            else:
                return player_selection

    def mark_position(self, player):
        # Mark new position on the chart
        try:
            player_selection = self.capture_response(player)
            if not self.repeat:
                row = player_selection[0][0]
                col = player_selection[0][1]

                if player == 1:
                    self.block[row][col] = '_X_'
                    self.player1_selection.append(player_selection[0])
                else:
                    self.block[row][col] = '_O_'
                    self.player2_selection.append(player_selection[0])

        except ValueError as err:
            print(f"Please enter numeric value 1, 2 and 3. Player {player}, please enter again!")
            logging.exception(err)
            self.mark_position(player)

        except IndexError as err:
            print(f"Only number 1, 2 and 3 are allowed. Player {player}, please enter again!")
            logging.exception(err)
            self.mark_position(player)
        return self.repeat

    def play_again(self):
        again = input("Do you want to continue? Enter 'Y or 'N: ").upper()
        if again == 'Y':
            self.counter = 1
        else:
            # End the While loop
            self.counter = 100
        return self.counter
