import math
h = None


def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # add code here
    return maximin(current_game, depth, -math.inf, math.inf)


def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # add code here
    return minimax(current_game, depth, -math.inf, math.inf)


def maximin(current_game, depth, alpha, beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, depth - 1, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    return v, best_move


def minimax(current_game, depth, alpha, beta):
    global h
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, depth - 1, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
            beta = min(beta, v)
            if alpha >= beta:
                break
    return v, best_move
