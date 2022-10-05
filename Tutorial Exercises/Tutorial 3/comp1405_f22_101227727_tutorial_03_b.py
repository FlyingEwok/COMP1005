def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def printSelectionScreenText():
    """Prints the welcome screen and character choice"""
    print("Welcome to the world of FlyingLand!\nThere are many type of flying species that made it's way to FlyingLand.\n\nYou may:\n1. Be FlyingPiggys from the Pig Universe\n2. Be FlyingDonkeys from the Donkey Universe\n3. Be FlyingEwok from the Star Wars Galaxy - Planet Endor")

def characterSelection() -> list:
    """Selects a character and then assigns the character and balance to a list, returns that list"""
    userCharacter = input("\n\nWhat is your choice? ")
    while not __checkIfConvertsToInt(userCharacter): # Error Handling
        userCharacter = input("\nInvalid Input: Enter 1, 2, or 3\nWhat is your choice? ")
    else:
        userCharacter = int(userCharacter)
    
    # Character to number assignment
    FlyingPiggys = 1
    FlyingDonkeys = 2
    FlyingEwok = 3

    # Print selection and assign balance
    if userCharacter == FlyingPiggys:
        balance = 2000
        print(f"\nYou Have Selected FlyingPiggys and you have a starting balance of ${balance}")
        infoList = ['FlyingPiggys',balance]
    elif userCharacter == FlyingDonkeys:
        balance= 1500
        print(f"\nYou Have Selected FlyingDonkeys and you have a starting balance of ${balance}")
        infoList = ['FlyingDonkeys',balance]
    elif userCharacter == FlyingEwok:
        balance = 2250
        print(f"\nYou Have Selected FlyingEwok and you have a starting balance of ${balance}")
        infoList = ['FlyingEwok',balance]
    
    return infoList

def printShopScreen(characterInfo: list) -> None:
    # Amount of Money
    money = characterInfo[1]
    # Item Prices
    # FlyingPiggys
    wing = 1000
    bacon = 100
    laserEye = 500
    # FlyingDonkeys
    jetEngines = 500
    donkeyMilk = 50
    miniNukes = 190
    # FlyingEwok
    spaceShip = 1500
    youngling = 200
    lightSaber = 110 
    # Assign Amount spent on items
    # FlyingPiggys
    wingsSpent = 0
    baconSpent = 0
    laserEyesSpent = 0
    # FlyingDonkeys
    jetEnginesSpent = 0
    donkeyMilkSpent = 0
    miniNukesSpent = 0
    # FlyingEwok
    spaceShipSpent = 0
    younglingSpent = 0
    lightSaber = 0


    # Print FlyingPiggy layout
    if characterInfo[0] == 'FlyingPiggys':
        while True:
            print(f"\nPig Item Shop!!\n1. Wing: Cost: ${wing}   Amount Spent: ${wingsSpent}\n2. Bacon:  Cost: ${bacon}   Amount Spent: ${baconSpent}\n3. Laser Eye: Cost: ${laserEye}   Amount Spent: ${laserEyesSpent}")
            


printSelectionScreenText()
characterInfo = characterSelection()
printShopScreen(characterInfo)