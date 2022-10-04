def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def acquireGrades() -> list:
    """Acquires the students final grades in each category"""
    # Variables
    tutorials = input("What is your final tutorial grade? ")
    quizzes = input("What is your final quizzes grade ?")
    assignments = input("What is your final assignments grade? ")
    exam = input("What is your final exam grade? ")

    # Convert to integer
    while __checkIfConvertsToInt(tutorials):
        int(tutorials)
    else:
        tutorials = input("What is your final tutorial grade? ")

    while __checkIfConvertsToInt(quizzes):
        int(quizzes)
    else:
        quizzes = input("What is your final quizzes grade? ")

    while __checkIfConvertsToInt(assignments):
        int(assignments)
    else:
        assignments = input("What is your final assignments grade? ")

    while __checkIfConvertsToInt(exam):
        int(exam)
    else:
        exam = input("What is your final exam grade? ")



    