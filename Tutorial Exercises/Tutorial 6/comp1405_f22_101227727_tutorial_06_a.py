# Nicholas Garth 101227727
def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def printOptions() -> str:
    """Prints options and asks user to select one and return the selection"""
    print("Enter the number associated with the option you want:\n1. Quit\n2. Add to end of list\n3. Remove from list\n4. Add to specific index of list")
    selection = input("\nEnter an option: ")

    return selection

def actionForLoop(var: str) -> bool:
    """Checks if user enters Q and returns a bool"""
    # Check if user wants to quit
    if var.upper() == 'Q':
        wantsToQuit = True
        return wantsToQuit

def appendValueToList(list: list) -> list:
    """Adds a value to the end of the list given by the user"""
    var = input("Enter a string to insert into a list: ")
    list.append(var)
    return list

def removeValueFromList(list: list) -> list:
    """Removes a particular index from a list given by user"""
    askAgain = True
    while askAgain:
        indexToRemove = input("Enter the position of the element you'd like to remove: ")
        # Checks if can convert to int and converts
        while not __checkIfConvertsToInt(indexToRemove):
            indexToRemove = input("Invalid Input!\nTry Again!\nEnter the position of the element you'd like to remove: ")
        else:
            indexToRemove = (int(indexToRemove) - 1) # Subtract 1 since lists start counting from 0
        
        # Error handling
        try:
            list.pop(indexToRemove)
            askAgain = False
        except IndexError:
            print("Not Applicable try again!")
            askAgain = True

def addValueToList(list: list) -> list:
    """Adds value to specific index given by user"""
    indexToAdd = input("Enter the position of the element you'd like to add: ")
    var = input("Enter a string to insert into a list: ")
    
    # Checks if can convert to int and converts
    while not __checkIfConvertsToInt(indexToAdd):
        indexToAdd = input("Invalid Input!\nTry Again!\nEnter a string to insert into a list: ")
    else:
        indexToAdd = (int(indexToAdd) - 1) # Subtract 1 since lists start counting from 0
    
    list.insert(indexToAdd, var) # Inserts into position on list
    return list


def checkListLength(list: list) -> int:
    """Counts the length of a list"""
    listLength = 0
    # Iterate through the list and for each value in the list count the length
    for i in list:
        listLength +=1
    return listLength

# Main
list = []
selection = 0
while not selection == '1':
    selection = printOptions()

    while selection == '1': # Quit
        print(f"The length of the list is: {checkListLength(list)}\nThe list is {list}")
        break
    while selection == '2': # Append to list
        appendValueToList(list)
        print(f"The length of the list is: {checkListLength(list)}\nThe list is {list}")
        selection = 0 # Reset selection to kill loop
    while selection == '3': # Remove from list at certain index
        while checkListLength(list) > 0: 
            removeValueFromList(list)
            print(f"The length of the list is: {checkListLength(list)}\nThe list is {list}")
            selection = 0 # Reset selection to kill loop
        else:
            print("Not Applicable! Nothing to remove from list!")
            break
    while selection == '4': # Adds element to at certain index
        addValueToList(list)
        print(f"The length of the list is: {checkListLength(list)}\nThe list is {list}")
        selection = 0 # Reset selection to kill loop
        
