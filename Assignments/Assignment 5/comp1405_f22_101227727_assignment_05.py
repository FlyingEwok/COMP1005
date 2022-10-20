# Nicholas Garth 101227727
import pygame, random, sys

def saveFrameAsImage(surface: pygame.surface, fileName) -> None:
    """When called, the current frame will be saved"""
    pygame.image.save(surface, fileName)

def drawPointillism(window: pygame.surface, srcImg, width: int, height: int, scaleFactor: int) -> None:
    # RGB values
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    
    # Iterate through rows and columns of the pixels
    for i in range(height):
        for j in range(width):
            (r, g, b, _) = srcImg.get_at((j, i))
            luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) * 255
            
            # Feel free to play around with these values :)
            thresholdFactor = 128 # The threshold for the pixel in the image to draw a circle with
            pixelAlignment = -10 # The pixel alignment value (0 here will have pixel perfect placement, any other negative value will be more random looking)

            # Calculate required amount of circle
            redAmt = int(r/thresholdFactor)
            greenAmt = int(g/thresholdFactor)
            blueAmt = int(b/thresholdFactor)

            # Draws a random Red, Green, or Blue circle
            if luminance > 0.625:
                colours = [red for _ in range(redAmt)] + [green for _ in range(greenAmt)] + [blue for _ in range(blueAmt)]
                random.shuffle(colours)
                for colour in colours:
                    pygame.draw.circle(window, colour, (random.randint((j*scaleFactor)+pixelAlignment,(j*scaleFactor)),random.randint((i*scaleFactor)+pixelAlignment,(i*scaleFactor))), 1)

def configurePygame() -> pygame.surface:
    """Creates pygame window and applies pointillism to pygame window, returns the window (surface)"""
    pygame.display.init()

    # Import Image
    srcImg = pygame.image.load(sys.argv[1])


    
    # Feel free to play with these values as well :)
    scaleFactor = 4 # The factor to scale the pointillism up to! (If your image is big then you may not want this factor to be any higher than 1, but for the requirements of the assignment it has to be 4)
    sourceImagetestScaleFactor = 1 # The factor to scale the image down by (Change this if your image is too big)
    
    # Window Sizing
    (wid, hgt) = srcImg.get_size()
    srcImg = pygame.transform.scale(srcImg, (wid/sourceImagetestScaleFactor, hgt/sourceImagetestScaleFactor)) # Scale the image down by a factor
    (wid, hgt) = srcImg.get_size()
    window = pygame.display.set_mode((wid*scaleFactor, hgt*scaleFactor))
    
    # Draws the pointillism
    drawPointillism(window, srcImg,  wid, hgt, scaleFactor)

    #Update the display to show what has just been drawn
    pygame.display.update()
    return window

# Main
screen = configurePygame()
imageFileName = 'art.png' # Set variable as string for image file name
# Draw Image
# Create image while keeping the window open and close if the X button is clicked
while True: # Loop through infinitely
    # Constantly check if x button is clicked
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            saveFrameAsImage(screen, imageFileName) # Save the last frame as image (In this case only frame)
            pygame.quit()
            exit(0) # Removes text dump from the shell