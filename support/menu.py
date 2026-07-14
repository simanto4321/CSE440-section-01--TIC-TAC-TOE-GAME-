def display_menu():
    print("=" * 30)
    print("   TIC-TAC-TOE")
    print("=" * 30)
    print()
    print("Select a game mode:")
    print("[1] 1 Player (vs AI)")
    print("[2] 2 Players (vs Friend)")
    print()


def get_menu_choice():
    while True:
        choice = input("Enter your choice (1 or 2): ").strip()
        if choice == "1":
            return 1
        if choice == "2":
            return 2
        print("Invalid choice. Please enter 1 or 2.\n")
