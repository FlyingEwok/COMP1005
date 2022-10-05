import string

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
    quizzes = input("What is your final quizzes grade? ")
    assignments = input("What is your final assignments grade? ")
    exam = input("What is your final exam grade? ")

    # Convert to integer
    while (__checkIfConvertsToInt(tutorials) == False) or ((int(tutorials) < 0 or int(tutorials) > 100)):
        tutorials = input("Invalid tutorials Input!\nWhat is your final tutorial grade? ")
    else:
        tutorials = int(tutorials)

    while (__checkIfConvertsToInt(quizzes) == False) or ((int(quizzes) < 0 or int(quizzes) > 100)):
        quizzes = input("Invalid quizzes Input!\nWhat is your final quizzes grade? ")
    else:
        quizzes = int(quizzes)

    while (__checkIfConvertsToInt(assignments) == False) or ((int(assignments) < 0 or int(assignments) > 100)):
        assignments = input("Invalid assignments Input!\nWhat is your final assignments grade? ")
    else:
        assignments = int(assignments)

    while (__checkIfConvertsToInt(exam) == False) or ((int(exam) < 0 or int(exam) > 100)):
        exam = input("Invalid exam Input!\nWhat is your final exam grade? ")
    else:
        exam = int(exam)

    grades = [tutorials,quizzes,assignments,exam] # put grades in a list
    return grades

def computeFinalGrade(grades: list) -> int:
    """Computes a final grade as a percentage returns the final grade"""
    tutorialFinal = int(grades[0] * 0.10)
    quizFinal = int(grades[1] * 0.30)
    assignmentFinal = int(grades[2] * 0.40)
    examFinal = int(grades[3] * 0.20)

    finalGrade = tutorialFinal + quizFinal + assignmentFinal + examFinal # Calculate final grade
    return finalGrade

def convertGradePercentToLetter(gradePercent: int) -> string:
    """Converts the grade to a letter grade and returns that letter"""
    if gradePercent >= 90: gradeLetter = "A+"
    elif gradePercent > 85 < 90: gradeLetter = "A"
    elif gradePercent > 80 < 85: gradeLetter = "A-" 
    elif gradePercent > 77 < 80: gradeLetter = "B+" 
    elif gradePercent > 73 < 77: gradeLetter = "B" 
    elif gradePercent > 70 < 73: gradeLetter = "B-" 
    elif gradePercent > 67 < 70: gradeLetter = "C+"
    elif gradePercent > 63 < 67: gradeLetter = "C"
    elif gradePercent > 60 < 63: gradeLetter = "C-"
    elif gradePercent > 57 < 60: gradeLetter = "D+"
    elif gradePercent > 53 < 57: gradeLetter = "D"
    elif gradePercent > 50 < 53: gradeLetter = "D-"
    elif gradePercent > 0 < 50: gradeLetter = "F"
    else: gradeLetter = "If you managed to get this message then you're a witch!"      

    return gradeLetter

# Main
gradeList = acquireGrades()
percentGrade = computeFinalGrade(gradeList)
letterGrade = convertGradePercentToLetter(percentGrade)

print(f"Your grade in percentage is: {percentGrade}, and your letter grade is: {letterGrade}")

