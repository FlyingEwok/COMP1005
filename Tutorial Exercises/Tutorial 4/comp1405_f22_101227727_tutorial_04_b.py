# Nicholas Garth 101227727
from random import randint

def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def userGuess() -> int:
    """Converts user input to an int and returns the integer"""
    guess = input("\nEnter a number between 1 and 100 for your guess: ")
    while not __checkIfConvertsToInt(guess) or int(guess) < 1 or int(guess) > 100: # Error and condition handling
        guess = input("Invalid Input!\nTry Again!\nEnter a number between 1 and 100 for your guess: ")
    else:
        return int(guess)

def guessingGame() -> bool:
    """Performs guessing algorithm on the users guesses and returns win status"""
    randomNum = randint(1, 100)
    numOfGuesses = 10

    # Loop for 10 times 
    for guess in range(numOfGuesses):
        print(f"You have {(numOfGuesses) - guess} guesses left!")
        usersGuess = userGuess()
        # Perform check on the guess
        if usersGuess == randomNum:
            print("\nYou guessed the correct number!! 🫡")
            hasWon = True # Set a variable for after loop check for the correct message
            break # Break out of the loop
        elif usersGuess > randomNum:
            print("\nThe number is Lower!\nBy how much?\nYou can't know that silly 😛")
            hasWon = False # Set a variable for after loop check for the correct message
        elif usersGuess < randomNum:
            print("\nThe number is Higher!\nBy how much?\nYou can't know that silly 😛")
            hasWon = False # Set a variable for after loop check for the correct message
    return hasWon
    
def gameResults(hasWon: bool) -> None:
    """Given the game result as a boolean print if the user has one or lost"""
    if hasWon:
        print("\nCongrats! You Win!\nHere's a cookie   🍪")
    else:
        print("\nYou have Lost!\nHere's a pile of poo  💩")

# Main
gameResults(guessingGame())
