# Nicholas Garth 101227727 (Oops just realized I needed to do this with this assignment)

# Sub Genre Selection: Space Opera and Super Hero

# 10 Space Opera Films and distinguishing elements: 
# 1. Star Wars Revenge Of The Sith (Directed and Written By George Lucas; Not Tatooine Prominent)
# 2. Star Wars The Last Jedi (Made By Disney; Snoke In Film; Directed by Rian Johnson)
# 3. Star Wars Return of the Jedi (Directed By George Lucas)
# 4. Star Wars Rise of Skywalker (Made By Disney)
# 5. Star Wars The Phantom Menace (Directed and Written By George Lucas; Jar Jar Binks Prominent)
# 6. Star Wars The Empire Strikes Back (Directed By George Lucas; Luke has real hand)
# 7. Dune (Not Star Wars)
# 8. Star Wars A New Hope (Directed and Written By George Lucas)
# 9. Star Wars The Force Awakens (Made By Disney; Snoke In Film)
# 10. Star Wars Attack of the Clones (Directed and Written By George Lucas; Ewan Mcgregor Obi-Wan)


# 10 Super Hero Films and distinguishing elements: 
# 1. Spiderman (2002) (Solo Film; Willem Dafoe; Tobey Maguire; Tobey Magure as protagonist)
# 2. The Dark knight (Solo Film; protagonist motorcycle; rely on tech)
# 3. Ghost Rider (Solo Film; protagonist motorcycle)
# 4. Avengers (No Speedster)
# 5. Justice League (Speedster)
# 6. Spiderman No Way Home (Solo Film; Willem Dafoe; Tobey Maguire)
# 7. The Amazing Spiderman (Solo Film; raging green monster antagonist)
# 8. The Incredible Hulk (Solo Film; raging green monster protagonist)
# 9. Wonder Woman (Solo Film)
# 10. Aquaman (Solo Film; Willem Dafoe)

def __checkIfConvertsToBool(variable: str) -> bool:
    """Checks if given variable can be converted to a bool and then returns a boolean"""
    if (variable == "Yes" or variable == "yes" or variable == "y" or variable == "Y"): # Check if variable is Yes/True or No/False and return 
        return True
    elif (variable == "No" or variable == "no" or variable == "n" or variable == "N"):
        return False
    else:
        print("Please type Yes or No as your answer\nTry Again") # Error handling
        return None

def __loopCheckConvertsToBool(question: str) -> bool:
    """Error Handling Function in addition to __CheckIfConvertsToBool, loops the request until user enters the correct response"""
    variable =__checkIfConvertsToBool(input(question))
    while variable == None:
        variable =__checkIfConvertsToBool(input(question))
    return variable

def setOfQuestionsSuperHero() -> bool:
    """Returns a list of answers as booleans from the user for Super Hero List"""
    # Define Variables
    soloSuperHeroMovie = False
    avengersOrJusticeLeague = False
    ragingGreenMonster = False
    antagonistOrProtagonist = False
    protagonistMotorcycle = False
    relyOnTech = False
    willemDafoe = False
    tobeyMaguire = False
    mainCharacterTobey = False

    # If Super Hero Film Questions
    soloSuperHeroMovie = __loopCheckConvertsToBool("Is the Film a solo Super Hero Movie? Yes/No ") # Eliminates Justice League and Avengers (Or narrows down to) (answerListSuperHero[1])
    
    # If is not a Solo Super Hero Film
    if not soloSuperHeroMovie:
        avengersOrJusticeLeague = __loopCheckConvertsToBool("Does the Film have a Speedster Super Hero? Yes/No ") # If does it's Justice League, If not Avengers (answerList[2])
    else: # If is a Solo Super Hero Film
        # Check if film has raging green Monster
        ragingGreenMonster = __loopCheckConvertsToBool("Does the Film have a raging Green Monster? Yes/No ") # if it does the film is either The Amazing Spiderman or the Incredible Hulk (answerList[3])
        # If has a raging Green Monster
        if ragingGreenMonster:
            antagonistOrProtagonist = __loopCheckConvertsToBool("Is the raging Green Monster the Protagonist? Yes/No ") # if it is the film is the Incredible Hulk, If not it's the Amazing Spiderman (answerList[4])
        else:
            # If protagonist drives a motorcycle
            protagonistMotorcycle = __loopCheckConvertsToBool("Does the protagonist drive a motorcycle? Yes/No ") # if protagonist does ride a motorcycle then film is either Dark Knight or Ghost Rider (answerList[5])
            # Determine if it's Ghost Rider or Batman
            if protagonistMotorcycle:
                relyOnTech = __loopCheckConvertsToBool("Does the protagonist rely on technology? Yes/No ") # If he does then it's Batman, otherwise it's Ghost Rider (answerList[6])
            else:
                # If the film stars Willem Dafoe
                willemDafoe = __loopCheckConvertsToBool("Is Willem Dafoe in the Film? Yes/No ") # If he is then it's either Spiderman (2002), Spiderman No Way Home, or Aquaman (answerList[7])
                # Determine if Tobey Maguire is in the film otherwise
                if willemDafoe:
                    tobeyMaguire = __loopCheckConvertsToBool("Is Tobey Maguire in the Film? Yes/No ") # If he is then it's either Spiderman (2002) or Spiderman No Way Home (answerList[8])
                    # If Tobey Maguire is in the film ask if he's the main character
                    if tobeyMaguire:    
                        mainCharacterTobey = __loopCheckConvertsToBool("Is Tobey Maguire the main character of the Film? Yes/No ") # If he is then the film is Spiderman (2002), if not then Spiderman No Way Home (answerList[9])
    answerListSuperHero = [soloSuperHeroMovie,avengersOrJusticeLeague,ragingGreenMonster,antagonistOrProtagonist,protagonistMotorcycle,relyOnTech,willemDafoe,tobeyMaguire,mainCharacterTobey]
    return answerListSuperHero

