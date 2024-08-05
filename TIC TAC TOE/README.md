A README documentation for our dynamic Tic Tac Toe game:

---

# Tic Tac Toe Game

This is a simple implementation of the classic Tic Tac Toe game in Python. The game allows one to choose the size of the board dynamically and play against another player.

## Prerequisites

Before running the game, ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies:**
   ```bash
   pip install colorama
   ```

3. **Run the game:**
   ```bash
   python tic_tac_toe.py ##to play against another player
     or 
   python game_2.py ##to play against computer
   ```https://github.com/MUGANE-ABEL/tictactoe_project/invitations

## How to Play

1. **Game Size:**
   - When prompted, enter the size of the Tic Tac Toe board you'd like to play with (e.g., 3 for a 3x3 board).

2. **Game Board:**
   - The board will be displayed with positions labeled with row and column numbers.

3. **Gameplay:**
   - Players take turns to place their mark ('X' or 'O') on the board.
   - Enter the row and column numbers (0-indexed) where you want to place your mark.
   - The game checks for a winner after each move.

4. **Winning:**
   - A player wins if they have three of their marks in a row (horizontally, vertically, or diagonally).

5. **Play Again:**
   - After each game concludes, you will be asked if you want to play again.
   - Type 'y' to play again or 'n' to exit.

## Error Handling

- The game handles various errors gracefully, such as invalid inputs for row and column selections.
- If an occupied position is chosen, the game prompts to choose another position.

## Libraries Used

- **itertools:** Used for cycling through player turns.
- **colorama:** Used for coloring the 'X' and 'O' marks on the board for better visual distinction.

## Credits

This game was created by Lone Rangers.

---
