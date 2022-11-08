# Nicholas Garth 101227727
from random import randint

def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def populateList(list: list) -> list:
    """Creates a randomly populated list of integers and returns"""
    listSize = input("What is the size of the random list? ")
    
    # Check if value entered is an convertible to int and convert it if it is
    while not __checkIfConvertsToInt(listSize):
        listSize = input("Invalid Input!\nTry Again!\nWhat is the size of the random list? ")
    else:        
        listSize = int(listSize)

    # Append random nums
    for n in range(listSize):
        list.append(randint(1, 10)) # Append random numbers from 1 to 10

def replaceValueInList(list: list) -> None:
    """Replaces a specified int in a list with a specified string"""
    valToSwap = input("What is the integer you want to swap? ")
    # Check if value entered is an convertible to int and convert it if it is
    while not __checkIfConvertsToInt(valToSwap): 
        valToSwap = input("Invalid Input!\nTry Again!\nWhat is the integer you want to swap? ")
    else:        
        valToSwap = int(valToSwap)
    
    newVal = input("Enter the string you'd like to replace with: ")

    # Perform swap
    for val in range(checkListLength(list)):
        if list[val] == valToSwap:
            list[val] = newVal

def checkListLength(list: list) -> int:
    """Counts the length of a list"""
    length = 0
    
    # Iterate through the list and for each value in the list count the length
    for i in list:
        length +=1
    return length

def countNumOfStrings(list: list) -> int:
    """Counts the number of strings in a list and returns the count as int"""
    numOfStr = 0

    for val in range(checkListLength(list)):
        if type(list[val]) == str:
            numOfStr += 1
    return numOfStr

def askIfWantToGoAgain() -> bool:
    """Checks if user wants to perform another replacement and returns a boolean"""
    askAgain = True
    while askAgain:
        goAgain = input("Would you like to replace another integer in the list? Y/N:  ")

        if goAgain.upper() == 'Y':
            askAgain = False
            return True
        elif goAgain.upper() == 'N':
            askAgain = False
            return False
        else:
            print("Invalid Input!\nTry Again!")
            askAgain = True
        

# Main
list = []
wantToGoAgain = True

populateList(list)
print(f"The list generated is: {list}")

# Run this until the user is done entering operations
while wantToGoAgain:
    replaceValueInList(list)
    print(f"The list is: {list} and it contains {countNumOfStrings(list)} strings!")
    wantToGoAgain = askIfWantToGoAgain()

    
