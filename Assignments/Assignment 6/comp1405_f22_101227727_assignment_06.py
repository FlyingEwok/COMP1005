import pygame

def drawCheckerboard():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))

    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (192, 192, 192)
    dark_grey = (48, 48, 48)
    red = (255, 0, 0)

    # Create board with gridlines
    board = pygame.Surface((430, 430))
    board.fill(dark_grey)
    for i in range(1, 4):
        pygame.draw.rect(board, grey, (0, -7 + i*110, 430, 4))
        pygame.draw.rect(board, grey, (-7 + i*110, 0, 4, 430))

    # Create object
    object1 = pygame.Surface((100, 100))
    object1.fill(dark_grey)
    pygame.draw.circle(object1, red, (50, 50), 50)

    x, y = (0, 0)
    done = False
    clock = pygame.time.Clock()

    while not done:

        # Clear the screen
        screen.fill(black)

        # Draw board
        screen.blit(board, (105, 20))

        # Draw objects
        screen.blit(object1, (105 + x*110, 20 + y*110))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x = (x - 1) % 4
                if event.key == pygame.K_RIGHT:
                    x = (x + 1) % 4
                if event.key == pygame.K_UP:
                    y = (y - 1) % 4
                if event.key == pygame.K_DOWN:
                    y = (y + 1) % 4

        # Update the screen
        clock.tick()
        pygame.display.flip()

while True:
    drawCheckerboard()