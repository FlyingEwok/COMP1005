import sys

def __checkIfConvertsToFloat(variable: any) -> bool:
    """Checks if given variable can be converted to a float and then returns a boolean"""
    try: # Try converting to float if error return False if no error return True
        float(variable)
        return True
    except ValueError:
        return False

def applyAlgorithim(userinput: float) -> chr:
    """Applies the set of instructions received in cmail"""
    # Perform multiplication of 5 to the operation
    firstOperation = operations = userinput * 5
    print(f"{userinput} multiplied by 5 equals: {operations}")
    
    # Performs the modulus of 3 to the operation
    secondOperation = operations = operations % 3
    print(f'The remainder of {firstOperation} when divided by 3 equals: {operations}')
    
    # Checks if Command Line argument exists and checks if argument can convert to float. If both cases are satisfied add to the operation 
    if len(sys.argv) > 1:
        if __checkIfConvertsToFloat(sys.argv[1]):
            thirdOperation = operations = operations + float(sys.argv[1]) # adds this particular position of command line argument array to the operation
            print(f"The command line arguments added to {secondOperation} is: {operations}")
    else:
        print("Command Line argument does not exist or is not a number")
        thirdOperation = operations # Set the thirdOperation to operations as nothing would change in this case
    
    # Performs an addition with an integer that is one more than itself
    fourthOperation = operations = operations + (operations + 1)
    print(f"{thirdOperation} added to {thirdOperation} + 1 is: {operations}")
    
    # Performs a multiplication of 2.516229 to the operation
    fifthOperation = operations = operations * 2.516229
    print(f"{fourthOperation} multiplied by 2.516229 is: {operations}")
    
    # Converts the float to an integer
    sixthOperation = operations = int(operations)
    print(f"{fifthOperation} as an integer is: {operations}")
    
    # Converts the integer into a character
    operations = chr(operations)
    print(f"{sixthOperation} as a character is: <{operations}>")

    return operations


# Main Program
userinput = input("Enter any number: ") # Gets users input

# Checks if the user entered a number that can convert to a float and if it isn't keep asking the user to try again
while __checkIfConvertsToFloat(userinput) == False:
    userinput = input("\nInvalid Input: Not a number\nPlease Try Again\nEnter any number: ")
else:
    userinput = float(userinput) # Convert the string to a float
    
# Run the function and print the Returned value
print(f"\nFinal Result: <{applyAlgorithim(userinput)}>")





