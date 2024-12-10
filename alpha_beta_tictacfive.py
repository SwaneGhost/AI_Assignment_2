import math


def alphabeta_max(current_game):
    #add code here for alpha-beta
    return maximin(current_game, -math.inf, math.inf)


def alphabeta_min(current_game):
    #add code here for alpha-beta
    return minimax(current_game, -math.inf, math.inf)


def maximin(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = minimax(move, alpha, beta)
        if v < mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
            alpha = max(alpha, v)
            if alpha >= beta:
                break
    return v, best_move


def minimax(current_game, alpha, beta):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()
    for move in moves:
        mx, next_move = maximin(move, alpha, beta)
        if v > mx:
            v = mx
            best_move = move
        #add code here for alpha-beta algorithm
            beta = min(beta, v)
            if alpha >= beta:
                break
    return v, best_move
