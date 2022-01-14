"""
Name: Flappy Bird(maybe?)
author: Fiona Zhong
date created: 2022-01-09
"""

from tkinter import EventType
from numpy import true_divide
import pygame, os, csv
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

# game setup
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 544
TILE_SIZE = 32#SCREEN_HEIGHT // ROWS
TILE_TYPES = 27
ROWS = 20
COL = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


#define game variables
GRAVITY = 0.5
ground_scroll = 0
scroll_speed = 0
flying = False
game_over = False

#---------------load images
# background
bg_colour = (52, 199, 255)
bg_img = pygame.image.load('background/bg.png').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (bg_img.get_width(), bg_img.get_height()))
cloud1_img = pygame.image.load('background/cloud1.png')
cloud1_img = pygame.transform.scale(cloud1_img, (cloud1_img.get_width()*2, cloud1_img.get_height()*2))
cloud2_img = pygame.image.load('background/cloud2.png')
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_img.get_width()*2, cloud2_img.get_height()*2))
cloud3_img = pygame.image.load('background/cloud3.png')
cloud3_img = pygame.transform.scale(cloud3_img, (cloud3_img.get_width()*2, cloud3_img.get_height()*2))

# tileset
img_list = []
decoration_img = []
strike_img = []
sign_img = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'tileset/{x}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
    if x >=15 and x <=17:
        decoration_img.append(img)
    if x >= 19 and x <= 21:
        strike_img.append(img)
    if x == 23:
        sign_img.append(img)
# --------- load img into different classes
coin_img = []
for i in range(4):
    img = pygame.image.load(f"Coin/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    coin_img.append(img)
blade_img = []
for i in range(2):
    img = pygame.image.load(f"saw blade/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    blade_img.append(img)

def draw_bg():
    screen.fill(bg_colour)
    screen.blit(bg_img, (0, 0))
    screen.blit(cloud1_img, (ground_scroll+SCREEN_WIDTH, 100))
    screen.blit(cloud2_img, (ground_scroll+SCREEN_WIDTH+300, 60))
    screen.blit(cloud2_img, (ground_scroll+SCREEN_WIDTH+400, 120))

# ---------------------------------- CLASSES ---------------------------------- #
class World():
    def __init__(self):
        self.obstacle_list = [] #for checking collision with blocks
    
    def process_data(self, data):
        
        self.level_length = len(data[0]) # how many columns they are (how wide the level is)
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0: #-1 means empty so ignore
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    #print(len(img_list))
                    # sort different blocks to let them hace different functions
                    if tile >= 0 and tile <= 14:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 15 and tile <= 17:
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(decoration)
                    elif tile  == 18: #snowman
                        pass#snowman = 
                    elif tile >= 19 and tile <= 21: #strikes
                        strike = Strike(img, x * TILE_SIZE, y * TILE_SIZE)
                        strike_list.add(strike)
                    elif tile == 22: #bat
                        pass
                    elif tile == 23: # sign
                        pass
                    elif tile == 24: #blade
                        pass
                    elif tile == 25: #player
                        player = Figure('player',100, SCREEN_HEIGHT//2, 3, 1.2)
                        player_list.add(player)

        return player, strike
    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += ground_scroll
            screen.blit(tile[0], tile[1])
        print(ground_scroll)

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += ground_scroll # scroll the world map

class Figure(pygame.sprite.Sprite):
    def __init__(self,cha_type, x, y, speed, scale):
        super().__init__()
        self.cha_type = cha_type
        self.animation_list = []
        self.action = 0
        self.ani_index = 0
        self.counter = 0

        # Load animation image #
        animation_type = ['fly','fall','dead']
        for animation in animation_type:
            aList = []
            frame_total = len(os.listdir(f'{self.cha_type}/{animation}'))-1
            for i in range(frame_total):
                img = pygame.image.load(f"{self.cha_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                aList.append(img)
            # update all frames to the specific list within the big list
            self.animation_list.append(aList)
        # img variable
        self.image = self.animation_list[self.action][self.ani_index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # movement and shooting
        self.speed = speed
        self.velocity_y = 0
        self.clicked = False
        self.fall = False
        self.shoot_cooldown = 0
        self.shooting = False

        # lives and score
        self.alive = True
        self.score = 0

        # variables for enemies only
        self.idling = True
        self.vision = pygame.Rect(0, 0, 200, 20)

    def update(self):
        self.update_animation()

    def movement(self):
        # fall
        if flying == True:
            #gravity
            self.fall = True
            self.velocity_y += GRAVITY
            if self.velocity_y > 10:
                self.velocity_y = 10
            if self.rect.bottom < 610:
                self.rect.y += int(self.velocity_y)

        if game_over == False:
            #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.fall = False
                self.clicked = True
                self.velocity_y = -5
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                self.fall = True
        # update scrolling 
        if self.cha_type == 'player':
            scroll_speed = self.speed
            
        return scroll_speed

    def update_action(self, new_action):
            # check if the new action is different to the previous one
            if new_action != self.action:
                self.action = new_action
                # reset the variables that are used to update the animation
                self.ani_index = 0
                self.update_time = pygame.time.get_ticks()

    def update_animation(self):
        # animation
        self.counter += 10
        animation_cooldown = 150 # speed of frame changes, the higher # the slower

        if self.counter > animation_cooldown:
            self.counter = 0 # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(self.animation_list[self.action]):
                #if self.action == 5: # dead
                self.ani_index = len(self.animation_list[self.action]) - 1 # stop at the last frame
         # update image depending on current frame
        self.image = self.animation_list[self.action][self.ani_index]
        
    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))

class Strike(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE //2, y )

    def update(self):
        self.rect.x -= scroll_speed
        
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))




# ----------- create sprite groups --------- #
decoration_list = pygame.sprite.Group()
strike_list = pygame.sprite.Group()
blade_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
sign_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()

# ------------- define classes
player = Figure('player',100, SCREEN_HEIGHT//2, 2, 1.2)
player_list.add(player)
#bat = Figure('bat', )


### World background
#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COL
    world_data.append(r)
#load in level data and create world
with open('level0_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
player, strike = world.process_data(world_data)
run = True
while run:

    clock.tick(20)

    #draw background
    draw_bg()
    world.draw()
    # draw sprites
    decoration_list.draw(screen)
    decoration_list.update()
    for strike in strike_list:
        strike.draw()
        strike.update()

    player.draw()
    scroll_speed = player.movement()
    player.update()

    if player.rect.bottom > 610:
        game_over = True
        flying = False
        player.update_action(2) # dead
        
    if game_over == False:
        if player.clicked:
            player.update_action(0) # fly
        elif player.clicked == False and player.fall == True:
            player.update_action(1) # fall
        

        ground_scroll = -scroll_speed
        if abs(ground_scroll) > 5:
            ground_scroll = 5
       


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flying == False and game_over == False:
                flying = True

    pygame.display.update()

pygame.quit()