def superHeroFilmAlgorithm(answerListSuperHero: list):
    """Using information obtained in a function asking questions determine the movie in the super hero list"""
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

def setOfQuestionsSpaceOpera() -> None:
    """Asks a bunch of questions to determine which movie from the Space Opera list you're thinking of"""
    writtenByGeorgeLucas = __loopCheckConvertsToBool("Is the film written by George Lucas? Yes/No ") # Eliminates all Disney Star Wars films, and Dune
    # If it is written by George Lucas ask if he directed them
    if writtenByGeorgeLucas:
        directedByGeorgeLucas = __loopCheckConvertsToBool("Is the film directed by George Lucas? Yes/No ") # Determine if it's a prequel star wars film or an original 
        # if it is directed by George it's a prequel
        if directedByGeorgeLucas:
            jarJarBinksProminent = __loopCheckConvertsToBool("Is Jar Jar Binks a prominent character in this film? Yes/No ") 
            # If Jar Jar is prominent then it Phantom Menace otherwise Revenge of the Sith
            if jarJarBinksProminent:
                print('"Star Wars The Phantom Menace" is the film title.')
            else:
                # If not Jar Jar Prominent determine if Attack of the Clones or Revenge of the Sith
                tatooineProminent = __loopCheckConvertsToBool("Is Tatooine a prominent planet in this film? Yes/No ")
                if tatooineProminent: # If tatooine is prominent location of the film then AOTC or ANH otherwise ROTS
                    # Check Obi Wan actor to determine if AOTC or ANH
                    obiWanActor = __loopCheckConvertsToBool("Is Ewan McGregor Obi-Wan Kenobi in this film? Yes/No ")
                    if obiWanActor:
                        print('"Star Wars Attack of the Clones" is the film title.')
                    else:
                        print('"Star Wars A New Hope" is the film title.')
                else:
                    print('"Star Wars Revenge of The Sith" is the film title.')
        else:
            # If Luke has his real hand it's TESB if not its ROTJ
            lukesHand = __loopCheckConvertsToBool("Does Luke have his real hand in this film? Yes/No ")
            if lukesHand:
                print('"Star Wars The Empire Strikes Back" is the film title.')
            else:
                print('"Star Wars Return Of The Jedi" is the film title.')
    else:
        # If made by Disney then must be a Star Wars Sequel if not then the only other film it can be is Dune
        madeByDisney = __loopCheckConvertsToBool("Is the film made by Disney? Yes/No ")
        if madeByDisney:
            snokeInFilm = __loopCheckConvertsToBool("Is Supreme Leader Snoke in the film? Yes/No ")
            # If snoke is not in the film then it has to be ROS if he is it can be TFA or TLJ
            if snokeInFilm:
                directedByRianJohnson = __loopCheckConvertsToBool("Is the film directed by Rian Johnson? Yes/No ")
                # If directed by Rian Johnson then TLJ otherwise TFA
                if directedByRianJohnson:
                    print('"Star Wars The Last Jedi" is the film title.')
                else:
                    print('"Star Wars The Force Awakens" is the film title.')
            else:
                print('"Star Wars The Rise of Skywalker" is the film title.')
        else:
            print('"Dune" is the film title.')

def performAlgorithm(superHero: bool) -> str:    
    # Determine the Genre of the Film
    if superHero: # If Super Hero Film
        answerListSuperHero = setOfQuestionsSuperHero()
        superHeroFilmAlgorithm(answerListSuperHero)
    else: # If Space Opera
        setOfQuestionsSpaceOpera()

# Main

# Genre Question
subGenreFilmQuestion = __loopCheckConvertsToBool("Does the film take place on planet Earth? Yes/No ")
performAlgorithm(subGenreFilmQuestion)
