"""
Use sprites to collect blocks.
 
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
Explanation video: http://youtu.be/4W2AqUetBi4
"""
import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

#   pygame sprite package, parentclass
class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x = (int) and rect.y = (int)
        self.rect = self.image.get_rect()
    def reset_pos(self):
        self.rect.y = random.randrange(-300, -20)
        # too let it fall from different position, reset x to random
        self.rect.x = random.randrange(700 - 20)
        
    def update(self):
        self.rect.y += 1

        if self.rect.y > 410: #reset the block to the top again if it falls out of the screen
            self.reset_pos()

class Player(Block):
    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()
 
        # Fetch the x and y out of the list,
            # just like we'd fetch letters out of a string.

        ## Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]



# Initialize Pygame
pygame.init()
 
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
 
# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()
 
# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# ------ Createing Blocks ------- #
for i in range(50):
    # This represents a block
    block = Block(BLACK, 20, 15) # color, width, height
 
    # Set a random location for the block
    block.rect.x = random.randrange(screen_width - 20)
    block.rect.y = random.randrange(screen_height - 15)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)
 
# Create a RED player block
player = Player(RED, 20, 15)
all_sprites_list.add(player)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
score = 0
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
 
    # Clear the screen
    screen.fill(WHITE)
    '''
    # NOTE: the following is moved into the update function under Player class
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.

    ## Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    '''
    ## More Challenging feature: blocks will fall off the screen
    all_sprites_list.update()
 
    # See if the player block has collided with anything.
    # spritecolloide: check if the BLOCK in the block_list is collided with PLAYER
    # And it will remove the collided blocks (into the blocks_hit_list)
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)
 
    # Check the list of collisions.
    for block in blocks_hit_list: #each hit will add one score by checking new things added to the list
        score += 1
        print(score)
        block.reset_pos()
 
    # Draw all the spites
    all_sprites_list.draw(screen)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()