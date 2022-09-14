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
    rectColour = (82,144,60) # Green RGB
    polygonColour = (131, 117, 175) # Purple RGB

    # Put the polygon verticies into a list
    polygonVerticies = [(320,106), (240,106), (321,0), (400,106), (400, 213)]

    # Draw!
    surface.fill(backgroundColour) # Set background colour to white
    pygame.draw.rect(surface, rectColour, pygame.Rect(320, 106, 81, 321)) # Draw Rectangle
    pygame.draw.polygon(surface, polygonColour, polygonVerticies) # Draw the polygon
    pygame.display.flip() # Update the display so the drawn images show

def saveFrameAsImage(surface: pygame.surface, fileName) -> None:
    """When called, the current frame will be saved"""
    pygame.image.save(surface, fileName)

# Main

imageFileName = 'assigned_image_for_101227727.png' # Set variable as string for image file name
# Draw Image
window = createPygameWindow(480,640) # Make a 480 by 640 window
# Create image while keeping the window open and close if the X button is clicked
while True: # Loop through infinently
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            saveFrameAsImage(window, imageFileName) # Save the last frame as image (In this case only frame)
            pygame.quit()
            exit(0) # Removes text dump from the shell
        drawMyAssignedImage(window)

