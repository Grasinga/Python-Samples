# String that acts as a spot that doesn't have an X or an O.
placeholder = " "

# Set-up the game board.
gameBoard = [["", "", ""],
             ["", "", ""],
             ["", "", ""]]

# Declare a variable that will house the winning info.
outcome = ""

# Assign the players a character.
player1 = "X"
player2 = "O"

# Method to run the program.
def main():
    # Initial the game board with the placeholder.
    global gameBoard
    gameBoard = [[placeholder, placeholder, placeholder],
                 [placeholder, placeholder, placeholder],
                 [placeholder, placeholder, placeholder]]
    
    print("Tic-Tac-Toe")
    print()
    printBoard()
    
    while True: # Main game loop.
        
        # Get player 1's selection, set it, and check it.
        print()
        setXSpot(player1Input())
        print()
        printBoard()
        if gameOver():
            break;
        
        # Get player 1's selection, set it, and check it.
        print()
        setOSpot(player2Input())
        print()
        printBoard()
        if gameOver():
            break;

    print()  
    print(outcome)
    print()

    if input("Play again? [y/n] ") == 'y':
        print()
        main()

# Passes Player 1's character to getSpot(character).
def player1Input():
    print ("- Player 1's Turn -")
    return getSpot(player1)

# Passes Player 2's character to getSpot(character).
def player2Input():
    print ("- Player 2's Turn -")
    return getSpot(player2)

# Gets the Player's input and creates a spot on the game board out of it.
# It then checks if the spot is empty and if so, puts the character there.
# If the spot wasn't empty, it asks for a new spot.
def getSpot(character):
    # Make sure the input is a valid number.
    parsed = False
    while not parsed:
        try:
            spot = [int(input("Enter the row to place " + character + ": ")),
                    int(input("Enter the collum to place " + character + ": "))]
            parsed = True
        except ValueError:
            print ("Not a valid row or collum! Please enter another spot:")
            return getSpot(character)

    # Makes the game board more player friendly by making the game board
    # start at [1][1] and end at [3][3] instead of
    # starting at [0][0] and ending at [2][2].
    spot[0] -= 1
    spot[1] -= 1

    # Make sure the input is within the game board's range.
    if(spot[0] < 0 or spot[0] > 2 or spot[1] < 0 or spot[1] > 2):
        print ("Not a valid row or collum! Please enter another spot:")
        if character is "X":
            return getSpot(character)
        else:
            return getSpot(character)

    # Make sure the spot is empty.   
    if isSpotEmpty(spot):
        return (spot)
    else:
        print ("That spot is already taken! Please enter another spot: ")
        if character is "X":
            return getSpot(character)
        else:
            return getSpot(character)

# Returns whether the given spot is empty or not.
# Uses the placeholder to check this.
def isSpotEmpty(spot):
    if gameBoard[spot[0]][spot[1]] == placeholder:
        return True
    else:
        return False

# Sets the given spot on the game board to X.
def setXSpot(spot):
    gameBoard[spot[0]][spot[1]] = "X"

# Sets the given spot on the game board to O.
def setOSpot(spot):
    gameBoard[spot[0]][spot[1]] = "O"

# Logic check to see if a player has won or lost.
def gameOver():
    if horizontalWin():
        return True
    if diagonalWin():
        return True
    if verticalWin():
        return True
    if isDraw():
        return True
    return False

# Logic check to see if there is three in-a-row horizontally.
def horizontalWin():
    global outcome # Needed to modify global copy of outcome.
    
    if gameBoard[0][0] == gameBoard[0][1] and gameBoard[0][1] == gameBoard[0][2]:
        if gameBoard[0][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[0][0] == "X":
            outcome = "Player 1 wins!"
            return True
    elif gameBoard[1][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[1][2]:
        if gameBoard[1][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[1][0] == "X":
            outcome = "Player 1 wins!"
            return True
    elif gameBoard[2][0] == gameBoard[2][1] and gameBoard[2][1] == gameBoard[2][2]:
        if gameBoard[2][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[2][0] == "X":
            outcome = "Player 1 wins!"
            return True
        
    return False # Wasn't a horizontal win.

# Logic check to see if there is three in-a-row diagonally.
def diagonalWin():
    global outcome # Needed to modify global copy of outcome.
    
    if gameBoard[0][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][2]:
        if gameBoard[0][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[0][0] == "X":
            outcome = "Player 1 wins!"
            return True
    if gameBoard[0][2] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[2][0]:
        if gameBoard[0][2] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[0][2] == "X":
            outcome = "Player 1 wins!"
            return True
        
    return False # Wasn't a diagonal win.

# Logic check to see if there is three in-a-row vertically.
def verticalWin():
    global outcome # Needed to modify global copy of outcome.
    
    if gameBoard[0][0] == gameBoard[1][0] and gameBoard[1][0] == gameBoard[2][0]:
        if gameBoard[0][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[0][0] == "X":
            outcome = "Player 1 wins!"
            return True
    elif gameBoard[1][0] == gameBoard[1][1] and gameBoard[1][1] == gameBoard[1][2]:
        if gameBoard[1][0] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[1][0] == "X":
            outcome = "Player 1 wins!"
            return True
    elif gameBoard[0][2] == gameBoard[1][2] and gameBoard[1][2] == gameBoard[2][2]:
        if gameBoard[0][2] == "O":
            outcome = "Player 2 wins!"
            return True
        elif gameBoard[0][2] == "X":
            outcome = "Player 1 wins!"
            return True
        
    return False # Wasn't a vertical win.

# Logic check to see if the board doesn't have anymore placeholders.
# (All spots have an X or an O.)
def isDraw():
    global outcome # Needed to modify global copy of outcome.

    if not placeholder in gameBoard[0] and not placeholder in gameBoard[1] and not placeholder in gameBoard[2]:
        outcome = "It's a draw!"
        return True
    
    return False # Wasn't a draw.

# Print the game board.
def printBoard():
    print(gameBoard[0][0] + "|" + gameBoard[0][1] + "|" + gameBoard[0][2])
    print("- - -")
    print(gameBoard[1][0] + "|" + gameBoard[1][1] + "|" + gameBoard[1][2])
    print("- - -")
    print(gameBoard[2][0] + "|" + gameBoard[2][1] + "|" + gameBoard[2][2])

main()
