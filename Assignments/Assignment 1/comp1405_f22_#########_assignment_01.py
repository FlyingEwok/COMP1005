from cmath import rect
import pygame
from sympy import true

def createPygameWindow(x: int, y: int) -> rect:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    window = pygame.display.set_mode(size=(x,y))
    return window
def drawMyAssignedImage(surface):
    """Draws a image to the pygame window"""
    backGroundColour = (255,255,255) # White RGB 
    rectColour = (82,144,60) # Green RGB
    polygonColour = (131, 117, 175)

    polygonVerticies = [(320,106), (240,106), (321,0), (400,106), (400, 213)]

    surface.fill(backGroundColour) # Set background colour to white
    pygame.draw.rect(surface, rectColour, pygame.Rect(320, 106, 81, 321)) # Draw Rectangle
    pygame.draw.polygon(surface, polygonColour, polygonVerticies)
    pygame.display.flip()

# Main

# Draw Image
window = createPygameWindow(480,640) # Make a 480 by 640 window
# Create image while keeping the window open and close if the X button is clicked
while true: # Loop through infinently
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0) # Removes text dump from the shell
        drawMyAssignedImage(window)
