import pygame, random

def createPygameWindow() -> pygame.surface:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    pygame.init()
    window = pygame.display.set_mode((1280, 720))
    return window

def drawCheckerboard(window: pygame.surface, boardDimensions: tuple) -> tuple:
    """Draws the game board on to the window"""
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (192, 192, 192)
    darkGrey = (48, 48, 48)
    
    # Create board with grid lines
    board = pygame.Surface((960, 720))
    board.fill(darkGrey)

    (boardWidth, boardHeight) = board.get_size()

    horizontalSquareCount = boardDimensions[0]
    verticalSquareCount = boardDimensions[1]

    for i in range(1, horizontalSquareCount):
        pygame.draw.rect(board, grey, (0, -7 + i*(boardHeight/horizontalSquareCount), boardWidth, 4)) # Horizontal Lines
    for i in range(1, verticalSquareCount):
        pygame.draw.rect(board, grey, (-7 + i*(boardWidth/verticalSquareCount), 0, 4, boardHeight)) # Vertical Lines

    # Draw board
    window.blit(board, (0, 0))

    return (boardWidth, boardHeight)

def drawPlayerObject(window: pygame.surface, boardDimensions: tuple, boardDimensionsInPixels: tuple, playerCoords: tuple, player1: bool) -> None:
    darkGrey = (48, 48, 48, 255)
    red = (255, 0, 0)

    horizontalSquareCount = boardDimensions[0]
    verticalSquareCount = boardDimensions[1]
    
    if player1:
        xOffSet = 15
        yOffSet = 5
    else:
        xOffSet = 60
        yOffSet = 50

    # Create object            
    player = pygame.Surface((50, 50))
    player.fill(darkGrey)
    pygame.draw.circle(player, (random.randint(0, 255) if player1 else 0, 0, random.randint(0, 255) if not player1 else 0), (25, 25), 25)

    (x, y) = playerCoords

    # Draw objects
    window.blit(player, (xOffSet + (x*(boardDimensionsInPixels[0]/verticalSquareCount)), yOffSet + y*(boardDimensionsInPixels[1]/horizontalSquareCount)))

def playerMove(boardDimensions: tuple, playerCoords: tuple, diceRoll: int) -> tuple:
    """Moves the player on the board by the amount of the dice roll"""
    newYPos = playerCoords[1]
    newXPos = playerCoords[0]

    nextPos = playerCoords[0] + diceRoll
    if nextPos >= boardDimensions[0]:
        newYPos += 1
    
    newXPos = nextPos % boardDimensions[0]

    return (newXPos, newYPos)

def hasPlayerWon(boardDimensions: tuple, coords: tuple) -> bool:
    """Checks if a player has won"""
    # Win when new player coords >= (6,7)
    (boardX, boardY) = boardDimensions
    (playerX, playerY) = coords
    print("Board:", (boardX, boardY), "Player:", (playerX, playerY))
    if playerY >= boardY-1:
        print("Last Row (or Greater)")
        if playerX >= boardX-1 or playerY > boardY-1:
            print("Player Won")
            return True
    return False

def playerWonDraw(hasPlayerWon: bool, player):
    """Draws text on screen if a player has won"""
    if hasPlayerWon:
        pygame.font.init()
        myFont = pygame.font.SysFont('Comic Sans MS', 30)
        winStatement = myFont.render(f"Player {player} has won!!", False, (255,255,255))
        window.blit(winStatement, (961, 100))

def playerTurn(boardDimensions: tuple, playerCoords: tuple) -> tuple:
    """Initiates player one turn"""
    diceRole = diceRoll()
    newCoords = playerMove(boardDimensions, playerCoords, diceRole)
    playerWon = hasPlayerWon(boardDimensions, playerCoords)
    if playerWon:
        newCoords = (6, 5)

    return (diceRole, newCoords, playerWon)

def diceRoll() -> int:
    """Rolls a die"""
    diceRoll = random.randint(1,6)
    return diceRoll

def diceRollDrawCount(diceRoll: int, player1: bool) -> None:
    """Draw diceroll num on screen"""
    pygame.font.init()
    myFont = pygame.font.SysFont('Comic Sans MS', 30)
    diceRolePlayer = "Player 1" if player1 else "Player 2"
    diceRoleStr = "" if diceRoll == -1 else str(diceRoll)
    diceRollNumDraw = myFont.render(f"{diceRolePlayer} Dice Roll: {diceRoleStr}", False, (255,255,255))
    if player1:
        window.blit(diceRollNumDraw, (961, 0))
    else:
        window.blit(diceRollNumDraw, (961, 50))

# Main
window = createPygameWindow()
# clock = pygame.time.Clock()
# Program Loop
exit_flag = False # Set flag to false since we want the window to stay open
boardDimensions = (6, 7) # 42 squares

playerOneCoords = (0, 0)
playerTwoCoords = (0, 0)
playerWon = 0

diceRolePlayer1 = -1
diceRolePlayer2 = -1

grey = (69, 69, 69)

pygame.time.set_timer(pygame.USEREVENT, 3000)

while not exit_flag: # Loop through until flag is set to True
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit_flag = True # Set flag to true so program can terminate
        elif event.type == pygame.USEREVENT:
            # Player Wan goes
            (diceRolePlayer1, playerOneCoords, playerWonRound) = playerTurn(boardDimensions, playerOneCoords)
            # Check player Wan's Win (if win remove event)
            if playerWonRound:
                playerWon = 1
                pygame.time.set_timer(pygame.USEREVENT, 0)
            else:
                # Player Twoot goes
                (diceRolePlayer2, playerTwoCoords, playerWonRound) = playerTurn(boardDimensions, playerTwoCoords)               

                # Check Player Twoot's Win (if win remove event)
                if playerWonRound:
                    playerWon = 2
                    pygame.time.set_timer(pygame.USEREVENT, 0)


    # State Logic
    # playerTurn(boardDimensions, playerOneCoords)

    # Draw Screens
    window.fill(grey)
    boardDimensionsInPixels = drawCheckerboard(window, boardDimensions)
    drawPlayerObject(window, boardDimensions, boardDimensionsInPixels, playerOneCoords, True) # Player One
    drawPlayerObject(window, boardDimensions, boardDimensionsInPixels, playerTwoCoords, False) # Player Two
    diceRollDrawCount(diceRolePlayer1, True)
    diceRollDrawCount(diceRolePlayer2, False)
    playerWonDraw(playerWon > 0, playerWon)
    pygame.display.flip()
    # clock.tick(5)
pygame.quit()