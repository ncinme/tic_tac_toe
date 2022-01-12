# Calculate the winning combinations
winning_rows = [[(i, j) for j in range(0, 3)] for i in range(0, 3)]
winning_cols = [[(j, i) for j in range(0, 3)] for i in range(0, 3)]
winning_diagonal_1 = [[item[winning_rows.index(item)] for item in winning_rows]]
winning_diagonal_2 = [[item[len(item) - winning_rows.index(item) - 1] for item in winning_rows]]
winning_combination = winning_rows + winning_cols + winning_diagonal_1 + winning_diagonal_2
central_corner_position = [(1, 1), (0, 0), (2, 0), (0, 2), (2, 2)]


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

    else:
        if len(list2) == 1:
            for item in central_corner_position:
                list_item = [item]
                if not (set(list_item).issubset(set(list1)) or set(list_item).issubset(set(list2))):
                    return [item]
    return []