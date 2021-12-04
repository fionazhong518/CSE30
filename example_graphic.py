'''
following tutorial about graphic in pygame
author: Fiona Zhong
date created: 2021-9-17
'''
# Import a library of functions called 'pygame'
import pygame, math

# Initialize the game engine
pygame.init()

# Define some colors (0-255)
## (Red, Green, Blue)  can find color combinations on: www.colorpicker.com
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Set the width and height of the screen
size = [700, 500] # width,height unit:px
# NOTE: why brackets? cuz python can't normally store two numbers, so 
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Prodessor Craven's cool Game")

# so far, the program would create a window and immediately hang.
# we can't interact or even lose it.
# so code need to be added so that the program waits in a loop until the user clicks "exit"

# Added Pi to draw an ARC
pi = 3.1415926535

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen(loop) update
clock = pygame.time.Clock() # will limit to 20 times/sec

# was moved from DRAW TEXT section to speed up the program
font = pygame.font.Font(None, 25)

# ---- MAIN PROGRAM LOOP -----#
while done == False:
    ####### INPUT #########
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if user clicked close
            done = True # Flag that we are done so we ecit this loop
    # ALL EVENT PROCESSING SHOULD GO GO BELOW THIS COMMENT


    ####### PROCESSING ########

    # All code to DRAW should go below this comment

    # YOU MUST FLIP THE DISPLAY AFTER YOU DRAW!!! otherwise it will cause the creen to flicker
    ### logic: waits to the display the screen UNTILL the program has finished drawing
    screen.fill(white) # fill the display with white color, related to line 22
    # call SCREEN.FILL first because I want to draw above the white background

    '''
    pygame.draw.line(screen, green, [0,0], [100, 100], 5)
    # library.module.function(1 window we open, color drawing, [start location], [end position], width if blank defalt 1)
    '''
    # can't just simply call for i in range(5) <-- draw 5 times at the same location (see above)
    for x in range(0, 100, 20): # (start, stop, step by)
        pygame.draw.line(screen, green, [x, 0], [x, 100], 5)
        # start position:[0,0] -> [20, 0]
        #                  |          |
        # end position: [0, 100] -> [20, 100]


    ## COMPLEX offsets for this one: MAKE SURE TO IMPORT MATH
    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 400 
        y = int(75 * math.cos(radians_y)) + 400
        # int(size * math.sin(1/20) + move the grath to the middle)

        pygame.draw.line(screen, black, [x,y], [x+8, y], 6) # [x+#,y], larger # more continuous

    '''
    Here is a list of things that you can draw:
    http://www.pygame.org/docs/ref/draw.html
    '''
    # DRAW a Rectangle
    pygame.draw.rect(screen, black, [150, 50, 250, 100], 2) #[x, y, width, height], width of line
    ## if the width of the line = 0, then it will be solid black

    # DRAW a Ellipse (it is inside the rectangle above)
    ### however, the ellipse would not start drawing at 150
    pygame.draw.ellipse(screen, black, [150, 50, 250, 100], 2) #[x, y, width, height], width of line


    # DRAW AN ARC, 1.figure out the rectangle to draw ARC inside
    # All arc would be drew inside this rect[x, y, w, h], start angle, end angle
    # for angles you can look up them online (tips: do you remember the big circle?)
    pygame.draw.arc(screen, green, [100, 200, 250, 200], pi/2,      pi, 2)
    pygame.draw.arc(screen, black, [100, 200, 250, 200],    0,    pi/2, 2)
    pygame.draw.arc(screen, red, [100, 200, 250, 200], 3*pi/2,    2*pi, 2)
    pygame.draw.arc(screen, blue, [100, 200, 250, 200],    pi,  3*pi/2, 2)


    # DRAW AN POLYGON
    pygame.draw.polygon(screen, blue, [[100, 100], [0,200], [200, 200], [100, 150]], 5)
    #  in this case: [[x, y of the first point],[second point], [third point]]
    # you can add as many [location of the point] into it to create different polygons


    # DRAW A TEXT
    # 1) what font, how big?   2) create a stamp (combine what text, font, size)  3)where you want it to go, stamp it
    
    # STEP 1: What Font, How Big?
    '''
    font = pygame.font.Font(None, 25)
    #  ------|           (defalut fone, size)
    #        |  the font was moved to the front of the MAIN CODE 
    text = font.render("My text", True, black) # True = anti-alien thing # STEP 2: create stamp
    '''
    # NOTE: usually you create FONT before the program to speed it up cuz the program is running 20px,
    #     but font is always the same. Also, it would be easier for users to specify the font they want
    #     (MAIN PROGRAM is really heavy so relieve it )
    ## to find font, 
    # search in Finder - Fonts file - right click -open new window - properties - copy file name
    # ("location/location/filename/")


    # if want to add a score board (for different uses)
    score = 100
    # STEP 2：create a stamp that combine font.render(text, good_to_print, color)
    # render = sorts of combine things together
    text = font.render("Score: " + str(score), True, red)
    #      you HAVE TO convert int(100) -> str(score) otherwise python would get confused

    

    # STEP 3: Stamp the text on the screen
    # blit = stamp it to the screen
    screen.blit(text, [500, 300] ) #[top-left coordinate] = where I want to draw


    # TRY ON YOUR OWN
    # draw a slope
    pygame.draw.line(screen, red, [0,0], [100, 100], 5)

    # draw a series of line (horizontal)
    for x in range(400, 800, 10):
        for y in range(0, 300, 10): # (smaller 10, denser the line)
            pygame.draw.line(screen, blue, [x, y], [x, y], 50)

    # draw a series of slopes
    for y_offset in range(100, 200, 10): #draw from (200, 100) to (400, 200) 
        pygame.draw.line(screen, red, [200, 100+ y_offset], [400,200+y_offset], 5)

    pygame.display.flip()

    clock.tick(20)

pygame.quit()