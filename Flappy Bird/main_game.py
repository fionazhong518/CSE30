"""
Name: Flappy Bird(maybe?)
author: Fiona Zhong
date created: 2022-01-09
"""

import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

# game setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 640
TILE_SIZE = 32#SCREEN_HEIGHT // ROWS
TILE_TYPES = 27

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4

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
    #width = bg_img.get_width() # all widths are same
    for x in range(4):
        screen.blit(bg_img, (0, 0))
        screen.blit(cloud1_img, (ground_scroll+150, SCREEN_HEIGHT - cloud1_img.get_height()+100))
        screen.blit(cloud2_img, (ground_scroll+200, SCREEN_HEIGHT - cloud2_img.get_height()+100))
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

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += ground_scroll # scroll the world map

# ----------- create sprite groups --------- #
decoration_list = pygame.sprite.Group()
strike_list = pygame.sprite.Group()
blade_list = pygame.sprite.Group()
coin_list = pygame.sprite.Group()
sign_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

run = True
while run:

    clock.tick(20)

    #draw background
    draw_bg()

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()