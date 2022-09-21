# Imports
import pygame
from math import pi

# Functions
def createPygameWindow(x: int, y: int) -> pygame.surface:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    window = pygame.display.set_mode(size=(x,y))
    return window

# Exercise B Functions
def drawImage(surface: pygame.surface) -> None:
    """Draws a image to the pygame window"""
    # Variables
    backgroundColour = (255,255,255) # White RGB 
    bodyColour = (25,128,66) # Green RGB
    mouthColour = (255,0,0) # Red RGB
    eyeColour = (255,0,255) # Magenta RGB
    propColour = (156, 170, 160) # Green Beige 
    bodyPolygonVerticies = [(90,125), (150,220), (211,125)]
    propPolygonVerticies = [(200,70),(231,20),(250,70)]

    # Draw!
    surface.fill(backgroundColour) # Set background colour to white
    pygame.draw.circle(surface, bodyColour, (150, 50), 40) # Draw head
    pygame.draw.arc(surface, bodyColour, pygame.Rect(90, 110, 120, 30), 0, -pi, 9999) # Top of body
    pygame.draw.polygon(surface, bodyColour, bodyPolygonVerticies) # Body
    pygame.draw.arc(surface,bodyColour,pygame.Rect(115, 200, 41, 120), pi/2, -pi, 5) # Left Leg
    pygame.draw.arc(surface,bodyColour,pygame.Rect(145, 200, 41, 120), 0, pi/2, 5) # Right Leg
    pygame.draw.arc(surface,bodyColour,pygame.Rect(65, 10, 41, 120), (2*pi)/3, (3*pi)/2, 5) # Left Arm
    pygame.draw.arc(surface,bodyColour,pygame.Rect(195, 10, 41, 120), (3*pi)/2, 0, 5) # Right Arm
    #pygame.draw.rect(surface, eyeColour, pygame.Rect(115, 60, 41, 20))
    pygame.draw.arc(surface, mouthColour, pygame.Rect(115, 60, 41, 20), (7*pi)/4, (3*pi)/2, 3) # Mouth
    pygame.draw.circle(surface, eyeColour, (130,40), 10) # Eye
    pygame.draw.polygon(surface,propColour,propPolygonVerticies) # Prop
    pygame.draw.circle(surface, eyeColour, (231,50), 6) # Prop Eye

    pygame.display.flip() # Update the display so the drawn images show

def runExerciseB() -> None:
    """Executes a series of code to run the program"""
    # Draw Image
    window = createPygameWindow(300,300) # Make a 300 by 300 pygame window
    # Create image while keeping the window open and close if the X button is clicked
    while True: # Loop through infinitely
        # Constantly check if x button is clicked
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0) # Removes text dump from the shell
            drawImage(window)
# Main
runExerciseB()


