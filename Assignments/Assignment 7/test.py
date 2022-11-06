import pygame

# --- constants --- (UPPER_CASE names)

SCREEN_WIDTH = 430
SCREEN_HEIGHT = 410

#BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30

# --- classses --- (CamelCase names)

# empty

# --- functions --- (lower_case names)

# empty

# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen_rect = screen.get_rect()

pygame.display.set_caption("Tracking System")

# - objects -

# rectangle = pygame.rect.Rect(0, 0, 0, 0)
rectangle_draging = False

# - mainloop -

clock = pygame.time.Clock()

running = True

initialMousePosition = (0,0)
newMousePosition = (0,0)
rectangle = None 


def functionWithCoolName(initial, newPosition):
    rectangle = pygame.rect.Rect(
        min(initial[0], newPosition[0]), 
        min(initial[1], newPosition[1]), 
        abs(newPosition[0]-initial[0]), 
        abs(newPosition[1]-initial[1])
    )

    return rectangle


while running:

    # - events -
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                rectangle_draging = True
                initialMousePosition = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                newMousePosition = event.pos
                rectangle = functionWithCoolName(initialMousePosition, newMousePosition)
                

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    if(rectangle):
        pygame.draw.rect(screen, RED, rectangle)

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()