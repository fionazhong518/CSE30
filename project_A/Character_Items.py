"""
Name: Fighter Flight
author: Fiona Zhong
date created: 2021-10-13
"""
''' GOALS BY STEPS
1. create player and let it be able to move with buttons
2. let the player be able to shoot 
3. create enemy(computer) class that can shoot automatically (maybe some AI thing?)
4. 
'''
import pygame, random, os, csv, time

from pygame.constants import APPACTIVE, DROPCOMPLETE, K_SPACE, KEYDOWN, KEYUP, K_w


#from background_levels import ROWS, TILE_SIZE
# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Game Window
screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("my game")

clock = pygame.time.Clock()

# ---- VARIABLES ---- #
# game defalut setting
GRAVITY = 0.75
SCROLL_THRESH = 200
ROWS = 20
COLS = 150
TILE_SIZE = 32#screen_height // ROWS
TILE_TYPES = 28
screen_scroll = 0
bg_scroll = 0
level = 2
start_game = False

# -- player
player_move_left = False
player_move_right = False
shoot = False
player_shooting = False

# ------------------------- LOAD IMAGES ---------------------------- #
# background img
bg_1 = pygame.image.load('background/bg_0.png').convert_alpha()
bg_1 = pygame.transform.scale(bg_1, (int(bg_1.get_width()*4), int(bg_1.get_height() *4)))
bg_2 = pygame.image.load('background/bg_1.png').convert_alpha()
bg_2 = pygame.transform.scale(bg_2, (int(bg_2.get_width()*4), int(bg_2.get_height()*4)))
bg_3 = pygame.image.load('background/bg_2.png').convert_alpha()
bg_3 = pygame.transform.scale(bg_3, (int(bg_3.get_width()*4), int(bg_3.get_height()*4)))
'''
# button img
start_img = pygame.image.load('')
'''
img_list = [] # store tiles in a list
box_img = []
strike_img = []
# img with normal 16x16 size
for x in range(TILE_TYPES):
    img = pygame.image.load(f'Tileset/{x}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
    if x == 16:
        box_img.append(img)
    if x == 15:
        strike_img.append(img)
    #if x == 15:
        #strike_img.append(img)
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


# water img
img = pygame.image.load('Tileset/river.png').convert_alpha()
img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE)))
img_list.append(img)
img = pygame.image.load('Tileset/wave.png').convert_alpha()
img = pygame.transform.scale(img, (int(TILE_SIZE*2.5), int(TILE_SIZE)))
img_list.append(img)
img = pygame.image.load('Tileset/waterfall.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*2)))
img_list.append(img)
'''

'''
# -- bullet
bullet_img = pygame.image.load('Bullet.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (int(bullet_img.get_width()*1.2), int(bullet_img.get_height() * 1.2)))

# -- items and water image
## Red flask
red_flask_img = []
for i in range(4):
    img = pygame.image.load(f"Items/Red_flask/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    # add all types of img to the animation_list (big list)
    red_flask_img.append(img)
## Chest
chest_img = []
for i in range(4):
    img = pygame.image.load(f"Items/Chest/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    # add all types of img to the animation_list (big list)
    chest_img.append(img)
## Coin
coin_img = []
for i in range(4):
    img = pygame.image.load(f"Items/Coin/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    coin_img.append(img)
## Key
key_img = []
for i in range(4):
    img = pygame.image.load(f"Items/key/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    key_img.append(img)
## bottle
bottle_img = []
img = pygame.image.load("Items/bottle.png")
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
bottle_img.append(img)
## sign
sign_img =[]
img = pygame.image.load("Items/sign.png")
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
bottle_img.append(img)
## water img
river_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/river/{1}.png').convert_alpha()
    img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE)))
    river_img.append(img)
wave_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/wave/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (int(TILE_SIZE*2.5), int(TILE_SIZE)))
    wave_img.append(img)
waterfall_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/waterfall/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*2)))
    waterfall_img.append(img)
