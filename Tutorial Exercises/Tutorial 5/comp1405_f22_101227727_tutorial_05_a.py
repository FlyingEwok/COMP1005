# Nicholas Garth 101227727

def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def userInputInterpolation() -> int:
    """Grabs userinput and Converts userinput to an int and returns as well as detects if the user wants to quit"""
    userNum = input("\nEnter a number to determine if prime number: ")
    
    # Check if user wants quit
    while userNum.upper() == 'Q':
        print("Have a Nice Day!")
        exit()
    
    # Error and condition handling
    while not __checkIfConvertsToInt(userNum):
        userNum = input("Invalid Input!\nTry Again!\n\nEnter a number to determine if prime number ")
    else:
        return int(userNum)

def isPrimeNumber(num: int) -> bool:
    """Takes a number and determines if it's a prime number"""
    notPrime = False
    i = 2 # Start at 2 because prime numbers are greater than 1
    while i <= (num/2):
        if (num%1) == 0: # Check if not prime
            notPrime = True
            break
        i += 1
    
    # Check if user entered a number less than or equal to 1 (as any number in that range is not prime)
    if num > 1:
        return notPrime
    else:
        notPrime = True
        return notPrime

def printResults(notPrime: bool) -> None:
    """Prints the results of isPrimeNumber"""
    if notPrime: # If not a prime number statement
        print("The number you entered is not a prime number!")
    else: # If prime number statement 
        print("The number you entered is a prime number!")

def runProgram() -> None:
    """Infinitely runs the program"""
    # Tell user how to quit
    print("Enter the letter 'Q' to quit at any point!\n")
    
    # Infinitely loop through the program
    while True:
        printResults(isPrimeNumber(userInputInterpolation()))  

# Main
runProgram()
