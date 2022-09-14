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
    rectColour = (82,144,60) # Green
    pygame.draw.rect(surface, rectColour, pygame.Rect(328, 111, 74, 316))
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
            exit(0) # Removes text dumb to the shell
        drawMyAssignedImage(window)
