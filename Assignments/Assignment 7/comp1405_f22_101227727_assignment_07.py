import pygame, sys

def saveFrameAsImage(surface: pygame.surface, fileName) -> None:
    """When called, the current frame will be saved"""
    pygame.image.save(surface, fileName)

def createPygameWindow(srcImg: pygame.surface) -> pygame.surface:
    """Takes in dimensions and creates a pygame window"""
    # Intialize pygame
    pygame.display.init()
    # Create Window
    (x,y) = srcImg.get_size()
    window = pygame.display.set_mode(size=(x,y))

    return window

def displayImg(window: pygame.surface, srcImg: pygame.surface) -> None:
    """Blits the loaded image to the screen"""
    window.blit(srcImg, (0,0))

def calculateRect(initial: tuple, newPosition: tuple):
    """The math behind drawing the rectangle with mouse cursor while dragging"""
    rectangle = pygame.rect.Rect(
        min(initial[0], newPosition[0]), 
        min(initial[1], newPosition[1]), 
        abs(newPosition[0]-initial[0]), 
        abs(newPosition[1]-initial[1])
    )

    return rectangle

def selectPositionOnScreen(event, rectangle: pygame.rect.Rect, rectangleDragging: bool, initialMousePosition: tuple, newMousePosition: tuple):
    """Selects the position on the screen by drawing a rectangle"""
    coordToNegate = None # Define variable
    
    # Selection tool code
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:            
            rectangleDragging = True
            initialMousePosition = event.pos

    elif event.type == pygame.MOUSEBUTTONUP:
        if event.button == 1:        
            rectangleDragging = False
            # Grab the rectangles position
            if rectangle:
                (x, y, w, h) = rectangle
                coordToNegate = (x, y, w, h)
                rectangle = None # Delete the rectangle
                print(coordToNegate)

    elif event.type == pygame.MOUSEMOTION:
        if rectangleDragging:
            newMousePosition = event.pos
            rectangle = calculateRect(initialMousePosition, newMousePosition)
    return rectangle, rectangleDragging, initialMousePosition, newMousePosition, coordToNegate

def drawSelectionRectangle(window: pygame.surface, rectangle: pygame.rect.Rect) -> None:
    """Draws the rectangle on the screen"""
    # Draw Rectangle
    if rectangle:
        surface = pygame.Surface(window.get_size())
        surface.set_alpha(128)
        surface.fill((0,0,0))
        pygame.draw.rect(surface, RED, rectangle)
        window.blit(surface, (0,0))
    

def negateImage(window: pygame.surface, srcImg: pygame.surface, coordToNegate: tuple) -> None:
    """Inverts a selected portion of background given the coordinates"""
    # THIS IS THE BETTER SOLUTION BUT REQUIRED TO USE NESTED LOOPS FOR THIS ASSIGNMENT!
    # negativeImageSurface = pygame.Surface((coordToNegate[2], coordToNegate[3])) # Makes surface size of rectangle
    # negativeImageSurface.fill((255, 255, 255)) 
    # negativeImageSurface.blit(window, (0, 0), coordToNegate, special_flags=pygame.BLEND_SUB) # Crops background and inverts it

    # window.blit(negativeImageSurface, (coordToNegate[0], coordToNegate[1])) # Blits on to the screen
    

    # Loops through pixel by pixel and inverts the area selected
    for y in range(coordToNegate[1], coordToNegate[1] + coordToNegate[3]):
        for x in range(coordToNegate[0], coordToNegate[0] + coordToNegate[2]):
            colour = window.get_at((x, y))
            window.set_at((x, y), (255 - colour[0], 255 - colour[1], 255 - colour[2], 255))


# Main
# Variables 
srcImg = pygame.image.load(sys.argv[1])
window = createPygameWindow(srcImg)

initialMousePosition = (0,0)
newMousePosition = (0,0)
selectionRectangle = None
rectangleDragging = False

temp = []
temp2 = []

# RGB Values
RED = pygame.Color(255,0,0)

# Program Loop
exit_flag = False # Set flag to false since we want the window to stay open

while not exit_flag: # Loop through until flag is set to True
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit_flag = True # Set flag to true so program can terminate
        
        selectionRectangle, rectangleDragging, initialMousePosition, newMousePosition, coordToNegate  = selectPositionOnScreen(event, selectionRectangle, rectangleDragging, initialMousePosition, newMousePosition) # Select the position on the screen

        
    # Blit image to background
    displayImg(window, srcImg)
    drawSelectionRectangle(window, selectionRectangle)
    if not selectionRectangle: 
        if coordToNegate != None:
            temp.append(coordToNegate)
            print("appending", coordToNegate)
            coordToNegate = None
        # Allow for multiple selections
        for coord in temp:
            negateImage(window, srcImg, coord)
    pygame.display.flip()

pygame.quit()








