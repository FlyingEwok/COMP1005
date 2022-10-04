import sys
def __checkIfConvertsToBool(variable: str) -> bool:
    """Checks if given variable can be converted to a bool and then returns a boolean"""
    if (variable == "True" or variable == "1"): # Check if variable is True or False and return 
        return True
    elif (variable == "False" or variable == "0"):
        return False
    else:
        print("At least one of the values you entered is invalid.\nTry Again") # Error handling
        exit(1)

def booleanAlgorithim(A: bool, C: bool, E: bool, H: bool, L: bool, I: bool) -> bool:
    """Performs logic on a set of booleans and print the result"""
    result1 = (E or ((not C) and (A or C)))
    result2 = (((not H) or L) or I) and (not I)

    print(f"<{result1},{result2}>")

# Variables
A = __checkIfConvertsToBool(sys.argv[1])
C = __checkIfConvertsToBool(sys.argv[2])
E = __checkIfConvertsToBool(sys.argv[3])
H = __checkIfConvertsToBool(sys.argv[4])
L = __checkIfConvertsToBool(sys.argv[5])
I = __checkIfConvertsToBool(sys.argv[6])

booleanAlgorithim(A,C,E,H,L,I) # Run the logic on the variables
