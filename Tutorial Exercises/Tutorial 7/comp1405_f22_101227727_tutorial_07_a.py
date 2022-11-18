# Nicholas Garth 101227727

def isValidMatrix(matrix: list) -> bool:
    """Runs a series of checks to determine if the matrix is a valid numeric matrix, returns a boolean"""
    row1Checked = False # Initialize check to verify the first row has been completed
    for row in matrix:
        # Check if the matrix elements are lists
        if type(row) == list:
            matrixElementsIsList = True
        else:
            matrixElementsIsList = False
            break
        
        # Check if each Row is the same length as the first row
        if not row1Checked:
            row1Length = len(row) # Save the length of the first row
            row1Checked = True

        if len(row) == row1Length:
            rowLengthSame = True
        else:
            rowLengthSame = False
            break

        # Check if each element in a matrix is a numeric value
        for element in row:
            if type(element) == int or type(element) == float:
                allElementsAreNumeric = True
            else:
                allElementsAreNumeric = False
                break
    
    # Return a True/False if the matrix is a valid matrix
    if matrixElementsIsList and rowLengthSame and allElementsAreNumeric:
        return True
    else:
        return False

# Main (Test cases)
matrixTest1 = [[1,2,3,4,5],
               [6,5,3.6,7,2],
               [1,9,5,3,8]     
              ]

matrixTest2 = [2,3,6,3,2, 
               [1,2,3,4,5],
               [6,5,3,7,2],
               [1,9,5,3,8]   
              ]

matrixTest3 = [[1,2,3,4,5],
               [6,5,3,7,2,9],
               [1,9,5,3,8]     
              ]

matrixTest4 = [[1,2,3,4,5],
               [6,5,3,7,2],
               [1,9,'pie',3,8]     
              ]

print(f"Matrix 1 is a {isValidMatrix(matrixTest1)} numeric matrix")
print(f"Matrix 2 is a {isValidMatrix(matrixTest2)} numeric matrix")
print(f"Matrix 3 is a {isValidMatrix(matrixTest3)} numeric matrix")
print(f"Matrix 4 is a {isValidMatrix(matrixTest4)} numeric matrix")