# Imports
import pygame

# Functions
def createPygameWindow(x: int, y: int) -> pygame.surface:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    window = pygame.display.set_mode(size=(x,y))
    return window

def drawMyAssignedImage(surface: pygame.surface) -> None:
    """Draws a image to the pygame window"""
backgroundColour = (255,255,255) # White RGB 
circleColour = (255,0,0) # Red RGB
blue = (0,0,255)

# Draw!
surface.fill(backgroundColour) # Set background colour to white
for i in range(4, 10, 2):
    for j in range(2, 10, 4):
        pygame.draw.circle(i,j,255,0,0)

for i in range(1, 9, 2):
    for j in range(2, 11, 3):
        pygame.draw.star(i,j,0,0,255 )

pygame.display.flip() # Update the display so the drawn images show


# Main
# Draw Image
window = createPygameWindow(750,750) # Make a 750 by 750 window
# Create image while keeping the window open and close if the X button is clicked
while True: # Loop through infinently
  drawMyAssignedImage(window)

