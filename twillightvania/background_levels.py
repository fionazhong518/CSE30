"""
Name: Background and Levels for the Main Game
Author: Fiona Zhong
Date Created: 2021-11-11
"""
import pygame
import button
import csv

#from project_A_mainGame import TILE_SIZE

pygame.init()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH+SIDE_MARGIN, SCREEN_HEIGHT+LOWER_MARGIN))
pygame.display.set_caption('Level Editor')
clock = pygame.time.Clock()

# define colors
GREEN = (144, 201, 120)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

# define font
font = pygame.font.SysFont('Futura', 15)

# define game variables
ROWS = 20
MAX_COLUMNS = 150
TILE_SIZE = 32#SCREEN_HEIGHT // ROWS
TILE_TYPES = 28


scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

current_tile = 0 #index of the current using tile in the tile_list
level = 0 # start with 0 in case of accidentally save the wrong thing
# load images
bg_1 = pygame.image.load('background/bg_0.png').convert_alpha()
bg_1 = pygame.transform.scale(bg_1, (int(bg_1.get_width()*4), int(bg_1.get_height() *4)))
bg_2 = pygame.image.load('background/bg_1.png').convert_alpha()
bg_2 = pygame.transform.scale(bg_2, (int(bg_2.get_width()*4), int(bg_2.get_height()*4)))
bg_3 = pygame.image.load('background/bg_2.png').convert_alpha()
bg_3 = pygame.transform.scale(bg_3, (int(bg_3.get_width()*4), int(bg_3.get_height()*4)))

# ---- LOAD TILESETS IMG
img_list = [] # store tiles in a list
# img with normal 16x16 size
for x in range(TILE_TYPES):
    img = pygame.image.load(f'Tileset/{x}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
# decoration img
for x in range(9):
    img = pygame.image.load(f'Tileset/decorations/{x}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
# some img with special size
img = pygame.image.load('Tileset/sworm.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
img_list.append(img)

img = pygame.image.load('Tileset/torch.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*2)))
img_list.append(img)
# door img
img = pygame.image.load('Tileset/exit.png').convert_alpha()
img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE*2)))
img_list.append(img)

img = pygame.image.load('Tileset/door.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*3)))
img_list.append(img)
# water img
img = pygame.image.load('Tileset/river.png').convert_alpha()
img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE)))
img_list.append(img)
img = pygame.image.load('Tileset/wave.png').convert_alpha()
img = pygame.transform.scale(img, (int(TILE_SIZE*2.5), int(TILE_SIZE)))
img_list.append(img)
img = pygame.image.load('Tileset/Waterfall.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*2)))
img_list.append(img)
# new added inversed door img
img = pygame.image.load('Tileset/door_inversed.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*3)))
img_list.append(img)

save_img = pygame.image.load('save_btn.png').convert_alpha()
load_img = pygame.image.load('load_btn.png').convert_alpha()

print(len(img_list))

# create a list for storing data (empty)
world_data = []
for row in range(ROWS):
    row = [-1] * MAX_COLUMNS
    world_data.append(row)
#create ground
for tile in range(0, MAX_COLUMNS):
    world_data[ROWS - 1][tile] = 0 # very last list becomes all 0

# ptint text onto the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# create function for drawing background
def draw_bg():
    screen.fill(GREEN)
    width = bg_1.get_width() # all widths are same
    for x in range(4):
        screen.blit(bg_1, ((x * width) - scroll* 0.5, 0))
        screen.blit(bg_2, ((x * width) - scroll*0.6, SCREEN_HEIGHT - bg_2.get_height()+100))
        screen.blit(bg_3, ((x * width) - scroll*0.6, SCREEN_HEIGHT - bg_3.get_height()+100))

def draw_grid():
    # vertical lines, only x value in changing, y always = 0
    for col in range(MAX_COLUMNS + 1):
        pygame.draw.line(screen, WHITE, (col * TILE_SIZE - scroll, 0), (col * TILE_SIZE - scroll, SCREEN_HEIGHT))
    # horixontal lines
    for col in range(MAX_COLUMNS + 1):
        pygame.draw.line(screen, WHITE, (0, col * TILE_SIZE), (SCREEN_WIDTH,col * TILE_SIZE))

# draw world tiles
def draw_world():
    # at the very bottom, they would be all ground tiles
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0: # note -1 means empty
                screen.blit(img_list[tile], (x*TILE_SIZE - scroll, y *TILE_SIZE)) #blit the selected tile to the screen

# create buttons
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + LOWER_MARGIN - 50, save_img, 1)
load_button = button.Button(SCREEN_WIDTH // 2 + 100, SCREEN_HEIGHT + LOWER_MARGIN - 50, load_img, 1)

button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):#    (x, y, img, scale)
    tile_button = button.Button(SCREEN_WIDTH + (50 * button_col)+50, 50 * button_row+50, img_list[i], 0.5)
    button_list.append(tile_button)
    button_col += 1 # draw the next tile continuously
    if button_col == 5: # move to the next row if loaded more than 3 button
        button_row += 1
        button_col = 0



RUN = True
while RUN:
    clock.tick(60)
    # draw background
    draw_bg()
    draw_grid()
    draw_world()
    # draw tile panel and tiles 
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    pygame.draw.rect(screen, GREEN, (0, SCREEN_HEIGHT, SCREEN_WIDTH + SIDE_MARGIN, LOWER_MARGIN))
    
    draw_text(f'Level: {level}', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 90)
    draw_text('Press UP or DOWN to change level', font, WHITE, 10, SCREEN_HEIGHT + LOWER_MARGIN - 20)

    # ----- save and load data
    if save_button.draw(screen):
        # save level data
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile: # an easier and neater way of writting csv file
            writer = csv.writer(csvfile, delimiter = ',') # add comma in between to separate each value
            for row in world_data:
                writer.writerow(row)


    if load_button.draw(screen):
        # load in level data
        #1 reset scroll back to the start of the level
        scroll = 0
        with open(f'level{level}_data.csv', newline='') as csvfile: # an easier and neater way of writting csv file
            reader = csv.reader(csvfile, delimiter = ',') # add comma in between to separate each value
            for x, row in enumerate(reader): # read the csv file and quary the index
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile) # convert the read value to int format

    # choose a tile with button function implemented
    button_count = 0
    for button_count, i in enumerate(button_list): #(index, tile button)
        if i.draw(screen): # draw all tiles to the screen
            current_tile = button_count
    # highlight the selected tile
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    #scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True and scroll < (MAX_COLUMNS * TILE_SIZE) - SCREEN_WIDTH:
        scroll += 5 * scroll_speed

    # add new tiles to the screen
    #1 get mouse position
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // TILE_SIZE #increase as I scroll left/right
    y = (pos[1]) // TILE_SIZE

    #2 check that the coordinate are within the tile area
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        #update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                   world_data[y][x] = current_tile
    # codes above allow me to change the x y value by clicking the boxes, 
    # for example: print(x) print(y)
    # if I place the mouse above one of the boxes, it will print the boxes position like (1) (2) [row and col]
    # if I click that box, the value of that boxes would be replaced with the tile's value

    #3 remove tile
        if pygame.mouse.get_pressed()[2] == 1: #right click
            world_data[y][x] = -1
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        # keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN and level > 0:
                level -= 1
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1


    pygame.display.update()

pygame.quit()