"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame, random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

'''
# position of rectangle
rect_x = 50
rect_y = 50
# vector/direction and speed
rect_change_x = 5
rect_change_y = 3
'''

star_list = [] # to get each different snowflake's location stored
for i in range(50):
        x = random.randrange(0, 700) # width. need to match with the screen so can fill the whole
        y = random.randrange(0, 500) # height. need to match with the screen height too
        star_list.append([x, y]) # end up with 50 lists of [x,y] inside the big one
        # APPEND = store each random locations of snowflakes(50 total) into the big list


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    '''  
    # ------ BOUNCING RECTANGLE ------- #
    #rect_x = 50 # <--- need to be taken outside of the loop so it wont always be 50
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50]) #[x, y, width, height]
    
    # Version 2: draw a small rect inside the above one to make it look better
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, 30, 30])

    ### GAME LOGIC CODE ###
    rect_x += rect_change_x
    rect_y += rect_change_y

    #check bondaries
    # the wall need to subtract the width/height of the rect cuz x/y = top left position
    ##### DONT USE = cuz it might wont change dir immediately when it is beyond 650...
    if rect_x > 650 or rect_x < 0: 
        rect_change_x *= -1 
    if rect_y > 450 or rect_y < 0:
        rect_change_y *= -1
    '''

    # ------ FLICKING SNOWING ------- #
    
    for xy_coord in star_list: # so, extract the locations(above) and just apply it to DRAW
                           # so that they wont be flicking + dont need to recreate x/y every time.
        '''
    for i in range(50):
        ### the x and y has been moved above the MAIN
        x = random.randrange(0, 700) # width. need to match with the screen so can fill the whole
        y = random.randrange(0, 500) # height. need to match with the screen height too
        '''
        # NOTE: whyxy_coord[1]? because this represents the y values
        ## LOGIC: star_list = [[x, y], [x, y]...] 
        #             xy_coord = [x, y] and xy_coord[0] = xxy_coord[1] = y

        xy_coord[1] += 1 # to make the snowflakes falling down.
        pygame.draw.circle(screen, WHITE, xy_coord, 2) #xy_coord has replaced [x, y] 
                                                   #so we dont need to recreate
        # to let the snow fall forever
        ## BUT not perfect. the snowflake would always appear at the same location 
        if xy_coord[1] > 500: # if beyond the screen, come back to the top

            ## TO be PERFECTLY random, reset the x and y values if beyond the screen,
            ## but they should be stored into thexy_coord list for convienence
            xy_coord[1] = random.randrange(-20, -5) 
            #                          just a little above the screen for it to recreate
            xy_coord[0] = random.randrange(700) 
            #                            give it a new x position randomly

            
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()