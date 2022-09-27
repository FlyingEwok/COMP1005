def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def __convertToBool(variable: any) -> None:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    if variable == "True":
        return True
    elif variable == "False": 
        return False

def __checkIfLeapYear(year: int) -> bool: # Obsolete function that I didn't need to make, but I put the effort into it so it's staying here
    """Checks if the year is a leap year: Calculation instructions obtained from: https://learn.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year , Python code created by myself"""
    # Calculation

    if year % 4 == True:
        if year % 100 == True:
            if year % 400 == True:
                leapYear = True
            else:
                leapYear = False
        else:
            leapYear == True
    else:
        leapYear = False

def askUserPersonalInfo() -> list:
    """Obtains the name, current year, and birth year from the user and returns information in a list"""
    usersName = input("\nWhat is your name? ")

    # Current Year
    currentYear = input("\nWhat year is it? ")
    while __checkIfConvertsToInt(currentYear) == False: # Check if currentYear can be converted to int
        # Ask for the year again
        currentYear = input("\nInvalid input! Not a integer!\nTry again!\nWhat year is it? ")
    else:
        currentYear = int(currentYear) # Convert

    # Birth Year
    birthYear = input("\nWhat year were you born? ")
    while __checkIfConvertsToInt(birthYear) == False: # Check if birthYear can be converted to int
        # Ask for the birth year again
        birthYear = input("\nInvalid input! Not a integer!\nTry again!\nWhat year were you born? ")
    else:
        birthYear = int(birthYear) # Convert

    # Birthday this year
    birthdayThisYear = input("\nDid you have a birthday this year? True/False: ")
    # Check if the user typed the correct string
    while not birthdayThisYear == "True" and not birthdayThisYear == "False":
        print(birthdayThisYear)
        birthdayThisYear = input("\nInvalid Input\nPlease type 'True' or 'False'\nDid you have a birthday this year? True/False: ") # ask again
    else:
        birthdayThisYear = __convertToBool(birthdayThisYear) # Check if user typed True or False and if they did convert to bool

    # Born on Feb 29th
    bornOnFeb29 = input("\nWere you born on February 29th? True/False: ") # Ask user for input
    # Check if the user typed the correct string
    while not bornOnFeb29 == "True" and not bornOnFeb29 == "False":
        print(bornOnFeb29)
        bornOnFeb29 = input("\nInvalid Input\nPlease type 'True' or 'False'\nWere you born on February 29th? True/False: ") # ask again
    else:
        bornOnFeb29 = __convertToBool(bornOnFeb29) # Check if user typed True or False and if they did convert to bool

    # Create a list with values
    information = [usersName,currentYear,birthYear, birthdayThisYear, bornOnFeb29] # Create an empty list
    return information

def performCalculations(information: list) -> list: 
    """Calculates the age of a person given the year, year of birth, and etc..."""      
    if information[3] == True:
        userAge = information[1] - information [2] # Perform the age calculation
    else:
        userAge = (information[1] - information [2]) - 1 # Perform the age calculation but subtract 1 as they haven't had a birthday yet this year

    if __checkIfLeapYear(information[2]):
        if information[4] == True: # If they're born on a leap day calculate their actual age
            userAge = userAge//4
    else:
        print("Ignoring response, as the year entered is not a leap year!\n")
    
    information.append(userAge) # Append the users age to the list

# Main
information = askUserPersonalInfo() # Ask the user for the info and make the list
performCalculations(information) # Calculate age
print(information) # Print list for reference
# Print a statement with all the information
print(f"Your name is {information[0]} and you were born in {information[2]}, which makes you {information[5]} years old!")

