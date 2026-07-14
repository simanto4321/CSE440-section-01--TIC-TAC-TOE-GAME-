def get_human_move(board, player_name, symbol):
    while True:
        raw = input(f"{player_name} ({symbol}), choose a spot (1-9): ").strip()
        if not raw.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.\n")
            continue

        spot = int(raw)
        if spot < 1 or spot > 9:
            print("Out of bounds. Please enter a number from 1 to 9.\n")
            continue

        index = spot - 1
        if board[index]:
            print("That spot is already taken. Try again.\n")
            continue

        return index
