

import pygame

pygame.init()

# create game window
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# define colours
bg = (255, 200, 150)
body_inner = (50, 175, 25)
body_outer = (100, 100, 200)
RED = (255, 0, 0)

# define game variables
cell_size = 10

# create snake
snake_pos = [[SCREEN_WIDTH//2, SCREEN_HEIGHT//2]] # use list so its easier to add (append) more
snake_pos.append([SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + cell_size])
snake_pos.append([SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + cell_size *2])
snake_pos.append([SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + cell_size*3])


def draw_screen():
    screen.fill(bg)


# loop with exit event handler
run = True
while run:
    draw_screen()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw snake
    head = 1
    for x in snake_pos:
        if head == 0:

            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, body_outer, (x[0]+1, x[1]+1, cell_size - 2, cell_size-2))
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(screen, RED, (x[0]+1, x[1]+1, cell_size - 2, cell_size-2))
            head = 0
    # update the display
    pygame.display.update()
    