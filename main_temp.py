
# # Get last index of item in list
# row1 = ['a', 'b', 'c', 'a', 'd']
# elem = 'a'
# idx = len(row1) - row1[::-1].index(elem) - 1
# print(len(row1))
# print(row1[::-1])
# print(row1[::-1].index(elem))
# print(idx)

# Print list items horizontally, separated by any symbol
# for i in row1:
#     print(i, end="|")

# You don't even need to loop it
# print(*row1, sep="|")
# Winning rows
# list_full = []
# list_temp = []
# for i in range(0,3):
#     for j in range(0,3):
#         toup = (i, j)
#         list_temp.append(toup)
#     list_full.append(list_temp)
#     list_temp = []

# print(list_full)
#
# Partial list comprehension
# full_list = []
# # for i in range(0,3):
#     list_temp1 = [(i, j) for j in range(0,3)]
#     full_list.append(list_temp1)
# print(full_list)
#
# Double loop list comprehension
# winning_rows = [[(i, j) for j in range(0,3)] for i in range(0,3)]
# print(winning_rows)
#
# Winning columns
# list_full2 = []
# for i in range(0, 3):
#     for item in list_full:
#         list_temp.append(item[i])
#     list_full2.append(list_temp)
#     list_temp = []
#
# print(list_full2)
# winning_cols = [[(j, i) for j in range(0,3)] for i in range(0,3)]
# print(winning_cols)
# winning diagonals
# list_full3 = []
# list_full4 = []
# for item in list_full:
#     idx = list_full.index(item)
#     toup1 = item[idx]
#     list_full3.append(toup1)
#     idx2 = len(item) -1 - idx
#     toup2 = item[idx2]
#     list_full4.append(toup2)
# print(list_full3)
# print(list_full4)
# winning_diagonal_1 = [item[winning_rows.index(item)] for item in winning_rows]
# print(winning_diagonal_1)
#
# winning_diagonal_2 = [item[len(item) - 1 - winning_rows.index(item)] for item in winning_rows]
# print(winning_diagonal_2)

# row1 = ['___', '___', '___']
# row2 = ['___', '___', '___']
# row3 = ['   ', '   ', '   ']
# block = [row1, row2, row3]
#
# # https://stackoverflow.com/questions/8437964/python-printing-horizontally-rather-than-current-default-printing
# def print_ttt():
#     print(*row1, sep="|")
#     print(*row2, sep="|")
#     print(*row3, sep="|")


# print_ttt()
# count = 0
#
#
# def play_game(player):
#     row = int(input('Choose a row 1, 2 or 3: '))
#     col = int(input('Choose a column 1, 2 or 3 : '))
#     if player == 1:
#         block[row - 1][col - 1] = '_X_'
#     else:
#         block[row - 1][col - 1] = '_O_'
#     print_ttt()
#
#
# while count < 9:
#     player = int(input('Choose a player 1 or 2: '))
#     play_game(player)
#     count += 1

# winning_rows = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
# print(winning_rows)
#
# winning_cols = [[(j, i) for j in range(0, 3)] for i in range(0, 3)]
# print(winning_cols)
#
# winning_diagonal_1 = [item[winning_rows.index(item)] for item in winning_rows]
# print(winning_diagonal_1)
# # print(type(winning_diagonal_1))
#
# winning_diagonal_2 = [item[len(item) - 1 - winning_rows.index(item)] for item in winning_rows]
# print(winning_diagonal_2)
#
# winning_list = winning_rows + winning_cols
# winning_list.append(winning_diagonal_1)
# winning_list.append(winning_diagonal_2)
#
# print(winning_list)



# or
# winning_rows = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
# winning_cols = [[(j, i) for j in range(0, 3)] for i in range(0, 3)]
# winning_diagonal_1 = [[item[winning_rows.index(item)] for item in winning_rows]]
# winning_diagonal_2 = [[item[len(item) - winning_rows.index(item) - 1] for item in winning_rows]]
# winning_combination = winning_rows + winning_cols + winning_diagonal_1 + winning_diagonal_2
import random
from random import randint

