def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def magicNumbers(number: int) -> int:
    """Takes in a 7 digit number and does the magic calculation on it"""
    numberString = str(number) # Convert number to string
    
    # Obtain the prefix and line number
    try: # Error handling
        prefix = numberString[0] + numberString[1] + numberString[2] 
        lineNumber = numberString[3] + numberString[4] + numberString[5] + numberString[6]
    except IndexError:
        return False

    # Convert them back to integer    
    prefix = int(prefix)
    lineNumber = int(lineNumber)

    # Perform Calculations and print out statements
    result = (prefix * 80)
    print(f"\nYour prefix is {prefix}. Multiply this by 80, and the result is: {result}")
    result = (result + 1) * 250
    print(f"Add 1 to that result and multiply it by 250, and the result is: {result}")
    result = result + (lineNumber * 2)
    print(f"Your line number is {lineNumber}. Add this to the previous result twice, and the result is: {result}")
    result = (result - 250)//2
    print(f"Subtract 250 from that result and divide it by 2, and the result is: {result}")


# Main
sevenDigitPhoneNum = input("Enter a 7 seven digit phone number (no area code): ") # Ask for the number

# Error Handling! Force the user to enter only a 7 digit number
while magicNumbers(sevenDigitPhoneNum) == False:
    sevenDigitPhoneNum = input("\nNot a 7 digit number\nPlease Try Again\nEnter a 7 seven digit phone number (no area code): ")
else:
    sevenDigitPhoneNum = int(sevenDigitPhoneNum)
    