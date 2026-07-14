from support.ai import ai_move
from support.board import check_winner, display_board, is_board_full
from support.player import get_human_move


def end_game(board, mode):
    display_board(board)
    winner = check_winner(board)

    if winner == "X":
        if mode == 1:
            print("You win! Congratulations!")
        else:
            print("Player 1 (X) wins!")
    elif winner == "O":
        if mode == 1:
            print("AI (O) wins! Better luck next time.")
        else:
            print("Player 2 (O) wins!")
    else:
        print("It's a tie! The board is full.")


def play_game(mode):
    board = [None] * 9
    current_player = "X"

    while True:
        display_board(board)

        if current_player == "X":
            if mode == 1:
                index = get_human_move(board, "You", "X")
            else:
                index = get_human_move(board, "Player 1", "X")
        else:
            if mode == 1:
                print("AI (O) is thinking...")
                index = ai_move(board)
                print(f"AI chose spot {index + 1}.\n")
            else:
                index = get_human_move(board, "Player 2", "O")

        board[index] = current_player

        winner = check_winner(board)
        if winner:
            end_game(board, mode)
            return

        if is_board_full(board):
            end_game(board, mode)
            return

        current_player = "O" if current_player == "X" else "X"
