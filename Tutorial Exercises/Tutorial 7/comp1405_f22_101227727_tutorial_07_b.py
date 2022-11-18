# Nicholas Garth 101227727

def __compareRowLength(matrix1Row: list, matrix2Row: list) -> int:
    # Check if each Row is the same length as the first row
    matrix1RowLength = len(matrix1Row) # Save the length of the first row


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

def addMatrix(matrix1: list, matrix2: list) -> list:
    # Since we check if the matrix is valid before calling this function we can assume Row 0 is the same as all other rows in the matrix
    if len(matrix1[0]) == len(matrix2[0]):
        result = [[matrix1[row][column] + matrix2[row][column]  for column in range(len(matrix1[0]))] for row in range(len(matrix1))]
    else:
        result = []
    
    return result

# Main (Test cases)
matrix1 = [[1,2,3,4,5],
           [6,5,3.6,7,2],
           [1,9,5,3,8]     
          ]

matrix2 = [[9,8,3,4,5],
           [6,5,9.8,5,2],
           [1,9,3,3,1]     
          ]

if isValidMatrix(matrix1) and isValidMatrix(matrix2):
    results = addMatrix(matrix1,matrix2)
    # Check if the matrixes were able to be added together
    if not len(results) == 0:
        print("The added matrix is:")
        # Print in terminal looking like a matrix
        for result in results:
            print(result)
    else:
        print("These Matrixes can't be added!")
else:
    print("One of the matrix are not a valid matrix")

