from support.constants import WINNING_LINES


def display_board(board):
    cells = []
    for i, cell in enumerate(board):
        cells.append(cell if cell else str(i + 1))

    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def check_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_board_full(board):
    return all(cell for cell in board)


def get_available_moves(board):
    return [i for i, cell in enumerate(board) if not cell]
