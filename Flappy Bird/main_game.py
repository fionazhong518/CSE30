"""
Name: Flappy Bird(maybe?)
author: Fiona Zhong
date created: 2022-01-09
"""

import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


#define game variables
ground_scroll = 0
scroll_speed = 4

#load images
bg_colour = (52, 199, 255)
bg_img = pygame.image.load('background/mountain.png')
bg_img = pygame.transform.scale(bg_img, (bg_img.get_width()*3, bg_img.get_height()*3))
cloud1_img = pygame.image.load('background/cloud1.png')
cloud1_img = pygame.transform.scale(cloud1_img, (cloud1_img.get_width()*3, cloud1_img.get_height()*3))
cloud2_img = pygame.image.load('background/cloud2.png')
cloud2_img = pygame.transform.scale(cloud2_img, (cloud2_img.get_width()*3, cloud2_img.get_height()*3))
cloud3_img = pygame.image.load('background/cloud3.png')
cloud3_img = pygame.transform.scale(cloud3_img, (cloud3_img.get_width()*3, cloud3_img.get_height()*3))



run = True
while run:

    clock.tick(fps)

    #draw background
    screen.fill(bg_colour)

    #draw and scroll the ground
    screen.blit(bg_img, (0, 80))
    screen.blit(cloud1_img, (50, 100))
    screen.blit(cloud2_img, (250, 100))
    screen.blit(cloud3_img, (400, 100))

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()