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
A1 = __checkIfConvertsToBool(sys.argv[1])
C1 = __checkIfConvertsToBool(sys.argv[2])
E1 = __checkIfConvertsToBool(sys.argv[3])
H1 = __checkIfConvertsToBool(sys.argv[4])
L1 = __checkIfConvertsToBool(sys.argv[5])
I1 = __checkIfConvertsToBool(sys.argv[6])

A2 = __checkIfConvertsToBool(sys.argv[7])
C2 = __checkIfConvertsToBool(sys.argv[8])
E2 = __checkIfConvertsToBool(sys.argv[9])
H2 = __checkIfConvertsToBool(sys.argv[10])
L2 = __checkIfConvertsToBool(sys.argv[11])
I2 = __checkIfConvertsToBool(sys.argv[12])

booleanAlgorithim(A1,C1,E1,H1,L1,I1) # Run the logic on the variables
booleanAlgorithim(A2,C2,E2,H2,L2,I2) # Run the logic on the variables
