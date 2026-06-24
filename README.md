# CSE440-section-01--TIC-TAC-TOE-GAME-
Console-based Tic-Tac-Toe game. Single-player (vs AI) and two-player modes.

Course: CSE 440 — Artificial Intelligence
Group: 01 | Section: 02
Institution: North South University
Semester: Summer 2026

# Group Members
         NAME                 NSU ID
1.Mehedi Ashraf Simanto      2112085042
2.Md. Mazharul Islam Masum   2233562042
3.Mst.Fahmida Akter          2121534642
4.Abdur Rahman               2131641042


# Overview
This project is a console-based Tic-Tac-Toe game developed in Python. It allows users to play in two different modes: single-player mode against a rule-based AI and two-player mode for local play with a friend. The game uses a clean text-based 3x3 board interface where players choose positions using numbers 1 to 9.
The system includes input validation to prevent invalid or duplicate moves, automatic turn management between players, and game-end detection after every move. In single-player mode, the AI follows a dynamic strategy: it tries to win when possible, blocks the player’s winning move, takes the center if available, and otherwise selects a random valid position.
Overall, the project demonstrates core programming concepts such as modular design, condition handling, loops, user interaction, and simple decision-based AI in an interactive terminal application.


# Project Features

1. Main Menu
- Displays a clear game title and menu when the program starts.
- Offers two modes:
  - **1 Player** — play against the computer (AI)
  - **2 Players** — play with a friend on the same computer
- Validates user input; if the user enters anything other than `1` or `2`, an error message is shown and the menu is displayed again.

2. Game Board Display
- Shows a clean text-based 3×3 grid using `|`, `-`, and spaces.
- Numbers positions **1 to 9** on empty cells so players know what to type.
- Updates the board after every move with **X** and **O** in the correct spots.

3. Two-Player Mode
- Player 1 uses **X**, Player 2 uses **O**.
- Players take turns entering a number from **1 to 9**.
- If a spot is already taken or the input is invalid, an error is shown and the same player tries again without losing their turn.

4. Single-Player Mode (vs AI)
- The human plays as **X**, the AI plays as **O**.
- The AI uses rule-based logic with these priorities:
  1. Win if possible  
  2. Block the player’s winning move  
  3. Take the center square (position 5) if it is free  
  4. Otherwise choose a random available spot  

5. Win and Draw Detection
- After every move, the game checks for a winner (3 in a row horizontally, vertically, or diagonally).
- If the board is full with no winner, the game declares a **tie/draw**.
- Displays the final board and announces the winner or tie before ending.

6. Input Validation
- Rejects non-numeric input.
- Rejects numbers outside the range 1–9.
- Rejects moves on cells that are already occupied.

# Project Structure 
tic_tac_toe/
├── main.py                 # Main entry point
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
├── data/                   # Dataset folder (if needed)
├── support/                # Supporting source files
│   ├── ai.py               # AI move logic
│   ├── board.py            # Board display and win checks
│   ├── constants.py        # Winning line definitions
│   ├── game.py             # Main game loop
│   ├── menu.py             # Menu and mode selection
│   └── player.py           # Player input handling
└── others/                 # Reports, presentation, demo video  
