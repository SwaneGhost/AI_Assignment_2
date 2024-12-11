import numpy as np


def base_heuristic(curr_state):
    grid = curr_state.get_grid()
    row, col = len(grid), len(grid[0])
    score_player_1 = calculate_score(grid, row, col, 1)
    score_player_2 = calculate_score(grid, row, col, 2)
    return score_player_1 - score_player_2


def count_sequences(line, player):
    """
    Counts the number of sequences of 3 and 4 consecutive cells occupied by the given player in the line.
    Counts only sequences that can be extended to a winning sequence by adding a cell on either side for 4
    consecutive cells, or both sides for 3 consecutive cells.

    :param line: List of integers representing a row, column, or diagonal in the grid.
    :param player: Integer representing the player (e.g., 1 or 2).
    :return: sum of count_3, count_4 where count_3 is the number of sequences of 3 consecutive cells,
             and count_4 is the number of sequences of 4 consecutive cells occupied by the player.
    """
    count_3 = 0
    count_4 = 0

    if len(line) > 4:
        for i in range(len(line) - 3):
            if i + 4 <= len(line) and np.array_equal(line[i:i + 4], [player] * 4):
                if ((i != 0 and line[i - 1] == 0 and (i + 4 >= len(line) or line[i + 4] == 0)) or
                        ((i + 4 >= len(line) or line[i + 4] == 0) and (i == 0 or line[i - 1] == 0))):
                    count_4 += 1
            elif np.array_equal(line[i:i + 3], [player] * 3):
                if i != 0 and line[i - 1] == 0 and i + 3 < len(line) and line[i + 3] == 0:
                    count_3 += 1

    return count_3 + count_4


def calculate_score(grid, row, col, player):
    """
   Calculates the score for the given player based on the current state of the grid.
   The score is determined by counting sequences of 3 and 4 consecutive cells occupied by the player.

   :param grid: 2D list of integers representing the game grid.
   :param row: Integer representing the number of rows in the grid.
   :param col: Integer representing the number of columns in the grid.
   :param player: Integer representing the player (e.g., 1 or 2).
   :return: Integer score for the given player.
   """

    score = 0
    for r in range(row):
        score += count_sequences(grid[r], player)

    for c in range(col):
        score += count_sequences([grid[r][c] for r in range(row)], player)

    for d in range(-row + 1, col):
        diag1 = [grid[r][r - d] for r in range(max(0, d), min(row, col + d))]
        score += count_sequences(diag1, player)

    for d in range(col + row - 1):
        diag2 = [grid[r][d - r] for r in range(max(0, d - col + 1), min(row, d + 1))]
        score += count_sequences(diag2, player)

    return score


def advanced_heuristic(curr_state):
    return 0
