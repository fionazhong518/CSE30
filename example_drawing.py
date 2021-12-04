'''

'''
import pygame
from pygame.version import PygameVersion

# Initialize the game engine
pygame.init()

# ------ setup ------- #
# Define colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

# setup screen
SIZE = [700, 500]
screen = pygame.display.set_mode(SIZE)

# setup DONE for exit
done = False

pygame.display.set_caption("Do you wanna build a Snowman?")

# setup clock for speed of the program
clock = pygame.time.Clock()


# ------ Function for a Snowman ------#
"""
def draw_snowman (screen, x, y): #xy - where to draw snowman
    '''
    draw snowman at certain location
    draw 3 ellipse (head body base)

    parameter:
    screen(display): call out display to draw
    x, y: where to draw snowman - so that 3 ellipses will be align vertically
    '''
    # NOTE: the ellipse would be drew in the rectangle so the 
    # location xy and width/height are for rectangle's!

    pygame.draw.ellipse(screen, BLACK, [35+x, 0+y, 25, 25]) #head
    pygame.draw.ellipse(screen, BLACK, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, BLACK, [0+x, 65+y, 100, 100])

"""
# ------ Function for stick man ------#
# setup the location and speed for moving the stickman
x_coord = 10
y_coord = 10

x_speed = 0 #positive to move UP, negative to move DOWN
y_speed = 0 #positive to move DOWN, negative to move UP

def draw_stick_figure(screen, x, y):
    # Head
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)
 
    # Legs
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
    pygame.draw.line(screen, BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
 
    # Body
    pygame.draw.line(screen, RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
 
    # Arms
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
    pygame.draw.line(screen, RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

''' 
# set the mouse visible on the screen
pygame.mouse.set_visible(0) #0=invisible, 1= visible
'''

# ------ MAIN PROGRAM CODE ------ #
while done == False:
    # --- set up --- #
    # to make sure if user click close it quits
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # added keyboard into the event
        if event.type == pygame.KEYDOWN: #User press key to move the figure
            # change the speed of the guy
            if event.key == pygame.K_LEFT: # key <--
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3

        if event.type == pygame.KEYUP: #User hands-off the key
            # stop moving the guy
            if event.key == pygame.K_LEFT: # key <--
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0

    # set the screen background
    screen.fill(WHITE)


    # ---- INPUT ---- #
    '''
    # MOUSE - remember to call it before the FIGURE function!
    pos = pygame.mouse.get_pos() # it will be a list which [0] = x, [1] = y
    # attention: x, y below is variables that used in STICK FIGURE function
    # so basically now position of the mouse = x,y of the figure.
    # It will move as the mouse goes
    x = pos[0]
    y = pos[1]
    '''
    '''
    # DRAW SNOWMAN (instead of re-drawing snowmans by calculation x/y each time, we use funtion)
    # note: x, y are given values here = 10, 10
    #### upper left one
    draw_snowman(screen, 10, 10) #draw a snowman on screen at (10, 10)

    #### upper right one
    draw_snowman(screen, 300, 10)

    #### lower left one
    draw_snowman(screen, 10, 300)

    '''

    # CONTROL THE STICKMAN WITH KEYBOARD
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
    print("x_speed: "+ str(x_speed) + " y_speed: " + str(y_speed))

    # DRAW STICK MAN
    draw_stick_figure(screen,x_coord, y_coord) # has changed x/y values to follow the mouse position




    # ---- OUTPUT ---- #
    # This MUST happen after all other drawing command
    pygame.display.flip()

    clock.tick(20)

# Be idle frendly
pygame.quit()