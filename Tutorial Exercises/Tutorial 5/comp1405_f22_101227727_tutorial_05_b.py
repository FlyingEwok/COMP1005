# Nicholas Garth 101227727
from random import randint

def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def userInputInterpolation() -> int:
    """Grabs userinput and Converts userinput to an int and returns as well as detects if the user wants to quit"""
    userSelction = input("Type the number associated with the option\n1. Rock\n2. Paper\n3. Scissors\nSelect your option: ")
    
    # Check if user wants quit
    while userSelction.upper() == 'Q':
        print("Have a Nice Day!")
        exit()
    
    # Error and condition handling
    while not __checkIfConvertsToInt(userSelction) or int(userSelction) > 3 or int(userSelction) < 1:
        userSelction = input("Invalid Input!\nTry Again!\n\nType the number associated with the option:\n1. Rock\n2. Paper\n3. Scissors\nSelect your option: ")
    else:
        return int(userSelction)

def rockPaperScissorsGame():
    # Assign number to variable with name of game element 
    Rock = 1
    Paper = 2
    Scissors = 3  
    
    selectionList = ['Rock', 'Paper', 'Scissors'] # Create a list to print the matchups
    
    # Define selection variables
    userSelection = userInputInterpolation()
    opponentSelection = randint(1,3)

    print(f"\nThe Match Up Is: {selectionList[userSelection-1]} VS {selectionList[opponentSelection-1]}") # Subtract 1 from the selections due to how lists work

    # Check the selection and rank them against eachother
    if userSelection == opponentSelection:
        print("TIE!")
    elif (userSelection == Rock and opponentSelection == Paper) or (userSelection == Paper and opponentSelection == Scissors) or (userSelection == Scissors and opponentSelection == Rock):
        print("YOU LOSE!")
    else:
        print("YOU WIN!")

def runProgram() -> None:
    """Infinitely runs the program"""
    # Tell user how to quit
    print("Enter the letter 'Q' to quit at any point!\n")
    
    # Infinitely loop the program
    while True:
        rockPaperScissorsGame()

# Main
runProgram()