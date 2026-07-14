import random

from support.board import check_winner, get_available_moves


def find_winning_move(board, player):
    for move in get_available_moves(board):
        board[move] = player
        if check_winner(board) == player:
            board[move] = None
            return move
        board[move] = None
    return None


def ai_move(board):
    move = find_winning_move(board, "O")
    if move is not None:
        return move

    move = find_winning_move(board, "X")
    if move is not None:
        return move

    if not board[4]:
        return 4

    available = get_available_moves(board)
    return random.choice(available)
