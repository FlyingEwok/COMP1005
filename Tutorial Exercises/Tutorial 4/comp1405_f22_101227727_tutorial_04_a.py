# Nicholas Garth 101227727

def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def convertToInt() -> int:
    """Converts userinput to an int and returns"""
    numberRow = input("Enter a number for the number tree: ")
    while not __checkIfConvertsToInt(numberRow) or int(numberRow) < 0 or int(numberRow) > 9: # Error and condition handling
        numberRow = input("Invalid Input!\nTry Again!\nEnter a number for the number tree: ")
    else:
        return int(numberRow)

def makeNumberTriangle(numberRow: int) -> None:
    """Creates a number triangle given the number of rows"""    
    for i in range(numberRow + 1): # Iterate through and add 1 so it counts to actual number since range starts at 0 and we want it to print the last row
        for j in range(i): # Cycle through the range of i to print the amount of digits in each row
            print(i, end='') # Apply print formatting so new line isn't created every print
        print("") # Create a new row

# Main
makeNumberTriangle(convertToInt()) # Run the program