winning_combination = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                       [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                       [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

central_position = [(1, 1)]
corner_positions = [(0, 0), (2, 0), (0, 2), (2, 2)]


player1_selection = [(1, 1)]
player2_selection = [(0, 0)]

# player1_selection = [(0, 1), (2, 1), (1, 0)]
# player2_selection = [(1, 2), (2, 0)]
# player2_selection = [(0, 0), (1, 2)]
def bot_win(list1, list2):
    player_sub = []
    if len(list1) > 1:
        for item in winning_combination:
            for selection in list1:
                if selection in item:
                    player_sub.append(selection)
                    if len(player_sub) == 2:
                        player_selection = list(set(item) ^ set(player_sub))
                        print(item)
                        print(player_sub)
                        print(player_selection)
                        print(f'list2: {list2}')
                        if not set(player_selection).issubset(set(list2)):
                            print('I am inside')
                            return player_selection
            player_sub = []

    else:
        bot_selection = central_position
        if not (set(bot_selection).issubset(set(list1)) or set(bot_selection).issubset(set(list2))):
            return bot_selection
        else:
            bot_selection = [random.choice(corner_positions)]
            if not (set(bot_selection).issubset(set(list1)) or set(bot_selection).issubset(set(list2))):
                return bot_selection
    return []
            # if flag:
            #     player_sub = []
            # else:
            #     break
    #
    # return player_selection
# plr_sel = bot_win(player2_selection, player1_selection)
plr_sel = bot_win(player1_selection, player2_selection)
print(f'plr_sel: {plr_sel}')
if not plr_sel:
    print('omg')


# # player1_selection = [(1, 0)]
# player1_selection = [(2, 2), (0, 1), (2, 0)]
# player2_selection = [(0, 2), (2, 1)]
# # player2_selection = [(0, 0), (1, 2)]
# def bot_response(list1, list2):
#     player_sub = []
#     row = randint(0, 2)
#     col = randint(0, 2)
#     if len(list1) > 1:
#         for item in winning_combination:
#             for selection in list1:
#                 if selection in item:
#                     player_sub.append(selection)
#                     if len(player_sub) == 2:
#                         player_selection = list(set(item) ^ set(player_sub))
#                         print(item)
#                         print(player_sub)
#                         print(player_selection)
#                         print(f'list2: {list2}')
#                         if not set(player_selection).issubset(set(list2)):
#                             print('I am inside')
#                             return player_selection
#                         else:
#                             return [(row, col)]
#             player_sub = []
#     return [(row, col)]
#
#
# plr_sel = bot_response(player1_selection, player2_selection)
# print(f'plr_sel: {plr_sel}')
# if not plr_sel:
#     print('omg')


# flag = True
# player1_sub = []
# player2_sub = []
# player_selection = []
# row = randint(0, 2)
# col = randint(0, 2)
# if len(player1_selection) > 1:
#     for item in winning_combination:
#
#                 for selection in player1_selection:
#                     if selection in item:
#                         player1_sub.append(selection)
#                         if len(player1_sub) == 2:
#                             print(item)
#                             print(player1_sub)
#                             player_selection = list(set(item) ^ set(player1_sub))
#                             print(player_selection)
#                             if not set(player_selection).issubset(set(player2_selection)):
#                                 flag = False
#                 if flag:
#                     player1_sub = []
#                     player2_sub = []
#                 else:
#                     break
#     if flag:
#         player_selection = [(row, col)]
#         print(player_selection)
#
# else:
#     player_selection = [(row, col)]
#     print(player_selection)
#     row = player_selection[0][0]
#     col = player_selection[0][1]
#     print(f'row: {row}')
#     print(f'col: {col}')


# def bot_response(list1, list2):
#     flag = True
#     player_sub = []
#     player_selection = []
#     row = randint(0, 2)
#     col = randint(0, 2)
#     if len(list1) > 1:
#         for item in winning_combination:
#             for selection in list1:
#                 if selection in item:
#                     player_sub.append(selection)
#                     if len(player_sub) == 2:
#                         player_selection = list(set(item) ^ set(player_sub))
#                         if not set(player_selection).issubset(set(list2)):
#                             flag = False
#             if flag:
#                 player_sub = []
#             else:
#                 break
#         if flag:
#             player_selection = [(row, col)]
#
#     else:
#         player_selection = [(row, col)]
#
#     return player_selection

# test = [(1, 1), (0, 0), (2, 1), (1, 0), (2, 2)]
# for item in winning_combination:
#     if set(item).issubset(set(test)):
#         print("you're the winner!!")

