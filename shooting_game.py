'''
name: shooting game
author: Fiona Zhong
date created: 2021-10-05
'''
import pygame, random

# Define some colors
BLACK = ( 0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
BLUE = (0,0,255)

# -------------------- CLASSES --------------------- #
# This class represents the blocks
class Block(pygame.sprite.Sprite):
    '''parent class to create obstacle'''

    def __init__(self, color):
        super().__init__() #call the parent class

        # Create image of blocks
        self.image = pygame.Surface([20,15])
        self.image.fill(color)

        self.rect = self.image.get_rect()

# This class represents the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent function (here is the another way)
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()

        # create a block of player
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

    def update(self):
        '''update the player's position to follow the mouse'''

        pos = pygame.mouse.get_pos() # this is a list of xy position, [0] = x, [1] = y
        self.rect.x = pos[0]

        # check if the player hit a wall
        if self.rect.x < 0:
            self.rect.x -= self.rect.x
        elif self.rect.x >= 680:
            self.rect.x = 680
        #print(self.rect.x, self.rect.y)
        
class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class
        #pygame.sprite.Sprite.__init__(self)
        super().__init__()
        # set up the bullet's width, height and color
        self.image = pygame.Surface([4,10])
        self.image.fill(BLACK)

        # set up the shape of the bullet (rectangle)
        self.rect = self.image.get_rect()

    def update(self):
        '''Move the bullet'''
        # When fired, the bullet will move up (shoot) 5 pixels
        self.rect.y -= 3

# ----- Create the Window ----- #

# Initialize Pygame
pygame.init()

# set the width and height of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# ----- Sprite Lists ----- #
all_sprites_list = pygame.sprite.Group() # use Group to collect all the sprites include player and blocks

# List of all blocks
block_list = pygame.sprite.Group()

# List of all bullets
bullet_list = pygame.sprite.Group()

# ---- Create the Sprites ---- #
for i in range(50): #50 blocks
    # one block, which two parameter(self, color) = (block, BLUE)
    block = Block(BLUE) # so pygame.sprite.Sprite = BLUE (all sprites set to blue color)

    # Set a random location for the block
    block.rect.x = random.randrange(screen_width - 20)
    block.rect.y = random.randrange(350) # little above the screen for reset

    # Add the block to the lists (both all_sprites and block_list)
    block_list.add(block)
    all_sprites_list.add(block)

# --- Create a Player Block --- #
player = Player()

# Add the player to the big list
all_sprites_list.add(player)

# Set the player's position
player.rect.y = 370

# variable for recording score of player
score = 0


# --- Pygame engine code --- #
# Loop until click the exit bottom
done = False

# manage how fast the screen updates
clock = pygame.time.Clock()

# -------- MAIN PROGRAM LOOP ---------- #
while not done:
    # ---- Event Loop for Processing Pygame ---- #

    for event in pygame.event.get():
        # Default setup for pygame running
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Fire
            bullet = Bullet()
            # set the bullet that it is always following the player (at where the player is)
            bullet.rect.x = player.rect.x
            bullet.rect.y = player.rect.y

            # Add the bullet to all the lists (all_sprites and bullet_list)
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)

    # --- Game Logic --- #
    # Call the update() function on all the sprites
    all_sprites_list.update()

    # Calculate machaics of the bullets
    for bullet in bullet_list:

        # check if the cullet hit a block
        ## here we create a hit_list to see if bullet hits any block (block_list stores all the blocks)
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)

        # For each block hit, remove the bullet and add 1 to the score
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

            score += 1
            print(score)

        # Remove the bullet if it flies off the screen
        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    # ---- Manage the Display Window ---- #

    # Clear the screen
    screen.fill(WHITE)

    # Draw all sprite
    all_sprites_list.draw(screen)

    # update the screen with what we've draw and flip it to display
    pygame.display.flip()

    # --- Setup Clock speed for Running Pygame per second
    clock.tick(60)

pygame.quit()