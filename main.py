"""Console-based Tic-Tac-Toe — project entry point."""

from support.game import play_game
from support.menu import display_menu, get_menu_choice


def main():
    display_menu()
    mode = get_menu_choice()
    print()
    if mode == 1:
        print("Starting 1 Player mode. You are X, AI is O.\n")
    else:
        print("Starting 2 Player mode. Player 1 is X, Player 2 is O.\n")

    play_game(mode)


if __name__ == "__main__":
    main()