mushroom_img = []
for i in range(6):
    img = pygame.image.load(f'Mushroom/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    mushroom_img.append(img)
woodstep_img = []
img = pygame.image.load('Tileset/decorations/7.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
woodstep_img.append(img)
items_water = {
    'Red_flask' : red_flask_img,
    'Chest' : chest_img,
    'Coin' : coin_img,
    'Key' : key_img,
    'Bottle' : bottle_img,
    'Sign' : sign_img,
    'Box' : box_img,
    'River' : river_img,
    'Wave' : wave_img,
    'Waterfall' : waterfall_img,
    'Mushroom' : mushroom_img,
    'Strike' : strike_img,
    'Wood' : woodstep_img
}

## Heart
heart_img = pygame.image.load('Items/Heart.png')
heart_img = pygame.transform.scale(heart_img, (int(heart_img.get_width()*0.9), int(heart_img.get_height() * 0.9)))

# --- Triggers
## button
button_img = [] #[0]is up, [1] is down
img = pygame.image.load("Items/Button/0.png")
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
button_img.append(img)
img = pygame.image.load("Items/Button/1.png")
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
button_img.append(img)
## lever
lever_img = [] #[0]is left, [1]is right
for i in range(2):
    img = pygame.image.load(f"Items/Lever/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    lever_img.append(img)
triggers = {
    "Button" : button_img,
    "Lever" : lever_img
}
# Font
pygame.font.init()
font = pygame.font.SysFont('Futura', 15)

# ---- Texts and Background ---- #
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_bg():
    # continuous background
    width = bg_1.get_width()
    for x in range(5):
        screen.blit(bg_1, ((x * width) - bg_scroll * 0.5, 0))
        screen.blit(bg_2, ((x * width) - bg_scroll * 0.6, screen_height - bg_2.get_height()+100))
        screen.blit(bg_3, ((x * width) - bg_scroll * 0.6, screen_height - bg_3.get_height()+100))
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
                    # sort different blocks to let them hace different functions
                    if tile >= 0 and tile <= 11:
                        self.obstacle_list.append(tile_data)

                    elif tile >= 12 and tile <= 13: # left and right arrow sign
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(decoration)

                    elif tile >= 14 and tile <= 15:# strikes
                        strike = Item_Water('Strike', x * TILE_SIZE, y * TILE_SIZE)
                        #item_list.add(strike)
                        strike_list.add(strike)
                    elif tile == 16:# push box
                        box = Item_Water('Box', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(box)

                    elif tile == 17: # coin, 
                        coin = Item_Water('Coin', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(coin)                      
                    elif tile == 18: # flask, 
                        red_flask = Item_Water('Red_flask', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(red_flask)
                    elif tile == 19: # treasure box, 
                        chest = Item_Water('Chest', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(chest)
                    elif tile == 20: # bottle, 
                        bottle = Item_Water('Bottle', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(bottle)
                    elif tile == 21: # sign, 
                        sign = Item_Water('Sign', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(sign)
                    elif tile == 22: # key
                        key = Item_Water('Key', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(key)

                    elif tile == 23:# lever
                        lever = Trigger('Lever', x * TILE_SIZE, y * TILE_SIZE)
                        trigger_list.add(lever) 
                    elif tile == 24:# player                       
                        player = Figure('player', x * TILE_SIZE, y * TILE_SIZE, 2, 5, 50)
                        #all_sprite_list.add(player)

                    elif tile == 25:# enemies
                        trunk = Figure('Trunk', x * TILE_SIZE, y * TILE_SIZE, 1, 2, 50)
                        enemy_list.add(trunk)
                    elif tile == 26:
                        mushroom = Item_Water('Mushroom', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(mushroom)
                    elif tile == 27:
                        goblin = Figure('Goblin', x * TILE_SIZE, y * TILE_SIZE, 2, 2, 50)
                        enemy_list.add(goblin)
                        

                    elif tile >= 28 and tile <= 29:# decoration grass
                        grass = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(grass) 
                    elif tile >= 30 and tile <= 31:
                        pass # bloom and not-bloom flower
                    elif tile == 32:# root
                        root = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(root) 
                    elif tile == 33:# button
                        button = Trigger('Button', x * TILE_SIZE, y * TILE_SIZE)
                        trigger_list.add(button) 
                    elif tile >= 34 and tile <= 36: # woodstep
                        woodstep = Item_Water('Wood', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(woodstep)
                    elif tile == 37:# worm
                        worm = Figure('worm', x * TILE_SIZE, y * TILE_SIZE, 2, 0.1, 30)
                        enemy_list.add(worm) 
                    elif tile == 38:# torch
                        torch = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(torch)
                    elif tile == 39: # exit
                        exit = Exit(img, x * TILE_SIZE, y * TILE_SIZE)
                        exit_list.add(exit) 
                    elif tile == 40: # door
                        door = Door('Door', x * TILE_SIZE, y * TILE_SIZE)
                        door_list.add(door) 
                    elif tile >= 41 and tile <= 43:# river, wave and waterfall
                        river = Item_Water('River', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(river)
                        wave = Item_Water('Wave', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(wave)
                        waterfall = Item_Water('Waterfall', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(waterfall)
                    elif tile == 44: # new inversed door img
                        door_inv = Door('Door_Inversed', x * TILE_SIZE, y * TILE_SIZE)
                        door_list.add(door_inv)

        return player, button, lever, box, exit, mushroom
    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += screen_scroll # x coordinate add in screen_scroll to move the world map
            screen.blit(tile[0], tile[1])

class Trigger(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        super().__init__()
        self.type = img
        self.ani_index = 0
        self.image = triggers[img][self.ani_index]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.action = 0
        self.cool_down = 150

        self.press_down = False
        self.turning = False

    def update(self):
        self.rect.x += screen_scroll
        # functionality
        if self.type == 'Button':
            self.press()
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - (self.rect.height//2)
                player.rect.x = player.rect.x
                if player.velocity_y >= 0:
                    player.velocity_y = 0
                    player.inair = False
                    player.rect.y = self.rect.y - self.height//4
             
            # new action of the button
            if self.press_down:
                self.update_action(1) # button down
            else:
                self.update_action(0)

        if self.type == 'Lever':
            if self.turning:
                self.update_action(1)
            else:
                self.update_action(0)

    def turn(self):      
        if pygame.sprite.collide_rect(self, player) or pygame.sprite.collide_rect(self, enemy):
            if not self.turning:
                self.turning = True
            else:
                self.turning = False

    def press(self):
        if pygame.sprite.collide_rect(self, player) or pygame.sprite.collide_rect(self, enemy) or pygame.sprite.collide_rect(self, box):
            self.press_down = True
        else:
            if self.press_down:
                self.cool_down -= 1
                if self.cool_down <= 0:
                    print('up')
                    self.press_down = False

    def update_action(self, new_action):
        if self.type == 'Button':
            self.image = button_img[self.action]
        if self.type == 'Lever':
            self.image = lever_img[self.action]
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            
class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll # scroll the world map

class Water(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))
    def update(self):
        self.rect.x += screen_scroll # scroll the world map
        # funtionality
        self.update_animation()

    def update_animation(self):
            animation_cooldown = 150 # speed of frame changes, the higher # the slower

            # update image depending on current frame
            
            self.image = items_water[self.type][self.ani_index]
            
            # check if enough time has passed since the last update
            #               new time - last updated time > specific cooldown period
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks() # reset the timer
                self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(items_water[self.type]):
                self.ani_index = 0

class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll # scroll the world map
        # funtionality

    def update_level(self):
        global level
        if pygame.sprite.collide_rect(self, player):
            if level == 1:
                print('next')
                level = 2
            elif level == 3:# game over
                pass 
        return level

class Door(pygame.sprite.Sprite):
    def __init__(self, img_type, x, y):
        super().__init__()
        self.img_type = img_type
        self.animation_list = []
        self.action = 0
        self.ani_index = 0
        self.update_time = pygame.time.get_ticks()
        # Load Animation Image
        animation_type = ['default', 'opening', 'closing']
        for animation in animation_type:
            aList = [] # create a temporary list to collect frames of img
            frame_total = len(os.listdir(f'Tileset/{self.img_type}/{animation}'))-1 # new way to count # of files in one folder
            #print(frame_total)
            for i in range(frame_total):
                img = pygame.image.load(f"Tileset/{self.img_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*2), int(img.get_height()*2)))
                aList.append(img)
            # update all frames to the specific list within the big list
            self.animation_list.append(aList)
        # img
        self.image = self.animation_list[self.action][self.ani_index]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - self.image.get_height())
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # open
        self.open = False
        self.idle = True

    def update(self):
        self.update_animation()
        self.rect.x += screen_scroll
        # open
        if self.img_type == 'Door':
            self.open = button.press_down
        else:
            self.open = lever.turning
        if self.open:
            self.update_action(1) # opening
            self.open = False
            self.idle = False
        elif self.open == False and self.idle == False:
            self.update_action(2)
            if self.ani_index == len(self.animation_list[self.action]):
                self.idle = True
        if self.idle:
            self.update_action(0)
        
     
    def update_animation(self):
        animation_cooldown = 150 # speed of frame changes, the higher # the slower

        # update image depending on current frame
        self.image = self.animation_list[self.action][self.ani_index]
        
        # check if enough time has passed since the last update
        #               new time - last updated time > specific cooldown period
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks() # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

        # aviod animation list run out of the range (back to the start)
        if self.ani_index >= len(self.animation_list[self.action]):
            if self.action == 1:
                self.ani_index = self.ani_index - 1
            elif self.action == 2:
                self.ani_index = self.ani_index
            else:
                self.ani_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # reset the variables that are used to update the animation
            self.ani_index = 0
            self.update_time = pygame.time.get_ticks()

class Figure(pygame.sprite.Sprite):
    def __init__(self, char_type,player_x, player_y, scale, speed, max_movement):
        super().__init__()
        # ---- image ---- #
        self.char_type = char_type
        self.animation_list = []
        self.action = 0
        self.ani_index = 0
        self.update_time = pygame.time.get_ticks()

    ## --- Load animation images of different actions --- #
        # NEW WAY OF LOADING IMAGES
        animation_type = ['Idle', 'Run', 'Jump', 'Attack', 'Hit','Dead']
        for animation in animation_type:
            aList = [] # create a temporary list to collect frames of img
            frame_total = len(os.listdir(f'{self.char_type}/{animation}'))-1 # new way to count # of files in one folder
            for i in range(frame_total):
                img = pygame.image.load(f"{self.char_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                aList.append(img)
            # update all frames to the specific list within the big list
            self.animation_list.append(aList)

        # img
        self.image = self.animation_list[self.action][self.ani_index]
        self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (player_x, player_y)
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # movement and shooting
        self.speed = speed
        self.direction = 1
        self.jump = False
        self.velocity_y = 0
        self.inair = False
        self.shoot_cooldown = 0
        self.shooting = False

        # lives
        self.alive = True
        self.health = 5
        self.max_health = self.health # will be useful for adding health later
        # score and item collect
        self.score = 0
        self.key = False
        self.bottle = 0
        self.sign = False

        # create variable for ai only
        self.move_counter = 0
        self.max_movement = max_movement
        self.ai_moving_left = False
        self.ai_moving_right = False
        self.idling = False
               # create a rect for ai to monitor if player comes toward
        self.vision = pygame.Rect(0, 0, 150, 20) #150 = how far the enemy can see
        self.attack_cooldown = 0

    def Movement(self, move_left, move_right):
        # world scrolling variable
        screen_scroll = 0
        # reset direction variables 
        dir_x = 0
        dir_y = 0
        #----- move left/right
        if move_left:
            dir_x = -self.speed
            self.flip = True
            self.direction = -1
        if move_right:
            dir_x = self.speed
            self.flip = False
            self.direction = 1

        #----- jump
        if self.jump == True and self.inair == False:
            self.velocity_y = -10 #NOTE: going up = decreasing y value
            #let jump only happen once when press W
            self.jump = False 
            self.inair = True

        #----- falling
        self.velocity_y = self.velocity_y + GRAVITY
        # to not let the player fall too fast
        if self.velocity_y > 10:
            self.velocity_y = 10
            
        dir_y += self.velocity_y

        # check if hit the floor (player's bottom collide with the ground)
        for tile in world.obstacle_list:
            # check collision in the horizontal direction (left/right)
            if tile[1].colliderect(self.rect.x + dir_x, self.rect.y, self.width, self.height):
                dir_x = 0
                # if the ai has hit the wall, make it turn around
                if self.char_type == 'worm'or self.char_type == 'Trunk':
                    self.direction *= -1
                    self.move_counter = 0 # restart counting units moved
            # check collision in vertical direction (up and down)
            if tile[1].colliderect(self.rect.x, self.rect.y + dir_y, self.width, self.height):
                # if it is below the ground (jumping and gonna hit the upper level)
                if self.velocity_y < 0:
                    self.velocity_y = 0
                    dir_y = tile[1].bottom - self.rect.top
                # if it is above the ground (falling and gonna hit the bottom level)
                elif self.velocity_y >= 0:
                    self.velocity_y = 0
                    dir_y = tile[1].top - self.rect.bottom
                    self.inair = False

        # check if off screen
        if self.char_type == 'player':
            if self.rect.left + dir_x < 0 or self.rect.right + dir_x > screen_width:
                dir_x = 0

        # update player position
        self.rect.x = self.rect.x + dir_x
        self.rect.y = self.rect.y + dir_y

        # update scrolling based on player's position
        if self.char_type == 'player':   # scroll left when meet a specific bondary AND not exceed the width of the bg(level tiles * size) - screenwidth !< 0
            if (self.rect.right > screen_width - SCROLL_THRESH and bg_scroll < (world.level_length * TILE_SIZE) - screen_width)\
                 or (self.rect.left < SCROLL_THRESH and bg_scroll  > abs(dir_x)):
                     # scroll right when player moves left AND check if dir not less than 0
                self.rect.x -= dir_x #infact the screen is gonna shift to left but player is not moving
                screen_scroll = -dir_x # screen scroll at opposite direction
            

        return screen_scroll # need to return back to the main game


    def update(self):
        self.update_animation()
        self.check_alive()
        # set the shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def update_animation(self):
        animation_cooldown = 150 # speed of frame changes, the higher # the slower

        # update image depending on current frame
        self.image = self.animation_list[self.action][self.ani_index]
        
        # check if enough time has passed since the last update
        #               new time - last updated time > specific cooldown period
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks() # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

        # aviod animation list run out of the range (back to the start)
        if self.ani_index >= len(self.animation_list[self.action]):
            if self.action == 5: # dead
                self.ani_index = len(self.animation_list[self.action]) - 1 # stop at the last frame
            else:
                self.ani_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # reset the variables that are used to update the animation
            self.ani_index = 0
            self.update_time = pygame.time.get_ticks()

    def shoot_bullet(self):
        '''this function would run only on space key press'''

        if self.shoot_cooldown == 0: #limit how quickly player can fire
            self.shoot_cooldown = 50
            
            bullet = Bullets(self.rect.centerx + int(1.2 * self.rect.size[0] * self.direction),self.rect.centery, self.direction)
            bullet_list.add(bullet)

    def attack(self):
        
        self.update_action(3) # Attack
        #print(self.attack_cooldown)
        if player.alive: # if character is alive (player and enemy for now)
            
            if self.attack_cooldown == 0:
                self.attack_cooldown = 30
                player.health -= 1
                player.update_action(4)
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1   
                
    def ai(self):
        if self.alive and player.alive:
            if self.idling == False and random.randint(1, 200) == 1: # let the enemy move randomly by picking a random #
                self.update_action(0) # Idle
                self.idling = True
            # check if the player goes into enemy's vision range
            if self.vision.colliderect(player.rect):
                if self.char_type == 'Trunk':
                    self.update_action(3) #attack
                    self.shoot_bullet()
                '''
                if self.char_type == 'worm':
                    if self.rect.colliderect(player.rect):
                        player.health -= 1
                '''
                if self.char_type == 'Bigguy' or self.char_type == 'worm':
                    self.Movement(self.ai_moving_left, self.ai_moving_right)

                    if self.rect.colliderect(player.rect):
                        self.speed = 0
                        self.attack()
                    else:
                        self.speed = 2
            else:
                self.speed = 1
                self.idling = False

                if self.idling == False:
                    if self.direction == 1:
                        self.ai_moving_right = True
                    else:
                        self.ai_moving_right = False
                    self.ai_moving_left = not self.ai_moving_right
                    self.Movement(self.ai_moving_left, self.ai_moving_right)
                    self.update_action(1) # Run
                    self.move_counter += 1

                    # update ai vision as the enemy moves
                    self.vision.center = (self.rect.centerx + 75*self.direction, self.rect.centery) # monitoring at a range of 75
                    #pygame.draw.rect(screen, RED, self.vision) #vision range

                    if self.move_counter > self.max_movement: # when move specific units, change direction
                        self.direction *= -1
                        self.move_counter *= -1
                else:
                    self.idling = True
        # scroll
        self.rect.x += screen_scroll # enemy scrolls as the world map scroll  
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(5) #death

    def draw(self):               #(image,     x(t/f),  y(t/f), rect)          
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 10
        if direction < 0:
            self.image = pygame.transform.flip(bullet_img, True, False)
        else:
            self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
     
    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed) + screen_scroll # also need to scroll as the world moves
        
        # check if off screen
        if self.rect.right < 0 or self.rect.left > screen_width - 50:
            self.kill()
        # check collision with blocks
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()
        # check collision with characters
        if pygame.sprite.spritecollide(player, bullet_list, False):
            if player.alive: # if character is alive (player and enemy for now)
                player.health -= 1
                player.update_action(4) #hit
                self.kill() #bullet disappear
        for enemy in enemy_list:
            if pygame.sprite.spritecollide(enemy, bullet_list, False):
                if enemy.alive: # if character is alive (player and enemy for now)
                    enemy.health -= 1
                    enemy.update_action(4) #hit
                    self.kill() #bullet disappear

class Strikes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Item_Water(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        super().__init__()  
        self.type = item_type
        self.action = 0 # for chest only
        self.ani_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = items_water[item_type][self.ani_index]

        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - self.image.get_height())

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.velocity_y = 0
        self.old_pos = self.rect.y

        self.collide_button = False

    def update(self):
        # scroll
        self.rect.x += screen_scroll # scroll the world map

        # funtionality     
        self.update_animation()
        if self.type == 'Box':
            self.box()
        if self.type == "Mushroom":
            self.mushroom()
        if self.type == 'Strikes':
            pass
        if self.type == 'Wood':
            self.woodstep()

        # if collide
        if pygame.sprite.collide_rect(self, player):
            # check what kind of item the player meet
            if self.type == 'Red_flask':
                player.health += 1
                # check if the player's health reaches the maximun value
                if player.health > player.max_health:
                    player.health = player.max_health
            elif self.type == 'Chest':
                player.score += 5
            elif self.type == 'Coin':
                player.score += 1
            elif self.type == 'Key':
                player.key = True
            elif self.type == 'Sign':
                player.sign = True
            elif self.type == 'Bottle':
                player.bottle = 1
            elif self.type == 'River' or self.type == 'Wave':
                pass
            elif self.type == 'Waterfall':
                pass
            # delete the item
            if self.type != 'Box' and self.type != 'Mushroom' and self.type != "Strike" and self.type != 'Wood':#or self.type != 'River' or self.type != 'Wave' or self.type != 'Waterfall':
                self.kill()

    def woodstep(self):
        update_y = 0
        if lever.turning:
            update_y = -1
            if self.rect.y + update_y <= self.old_pos-(2 * TILE_SIZE):
                update_y = 0
        self.rect.y += update_y

        #collision
        if pygame.sprite.collide_rect(self, player):
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - player.height
                player.inair = False
        if mushroom.rect.collidepoint(self.rect.midtop):
                print('collide')
        '''
        if pygame.sprite.collide_rect(self, mushroom):
            print('collide')
            mushroom.rect.y = self.rect.y - mushroom.height
        '''

    def strikes(self):
        self.velocity_y += GRAVITY
        update_y = 0
        
        fall_point_y = self.rect.y + 4* TILE_SIZE # if player is within 4 units away from the strikes, strikes fall
        if player.rect.y <= fall_point_y:
            update_y = self.velocity_y
            if self.velocity_y >= 5:
                self.velocity_y = 5

        if self.rect.colliderect(player):
            print('hit')
            player.health -= 1
        
        # bondaries
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + update_y, self.width, self.height):
                if self.velocity_y > 0:
                    self.velocity_y = 0
                    self.rect.y = tile[1].top
                if self.rect.bottom == tile[1].top:
                    self.kill()

        #update y location
        self.rect.y += update_y  

    def mushroom(self):
        if pygame.sprite.collide_rect(self, player):
            # bondaries
            if player.rect.collidepoint(self.rect.midleft):
                player.rect.x = self.rect.x - player.width
            if player.rect.collidepoint(self.rect.midright):
                player.rect.x = self.rect.x + player.width
            # spring
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - player.height
                player.velocity_y = -18
                
    def box(self):
        self.direction = player.direction # by passing player's direction, the movement of the box would be more fluent
        self.velocity_y += GRAVITY
        update_x = 0
        update_y = 0
        collide_x = False
        collide_y = False
        if pygame.sprite.collide_rect(self, player):
            if player.rect.collidepoint(self.rect.midleft) or player.rect.collidepoint(self.rect.midright):
                collide_x = True
                collide_y = False
            else:
                collide_x = False

            if player.rect.collidepoint(self.rect.midtop):
                collide_y = True
                collide_x = False
            else:
                collide_y = False
                
            if collide_x and collide_y == False:
                self.rect.y = self.rect.y
                update_x = self.direction * player.speed
                player.rect.x = self.rect.x - int(player.width * player.direction)

            if collide_y and collide_x == False: #fix this by using player.inair?
                self.rect.x = self.rect.x
                player.rect.x = player.rect.x
                player.velocity_y = 0
                player.inair = False
                player.rect.y = self.rect.y - player.height

        update_y += self.velocity_y
        # check bondaries
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + update_x, self.rect.y, self.width, self.height): # left/right
                update_x = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + update_y, self.width, self.height):
                if self.velocity_y > 0:
                    self.velocity_y = 0
                    update_y = tile[1].top - self.rect.bottom
        
        # let player push the box
        self.rect.x += update_x
        self.rect.y += update_y

    def update_animation(self):
            animation_cooldown = 150 # speed of frame changes, the higher # the slower

            # update image depending on current frame
            
            self.image = items_water[self.type][self.ani_index]
            
            # check if enough time has passed since the last update
            #               new time - last updated time > specific cooldown period
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks() # reset the timer
                self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(items_water[self.type]):
                self.ani_index = 0
    
class HealthBar():
    def __init__(self, x, y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
    
    def draw(self, health):
        # update with new health
        #self.health = health
        ratio =  self.health / self.max_health
        #print(ratio)
        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 49, 15)) #frame of the health bar
        pygame.draw.rect(screen, BLUE,(self.x, self.y, 45 * ratio, 10)) # damage
        pygame.draw.rect(screen, RED, (self.x, self.y, 45, 10)) # actual health
        

# ------ SPRITES ------ #
#--- sprite list
all_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()
decoration_list = pygame.sprite.Group()
#water_list = pygame.sprite.Group()
exit_list = pygame.sprite.Group()
door_list = pygame.sprite.Group()
trigger_list = pygame.sprite.Group()
strike_list = pygame.sprite.Group()


### World background
#create empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
#load in level data and create world
with open(f'level{level}_data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] = int(tile)

world = World()
player, button, lever, box, exit, mushroom = world.process_data(world_data)
# ---- MAIN PROGRAM LOOP ---- #
run = True
while run:

    
    clock.tick(60)
    #if start_game == False:
        # draw menu
    screen.fill(WHITE)
    #else: #exclude the event part
            
        #all_sprite_list.draw(screen)
        
    # draw bg
    draw_bg()
    #draw and update groups items
    item_list.draw(screen)
    item_list.update()
    # update background
    world.draw()

    # show variables
    draw_text('Health: ', font, RED, 10, 35)
    for x in range(player.health):
        screen.blit(heart_img, (70 + (x*20), 40))

    draw_text(f'Coins: {player.score}', font, RED, 10, 55)

    door_list.draw(screen)
    door_list.update()
    exit_list.draw(screen)
    exit_list.update()
    level = exit.update_level()

    player.draw()
    player.update()

    for enemy in enemy_list:
        enemy.ai()
        enemy.draw()
        enemy.update()

    strike_list.draw(screen)
    for item in strike_list:
        item.strikes()
        #item.draw()
    
    bullet_list.draw(screen)
    bullet_list.update()
    decoration_list.draw(screen)
    decoration_list.update()
    #water_list.draw(screen)
    #water_list.update()
    

    trigger_list.draw(screen)
    trigger_list.update()
    #button_press = box.pass_boolean()

    
    if player.alive:
        # show player's animation in different actions
        #print(player.action)
        if shoot:
            player.shoot_bullet()
            if player.shoot_cooldown > 0:
                player.update_action(3) #shoot
        
        elif player.inair:
            player.update_action(2) # Jump
        elif player_move_left or player_move_right:
            player.update_action(1) # Run
            #player.update_action(3)
        else:
            player.update_action(0) # Idle
        
        screen_scroll = player.Movement(player_move_left, player_move_right)
        #print(screen_scroll)
        bg_scroll -= screen_scroll
        #print(bg_scroll)

        
    for event in pygame.event.get():
        # QUIT Game
        if event.type == pygame.QUIT:
            run = False
        # Keydown
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_move_left = True
            if event.key == pygame.K_d:
                player_move_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == K_w and player.alive:
                player.jump = True
            if pygame.sprite.collide_rect(lever, player):
                if event.key == pygame.K_t:
                    lever.turn()

        # Button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player_move_left = False
            if event.key == pygame.K_d:
                player_move_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            


            
                


    # --- draw sprites
    #all_sprite_list.draw(screen)
    

    pygame.display.flip()
    
    

pygame.quit()