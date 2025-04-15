# Import required module for clearing screen
import os

# Initialize game board size and list to store moves
n = 13  # Grid size for visual representation (13x13 to accommodate the game board with spacing)
ls = [1,2,3,4,5,6,7,8,9]  # List representing the 9 positions on the board

def tic_tac_tow():
    """
    Function to display the game board.
    Creates a visual grid with current game state using ASCII characters.
    Uses * for grid lines and displays X's, O's, or position numbers.
    """
    os.system('clear')  # Clear terminal screen for better visualization
    a = 0  # Counter to track position in ls list
    
    # Nested loops to create the 13x13 grid
    for i in range(n):
        for j in range(n):
            # Check if current position should display a game piece
            if (i==2 or i==6 or i==10) and (j==2 or j==6 or j==10):
                print(ls[a],end=" ")  # Print the value from our game list
                a+=1
            # Check if current position should display a grid line
            elif i==4 or i==8 or j==4 or j==8:
                print("*",end=" ")  # Print grid lines
            else:
                print(" ",end=" ")  # Print empty space for formatting
        print()  # New line after each row

def is_winner():
    """
    Function to check if there's a winner.
    Returns True if any winning condition is met, False otherwise.
    Winning conditions: 3 same symbols in a row, column, or diagonal.
    """
    # Check all rows for a win
    for i in range(0, 9, 3):
        if ls[i] == ls[i+1] == ls[i+2]:
            return True
    
    # Check all columns for a win
    for i in range(3):
        if ls[i] == ls[i+3] == ls[i+6]:
            return True
    
    # Check main diagonal (top-left to bottom-right)
    if ls[0] == ls[4] == ls[8]:
        return True
    # Check secondary diagonal (top-right to bottom-left)
    if ls[2] == ls[4] == ls[6]:
        return True
    
    return False

def verify(x):
    """
    Function to validate player input.
    Args:
        x (str): The player's input
    Returns:
        bool: True if input is valid, False otherwise
    """
    # Check if input is a valid number
    if not x.isdigit():
        return False
    x = int(x)
    # Check if number is within valid range (1-9)
    if x < 1 or x > 9:
        return False
    # Check if position is already taken
    if ls[x-1] == "X" or ls[x-1] == "O":
        return False
    return True

def update(x, i):
    """
    Function to update the game board with player's move.
    Args:
        x (int): Position chosen by player (1-9)
        i (int): Turn counter (even for Player 1, odd for Player 2)
    """
    # Update board with X for Player 1, O for Player 2
    if i%2==0:
        ls[x-1]="X"
    else:
        ls[x-1]="O"
    tic_tac_tow()  # Display updated board

# Main game loop
tic_tac_tow()  # Display initial board
i = 0  # Turn counter
while i<9:  # Maximum 9 moves possible
    # Determine current player
    if i%2==0:
        print("Player 1", end=" ")
    else:
        print("Player 2", end=" ")
    
    # Get player input
    print("Enter the Choice between 1 to 9:", end=" ")
    z = input()
    
    # Validate move
    y = verify(z)
    if y==False:
        tic_tac_tow()
        print("Invalid Choice. Plz try again")
        continue
    else:
        # Make move and update game state
        update(int(z),i)
        i+=1
        
        # Check for winner
        if is_winner():
            if i%2==1:  # i is incremented after move, so logic is reversed
                print("Player 1 is winner")
            else:
                print("Player 2 is winner")
            break
        elif i == 9:  # Check for draw
            print("Game Draw!")
