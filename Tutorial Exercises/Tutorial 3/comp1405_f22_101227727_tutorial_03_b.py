def __checkIfConvertsToInt(variable: any) -> bool:
    """Checks if given variable can be converted to a int and then returns a boolean"""
    try: # Try converting to int if error return False if no error return True
        int(variable)
        return True
    except ValueError:
        return False

def printSelectionScreenText():
    """Prints the welcome screen and character choice"""
    print("Welcome to the world of FlyingLand!\nThere are many type of flying species that made it's way to FlyingLand.\n\nYou may:\n1. Be FlyingPiggys from the Pig Universe\n2. Be FlyingDonkeys from the Donkey Universe\n3. Be FlyingEwok from the Star Wars Galaxy - Planet Endor\n\nEnter 'q' at any point to quit")

def characterSelection() -> list:
    """Selects a character and then assigns the character and balance to a list, returns that list"""
    userCharacter = input("\n\nWhat is your choice? ")
    
    # Check if User wants to quit
    if userCharacter == 'q' or userCharacter == 'Q' or userCharacter == 'Quit' or userCharacter == 'QUIT':
        print("Goodbye!") # Print farewell
        exit(0)
    
    # If not quit command check if value can be converted to int and is 1,2,3
    while not __checkIfConvertsToInt(userCharacter) or (int(userCharacter) < 1 or int(userCharacter) > 3): # Error Handling
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

def itemSelection(money: int) -> int:
    """Asks the user what item they want and return that input as an integer"""
    # Ask user what they want to purchase
    userSelection = input("\nWhat do you want to purchase? ")

    # Check if User wants to quit
    if userSelection == 'q' or userSelection == 'Q' or userSelection == 'Quit' or userSelection == 'QUIT':
        print(f"You have ${money} left!\nThanks for your service!\nGoodbye!") # Print shop farewell
        exit(0)

    # If not quit command check if value can be converted to int and is 1,2,3
    while not __checkIfConvertsToInt(userSelection) or (int(userSelection) < 1 or int(userSelection) > 3): # Error Handling
        userSelection = input("\nInvalid Input: Enter 1, 2, or 3\nWhat do you want to purchase? ")
    else:
        userSelection = int(userSelection)
    return userSelection

def itemSelectionLogic(item: list, money: int, price: int, spent: int, userSelection) -> list:
    """Applies Store Logic given the passed through components"""
    # Check if the user selected passed in item
    if userSelection == item[0]:
        amount = input(f"How much {item[1]} would you like to buy? ")
        while not __checkIfConvertsToInt(amount) or (int(amount) < 0) or ((int(amount)*price) > money): # Error Handling - Can't buy negative product - can't spend more money than you have
            amount = input(f"\nInvalid Input or You can't spend money you don't have: Enter A positive number \nHow much {item[1]} would you like to buy? ")
        else:
            amount = int(amount)
        
        # Subtract the price from the money and add to spent
        money -= (price * amount)
        spent += (price * amount)
        moneyList = [money,spent,amount] # Put in a list so both values get returned
        return moneyList
    elif userSelection == 'q' or userSelection == 'Q' or userSelection == 'Quit' or userSelection == 'QUIT': # Check if user entered quit command
        print(f"You have ${money} left!\nThanks for your service!\nGoodbye!") # Print shop farewell
        exit(0)

