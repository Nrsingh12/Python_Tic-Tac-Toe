# Python Tic Tac Toe (Terminal Version)

A fun and interactive **Tic Tac Toe** game built in Python for the terminal. Two players can play turn-by-turn, placing Xs and Os on a grid, with a clear ASCII-based UI.

## Features

- Two-player gameplay (Player 1: X, Player 2: O)
- ASCII-art based 3x3 grid with a visually spaced-out 13x13 representation
- Validates user inputs
- Detects win conditions (rows, columns, diagonals)
- Declares winner or draw
- Clears screen after each move for better visibility

## How to Run

1. **Clone or download this repository**
2. Make sure Python is installed (recommended: Python 3.6+)
3. Open a terminal and navigate to the folder
4. Run the game using:

```bash
python3 tic_tac_toe.py
```

> **Note:** On Windows, change the command `os.system('clear')` to `os.system('cls')` inside the script for the screen to clear properly.

## Game Instructions

- The board has 9 positions, numbered 1 to 9 like this:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

- Players take turns entering the number of the position where they want to place their mark.
- Player 1 uses `X`, Player 2 uses `O`.
- The game ends when one player gets 3 in a row, column, or diagonal—or the board is full (draw).

## Example Gameplay

```
Player 1 Enter the Choice between 1 to 9: 5
Player 2 Enter the Choice between 1 to 9: 1
Player 1 Enter the Choice between 1 to 9: 9
...
Player 1 is winner!
```

## License

This is a basic project for learning purposes. Feel free to use and modify it!

---

Would you like a version of this with emojis, markdown badges, or as a GitHub README with sections like demo screenshots or video?
