"""
Name: Flappy Bird
Author: Fiona Zhong
Date created: 2022-1-9
"""
import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 860
SCREEN_HEIGHT = 940

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# load images
bg_colour = (51, 199, 255)
bg_img = pygame.image.load('background/mountain.png')
cloud_img = pygame.image.load('background/clouds.png')

run = True
while run:

    screen.fill(bg_colour)
    screen.blit(bg_img, (400, 0))
    screen.blit(cloud_img,(200, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()