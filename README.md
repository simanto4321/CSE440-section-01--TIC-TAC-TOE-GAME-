# CSE440-section-01--TIC-TAC-TOE-GAME-
Console-based Tic-Tac-Toe game. Single-player (vs AI) and two-player modes.

Here’s what you can write for **Project Features** (report, presentation, or README):

---

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

7. Project Structure 
- `main.py` — entry point to run the game  
- `support/` — supporting modules (board, menu, player, AI, game logic)  
- `data/` — folder for datasets (not used in this project)  
- `others/` — presentations, reports, and demo video  
- `requirements.txt` — lists project dependencies (Python standard library only)  
