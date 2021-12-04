'''
Name: Example of using background image and import sounds
Author: Fiona Zhong
Date Created: 2021-09-24
'''
"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
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


# --- Load Image --- #
background_image = pygame.image.load("saturn_family1.jpeg").convert()

# NOTE: for character image that needs to be transparent, better use png/gif rather than jpg
player_image = pygame.image.load("player.png").convert()

## to let the image unshaped and transparent
player_image.set_colorkey(BLACK)

# --- Load Sound --- #
click_sound = pygame.mixer.Sound("laser5.ogg")
'''
Great places to find free sounds!
https://opengameart.org/
www.freesound.org 
'''
# let the mouse disappear
pygame.mouse.set_visible(False)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Play the sound when click mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # NOTE: play sound command must go below EVENT loop so that it wont play forever and repeat
            click_sound.play()
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    ## NOTE: blit command is a method in SCREEN variable 
    ##       so we use it to fill the screen with background image
    screen.blit(background_image, [0, 0])
    
    # Create new variables for Mouse
    player_position = pygame.mouse.get_pos() # this list returns x y location of the mouse
    x = player_position[0]
    y = player_position[1]
    screen.blit(player_image, [x, y]) #display the player image with the x y values of the Mouse

    
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()