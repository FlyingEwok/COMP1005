# Nicholas Garth 101227727
import pygame
from math import pi

def createPygameWindow(x: int, y: int) -> pygame.surface:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    win_sfc = pygame.display.set_mode(size=(x,y))
    return win_sfc

def drawCircleOfFace(win_sfc: pygame.surface) -> tuple:
    """Draws the circle the face will be drawn on"""
    YELLOW = (255,204,0)
    BLACK = (0,0,0)
    circlePos = (((pygame.Surface.get_width(win_sfc))/2), ((pygame.Surface.get_height(win_sfc)))/2)

    pygame.draw.circle(win_sfc, BLACK, circlePos, 102) # Draw border
    pygame.draw.circle(win_sfc, YELLOW, circlePos, 100)

    return circlePos

def draw_eyes() -> None:
    """Draws a pair of eyes on to the screen, given the circles centre is (150,250) and the circle radius is 100"""
    BLACK = (0,0,0)
    WHITE = (255,255,255)

    circleCentreCoords = (150,250)

    # Eye Position
    leftEyePos = (circleCentreCoords[0]-35,circleCentreCoords[1]-35) #((((pygame.Surface.get_width(win_sfc))/2) - 35),(((pygame.Surface.get_height(win_sfc))/2) - 35))
    rightEyePos = (circleCentreCoords[0]+35,circleCentreCoords[1]-35) #((((pygame.Surface.get_width(win_sfc))/2) + 35),(((pygame.Surface.get_height(win_sfc))/2) - 35))

    # Eye pupil position
    leftEyePupilPos = ((leftEyePos[0] - 5), (leftEyePos[1] - 5))
    rightEyePupilPos = ((rightEyePos[0] - 5), (rightEyePos[1] - 5))

    # Draw Eye Border
    pygame.draw.circle(win_sfc, BLACK, leftEyePos, 22)
    pygame.draw.circle(win_sfc, BLACK, rightEyePos, 22)

    # Draw Eyes
    pygame.draw.circle(win_sfc, WHITE, leftEyePos, 20)
    pygame.draw.circle(win_sfc, WHITE, rightEyePos, 20)

    # Draw Eye Detail
    pygame.draw.circle(win_sfc,BLACK, leftEyePupilPos, 5)
    pygame.draw.circle(win_sfc, BLACK, rightEyePupilPos, 5)

def draw_hat() -> str:
    """Draws a hat on the screen, given the circles centre is (250,350) and the circle radius is 100"""
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED = (255,0,0)

    circleCentreCoords = (250,350)

    # Middle Top of head coords
    leftTopOfHead = (circleCentreCoords[0] - 100) #(((pygame.Surface.get_width(win_sfc))/2) - 100)
    topOfBottomOfHat = (circleCentreCoords[1]-120) #(((pygame.Surface.get_height(win_sfc))/2) - 120)

    # Draw Top Hat
    pygame.draw.rect(win_sfc, BLACK, pygame.Rect(leftTopOfHead-2,topOfBottomOfHat-2, 200+4, 20+4)) # Bottom of hat
    pygame.draw.rect(win_sfc, WHITE, pygame.Rect(leftTopOfHead,topOfBottomOfHat, 200, 20)) # Bottom of hat
    pygame.draw.rect(win_sfc, BLACK, pygame.Rect((leftTopOfHead + 48), topOfBottomOfHat-122, 100+4, 120)) # Top hat
    pygame.draw.rect(win_sfc, RED, pygame.Rect((leftTopOfHead + 50), topOfBottomOfHat-120, 100, 120)) # Top hat

    description = "top hat"
    return description

def draw_mouth(x: int, y: int) -> None:
    """Draws a mouth given the circle centre passed in, and that circle has a 100 radius"""
    BLACK = (0,0,0)
    RED = (255,0,0)
    WHITE = (255,255,255)
    
    # Draw Mouth
    pygame.draw.rect(win_sfc, BLACK, pygame.Rect((x-60), y, 110, 2)) # Top Lip
    pygame.draw.arc(win_sfc, RED, pygame.Rect((x-58), y-48, 108, 98), pi, 0, 9999) # Inside Mouth
    pygame.draw.arc(win_sfc, BLACK, pygame.Rect((x-60), y-50, 110, 100), pi, 0, 2) # Bottom Lip
    pygame.draw.rect(win_sfc, WHITE, pygame.Rect((x-20), y+1, 20, 25)) # Tooth



 
# Main
win_sfc = createPygameWindow(480,480)
# Program Loop
exit_flag = False # Set flag to false since we want the window to stay open

while not exit_flag: # Loop through until flag is set to True
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            #saveFrameAsImage(window, imageFileName) # Save the last frame as image (In this case only frame)
            exit_flag = True # Set flag to true so program can terminate
    win_sfc.fill((255,255,255)) # Fill background with white
    
    # TEST CASES
    #circleCentreCoord = drawCircleOfFace(win_sfc) # Grabs the centre of the test circle, as well as draws to the screen
    #draw_eyes()
    #draw_hat()
    #draw_mouth(circleCentreCoord[0],circleCentreCoord[1])  # Needs circleCentreCoords

    pygame.display.flip()