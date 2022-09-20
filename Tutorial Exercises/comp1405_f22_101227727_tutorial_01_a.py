# Imports
import pygame
import math

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
    backgroundColour = (158,59,40) # Red RGB 
    outerRightSemiCircleColour = (76,131,187) # Blue RGB
    innerRightSemiCircleColour = (214,174,77) # Yellow RGB
    outerLeftSemiCircleColour = (223, 212, 206) # Light Grey RGB
    innerLeftSemiCircleColour = (29, 29, 29) # Black RBG
    middleSemiCircleColour = (213,136,116) # Peach RGB

    # Draw!
    surface.fill(backgroundColour) # Set background colour to Red
    pygame.draw.rect(surface, outerLeftSemiCircleColour,pygame.Rect(69, 69, 162, 162)) # Draw Rectangle

    pygame.draw.arc(surface,outerRightSemiCircleColour, pygame.Rect(69, 69, 162, 162), -math.pi/2, -(3*math.pi)/2 , 27) # Draw the first semi circle
    pygame.display.flip() # Update the display so the drawn images show

def saveFrameAsImage(surface: pygame.surface, fileName) -> None:
    """When called, the current frame will be saved"""
    pygame.image.save(surface, fileName)

# Main

imageFileName = 'assigned_image_for_101227727.png' # Set variable as string for image file name
# Draw Image
window = createPygameWindow(300,300) # Make a 300 by 300 pygame window
# Create image while keeping the window open and close if the X button is clicked
while True: # Loop through infinently
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            #saveFrameAsImage(window, imageFileName) # Save the last frame as image (In this case only frame)
            pygame.quit()
            exit(0) # Removes text dump from the shell
        drawMyAssignedImage(window)

