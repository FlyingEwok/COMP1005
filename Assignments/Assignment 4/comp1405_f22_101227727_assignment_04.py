# Nicholas Garth 101227727 (Oops just realized I needed to do this with this assignment)

# Sub Genre Selection: Space Opera and Super Hero
# 10 Space Opera Films: Star Wars Revenge Of The Sith, Star Wars The Last Jedi, Star Wars Return of the Jedi, Rogue One, Star Wars The Phantom Menace, Solo, Dune, Star Wars A New Hope, Star Wars The Force Awakens, Star Wars Rise of Skywalker
# 10 Super Hero Films: Spiderman (2002), The Dark knight, Ghost Rider, Avengers, Justice League, Spiderman No Way Home, The Amazing Spiderman, The Incredible Hulk, Wonder Woman, Aquaman

def __checkIfConvertsToBool(variable: str) -> bool:
    """Checks if given variable can be converted to a bool and then returns a boolean"""
    if (variable == "Yes" or variable == "yes" or variable == "y" or variable == "Y"): # Check if variable is Yes/True or No/False and return 
        return True
    elif (variable == "No" or variable == "no" or variable == "n" or variable == "N"):
        return False
    else:
        print("Please type Yes or No as your answer\nTry Again") # Error handling
        exit(1)

def setOfQuestionsSuperHero() -> bool:
    """Returns a boolean of answers from the user"""
    # Define Variables
    soloSuperHeroMovie = False
    avengersOrJusticeLeague = False
    ragingGreenMonster = False
    antagonistOrProtagonist = False
    protagonistMotorcycle = False
    motorcycleType = False
    willemDafoe = False
    tobeyMaguire = False
    mainCharacterTobey = False

    # If Super Hero Film Questions
    soloSuperHeroMovie = __checkIfConvertsToBool(input("Is the Film a solo Super Hero Movie? Yes/No ")) # Eliminates Justice League and Avengers (Or narrows down to) (answerListSuperHero[1])
    
    # If is not a Solo Super Hero Film
    if not soloSuperHeroMovie:
        avengersOrJusticeLeague = __checkIfConvertsToBool(input("Does the Film have a Speedster Super Hero? Yes/No ")) # If does it's Justice League, If not Avengers (answerList[2])
        pass
    else: # If is a Solo Super Hero Film
        # Check if film has raging green Monster
        ragingGreenMonster = __checkIfConvertsToBool(input("Does the Film have a raging Green Monster? Yes/No ")) # if it does the film is either The Amazing Spiderman or the Incredible Hulk (answerList[3])
        # If has a raging Green Monster
        if ragingGreenMonster:
            antagonistOrProtagonist = __checkIfConvertsToBool(input("Is the raging Green Monster the Protagonist? Yes/No ")) # if it is the film is the Incredible Hulk, If not it's the Amazing Spiderman (answerList[4])
        else:
            # If protagonist drives a motorcycle
            protagonistMotorcycle = __checkIfConvertsToBool(input("Does the protagonist drive a motorcycle? Yes/No ")) # if protagonist does ride a motorcycle then film is either Dark Knight or Ghost Rider (answerList[5])
            # Determine if it's Ghost Rider or Batman
            if protagonistMotorcycle:
                motorcycleType = __checkIfConvertsToBool(input("Does the protagonist rely on technology? Yes/No ")) # If he does then it's Batman, otherwise it's Ghost Rider (answerList[6])
            else:
                # If the film stars Willem Dafoe
                willemDafoe = __checkIfConvertsToBool(input("Is Willem Dafoe in the Film? Yes/No ")) # If he is then it's either Spiderman (2002), Spiderman No Way Home, or Aquaman (answerList[7])
                # Determine if Tobey Maguire is in the film otherwise
                if willemDafoe:
                    tobeyMaguire = __checkIfConvertsToBool(input("Is Tobey Maguire in the Film? Yes/No ")) # If he is then it's either Spiderman (2002) or Spiderman No Way Home (answerList[8])
                    # If Tobey Maguire is in the film ask if he's the main character
                    if tobeyMaguire:    
                        mainCharacterTobey = __checkIfConvertsToBool(input("Is Tobey Maguire the main character of the Film? Yes/No ")) # If he is then the film is Spiderman (2002), if not then Spiderman No Way Home (answerList[9])
    answerListSuperHero = [soloSuperHeroMovie,avengersOrJusticeLeague,ragingGreenMonster,antagonistOrProtagonist,protagonistMotorcycle,motorcycleType,willemDafoe,tobeyMaguire,mainCharacterTobey]
    return answerListSuperHero

def superHeroFilmAlgorithm(answerListSuperHero: list):
    # Checks if a Solo super hero film
        if answerListSuperHero[0]:
            # Determine if the film has raging Green Monster
            if answerListSuperHero[2]:
                # Determine if the raging green monster is the protagonist (Determines movie title!)
                if answerListSuperHero[3]:
                    print('"The Incredible Hulk" is the film title') 
                else:
                    print('"The Amazing Spiderman" is the film title.')
            else:
                # Determines if the protagonist has a motorcycle
                if answerListSuperHero[4]:
                    # Determine if the protagonist rely on technology (Determines movie title!)
                    if answerListSuperHero[5]:
                        print('"The Dark Knight" is the film title.')
                    else:
                        print('"Ghost Rider" is the film title.')
                else:
                    # Determine if Willem Dafoe is in the film
                    if answerListSuperHero[6]:
                        # Determine if the film stars Tobey Maguire and if it doesn't the film is Aquaman
                        if answerListSuperHero[7]:
                            # Determine if Tobey Maguire is the main character if not then the film is Spider-Man No Way Home
                            if answerListSuperHero[8]:
                                print('"Spider-Man (2002)" is the film title.')
                            else:
                                print('"Spider-Man No Way Home" is the film title.')
                        else:
                            print('"Aquaman" is the film title.')
                    else:
                        print('"Wonder Woman" is the film title.')
        else:
            # Determine if the film has a speedster (Determines movie title!)
            if answerListSuperHero[1]: # Determined Justice League is the film
                print('"Justice League" is the film title.')
            else:
                print('"Avengers" is the film title.')

#def setOfQuestionsSpaceOpera(subGenreFilmQuestion: bool) -> bool: 

def performAlgorithm(superHero: bool) -> str:    
    # Determine the Genre of the Film
    if superHero: # If Super Hero Film
        answerListSuperHero = setOfQuestionsSuperHero()
        superHeroFilmAlgorithm(answerListSuperHero)
    else: # If Space Opera
        pass

# Main

# Genre Question
subGenreFilmQuestion = __checkIfConvertsToBool(input("Does the film take place on planet Earth? Yes/No "))
performAlgorithm(subGenreFilmQuestion)