def printShopScreen(characterInfo: list) -> None:
    # Amount of Money
    money = characterInfo[1]

    # Item Assigned as Number for selection
    # FlyingPiggys
    wing = [1, 'Wings']
    bacon = [2, 'Bacon']
    laserEye = [3, 'Laser Eyes']
    # FlyingDonkeys
    jetEngines = [1, 'Jet Engines']
    donkeyMilk = [2, 'Donkey Milk']
    miniNukes = [3, 'Mini Nukes']
    # FlyingEwok
    spaceShip = [1, 'Space Ships']
    youngling = [2, 'Younglings']
    lightSaber = [3, 'Lightsabers']
    
    # Item Prices
    # FlyingPiggys
    wingPrice = 1000
    baconPrice = 100
    laserEyePrice = 500
    # FlyingDonkeys
    jetEnginesPrice = 500
    donkeyMilkPrice = 50
    miniNukesPrice = 190
    # FlyingEwok
    spaceShipPrice = 1500
    younglingPrice = 200
    lightSaberPrice = 110 
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
    lightSaberSpent = 0
    # Assign Amount of items owned
    # FlyingPiggys
    wingsAmount = 0
    baconAmount = 0
    laserEyesAmount = 0
    # FlyingDonkeys
    jetEnginesAmount = 0
    donkeyMilkAmount = 0
    miniNukesAmount = 0
    # FlyingEwok
    spaceShipAmount = 0
    younglingAmount = 0
    lightSaberAmount = 0


    # Print FlyingPiggy layout and perform logic
    if characterInfo[0] == 'FlyingPiggys':
        while money > 0:
            print(f"\nPig Item Shop!!\n1. Wing: Cost: ${wingPrice}   Amount Spent: ${wingsSpent}    Owned: {wingsAmount}\n2. Bacon:  Cost: ${baconPrice}   Amount Spent: ${baconSpent}  Owned: {baconAmount}\n3. Laser Eye: Cost: ${laserEyePrice}   Amount Spent: ${laserEyesSpent}    Owned: {laserEyesAmount}\nYou have ${money} left!")
            userSelection = itemSelection(money) # Ask the user what item they want to buy
            
            # Run the algorithm and store the returned list in a variable
            if userSelection == wing[0]: newBal_amountSpent = itemSelectionLogic(wing, money, wingPrice, wingsSpent,userSelection)
            if userSelection == bacon[0]: newBal_amountSpent = itemSelectionLogic(bacon, money, baconPrice, baconSpent,userSelection)
            if userSelection == laserEye[0]: newBal_amountSpent = itemSelectionLogic(laserEye, money, laserEyePrice, laserEyesSpent,userSelection)
            money = newBal_amountSpent[0] # Update the amount of money the user has
            
            # Increment the amount spent variables
            if userSelection == wing[0]: wingsSpent += newBal_amountSpent[1]
            if userSelection == bacon[0]: baconSpent += newBal_amountSpent[1]
            if userSelection == laserEye[0]: laserEyesSpent += newBal_amountSpent[1]

            # Increment the amount owned variables
            if userSelection == wing[0]: wingsAmount += newBal_amountSpent[2]
            if userSelection == bacon[0]: baconAmount += newBal_amountSpent[2]
            if userSelection == laserEye[0]: laserEyesAmount += newBal_amountSpent[2]
        # Print your stats when out of money
        print(f"\nYour stats:\n1. Wing: Cost: ${wingPrice}   Amount Spent: ${wingsSpent}    Owned: {wingsAmount}\n2. Bacon:  Cost: ${baconPrice}   Amount Spent: ${baconSpent}  Owned: {baconAmount}\n3. Laser Eye: Cost: ${laserEyePrice}   Amount Spent: ${laserEyesSpent}    Owned: {laserEyesAmount}\nYou have ${money} left!")

    # Print FlyingDonkeys layout and perform logic
    if characterInfo[0] == 'FlyingDonkeys':
        while money > 0:
            print(f"\nDonkey Item Shop!!\n1. Jet Engine: Cost: ${jetEnginesPrice}   Amount Spent: ${jetEnginesSpent}    Owned: {jetEnginesAmount}\n2. Donkey Milk:  Cost: ${donkeyMilkPrice}   Amount Spent: ${donkeyMilkSpent} Owned: {donkeyMilkAmount}\n3. Mini Nuke: Cost: ${miniNukesPrice}   Amount Spent: ${miniNukesSpent}  Owned: {miniNukesAmount}\nYou have ${money} left!")
            userSelection = itemSelection(money) # Ask the user what item they want to buy
            
            # Run the algorithm and store the returned list in a variable
            if userSelection == jetEngines[0]: newBal_amountSpent = itemSelectionLogic(jetEngines, money, jetEnginesPrice, jetEnginesSpent,userSelection)
            if userSelection == donkeyMilk[0]: newBal_amountSpent = itemSelectionLogic(donkeyMilk, money, donkeyMilkPrice, donkeyMilkSpent,userSelection)
            if userSelection == miniNukes[0]: newBal_amountSpent = itemSelectionLogic(miniNukes, money, miniNukesPrice, miniNukesSpent,userSelection)
            money = newBal_amountSpent[0] # Update the amount of money the user has
            
            # Increment the amount spent variables
            if userSelection == jetEngines[0]: jetEnginesSpent += newBal_amountSpent[1]
            if userSelection == donkeyMilk[0]: donkeyMilkSpent += newBal_amountSpent[1]
            if userSelection == miniNukes[0]: miniNukesSpent += newBal_amountSpent[1]

            # Increment the amount owned variables
            if userSelection == jetEngines[0]: jetEnginesAmount += newBal_amountSpent[2]
            if userSelection == donkeyMilk[0]: donkeyMilkAmount += newBal_amountSpent[2]
            if userSelection == miniNukes[0]: miniNukesAmount += newBal_amountSpent[2]
        # Print your stats when out of money
        print(f"\nYour stats:\n1. Jet Engine: Cost: ${jetEnginesPrice}   Amount Spent: ${jetEnginesSpent}    Owned: {jetEnginesAmount}\n2. Donkey Milk:  Cost: ${donkeyMilkPrice}   Amount Spent: ${donkeyMilkSpent} Owned: {donkeyMilkAmount}\n3. Mini Nuke: Cost: ${miniNukesPrice}   Amount Spent: ${miniNukesSpent}  Owned: {miniNukesAmount}\nYou have ${money} left!")

    # Print FlyingEwok layout and perform logic
    if characterInfo[0] == 'FlyingEwok':
        while money > 0:
            print(f"\nEwok Item Shop!!\n1. Space Ship: Cost: ${spaceShipPrice}   Amount Spent: ${spaceShipSpent}    Owned: {spaceShipAmount}\n2. Youngling:  Cost: ${younglingPrice}   Amount Spent: ${younglingSpent}   Owned: {younglingAmount}\n3. Lightsaber: Cost: ${lightSaberPrice}   Amount Spent: ${lightSaberSpent}   Owned: {lightSaberAmount}\nYou have ${money} left!")
            userSelection = itemSelection(money) # Ask the user what item they want to buy
            
            # Run the algorithm and store the returned list in a variable
            if userSelection == spaceShip[0]: newBal_amountSpent = itemSelectionLogic(spaceShip, money, spaceShipPrice, spaceShipSpent,userSelection)
            if userSelection == youngling[0]: newBal_amountSpent = itemSelectionLogic(youngling, money, younglingPrice, younglingSpent,userSelection)
            if userSelection == lightSaber[0]: newBal_amountSpent = itemSelectionLogic(lightSaber, money, lightSaberPrice, lightSaberSpent,userSelection)
            money = newBal_amountSpent[0] # Update the amount of money the user has
            
            # Increment the amount spent variables
            if userSelection == spaceShip[0]: spaceShipSpent += newBal_amountSpent[1]
            if userSelection == youngling[0]: younglingSpent += newBal_amountSpent[1]
            if userSelection == lightSaber[0]: lightSaberSpent += newBal_amountSpent[1]

            # Increment the amount spent variables
            if userSelection == spaceShip[0]: spaceShipAmount += newBal_amountSpent[2]
            if userSelection == youngling[0]: younglingAmount += newBal_amountSpent[2]
            if userSelection == lightSaber[0]: lightSaberAmount += newBal_amountSpent[2]
        # Print your stats when out of money
        print(f"\nYour stats:\n1. Space Ship: Cost: ${spaceShipPrice}   Amount Spent: ${spaceShipSpent}    Owned: {spaceShipAmount}\n2. Youngling:  Cost: ${younglingPrice}   Amount Spent: ${younglingSpent}   Owned: {younglingAmount}\n3. Lightsaber: Cost: ${lightSaberPrice}   Amount Spent: ${lightSaberSpent}   Owned: {lightSaberAmount}\nYou have ${money} left!")
    print("\nYou have spent all your Money!\nThanks for your service!\nGoodbye!") # Print a statement when out of money

# Main
printSelectionScreenText()
characterInfo = characterSelection()
printShopScreen(characterInfo)