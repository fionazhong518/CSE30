"""
Name: 
author: Fiona Zhong
date created: 2021-10-13
"""
''' GOALS BY STEPS
1. create player and let it be able to move with buttons
2. let the player be able to shoot 
3. create enemy(computer) class that can shoot automatically (maybe some AI thing?)
4. 
'''
import pygame, random, os, csv, time, button
from pygame import mixer
from pygame.constants import APPACTIVE, DROPCOMPLETE, K_SPACE, KEYDOWN, KEYUP, K_w

mixer.init()
pygame.init()
# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (235, 65, 54)

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
MAX_LEVELS = 3
screen_scroll = 0
bg_scroll = 0
level = 0
start_game = False
start_intro = False

# -- player
player_move_left = False
player_move_right = False
shoot = False
player_shooting = False
lever_turn = False
# --------- LOAD MUSIC AND SOUNDS ---------- #
pygame.mixer.music.load('audiomusic/start_bgm.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1,0.0, 5000 ) #play infinitely, delay, 5 sec
click_sound = pygame.mixer.Sound('audiomusic/clicksound.wav')
click_sound.set_volume(0.5)
collect_sound = pygame.mixer.Sound('audiomusic/collect.wav')
collect_sound.set_volume(0.5)
collect2_sound = pygame.mixer.Sound('audiomusic/collect2.wav')
collect2_sound.set_volume(0.5)
jump_fx = pygame.mixer.Sound('audiomusic/audio_jump.wav')
jump_fx.set_volume(0.5)
shot_fx = pygame.mixer.Sound('audiomusic/pop.wav')
shot_fx.set_volume(0.5)
hit_fx = pygame.mixer.Sound('audiomusic/hit.wav')
hit_fx.set_volume(0.8)
button_fx = pygame.mixer.Sound('audiomusic/button.wav')
button_fx.set_volume(0.5)
lever_fx = pygame.mixer.Sound('audiomusic/lever.wav')
lever_fx.set_volume(0.5)
spring_fx = pygame.mixer.Sound('audiomusic/spring.wav')
spring_fx.set_volume(0.5)
door_fx = pygame.mixer.Sound('audiomusic/door.wav')
door_fx.set_volume(0.5)
strike_fx = pygame.mixer.Sound('audiomusic/strike.wav')
strike_fx.set_volume(0.5)
level_fx = pygame.mixer.Sound('audiomusic/level_up.wav')
level_fx.set_volume(0.5)


# ------------------------- LOAD IMAGES ---------------------------- #
# background img
bg_1 = pygame.image.load('background/bg_0.png').convert_alpha()
bg_1 = pygame.transform.scale(bg_1, (int(bg_1.get_width()*4), int(bg_1.get_height() *4)))
bg_2 = pygame.image.load('background/bg_1.png').convert_alpha()
bg_2 = pygame.transform.scale(bg_2, (int(bg_2.get_width()*4), int(bg_2.get_height()*4)))
bg_3 = pygame.image.load('background/bg_2.png').convert_alpha()
bg_3 = pygame.transform.scale(bg_3, (int(bg_3.get_width()*4), int(bg_3.get_height()*4)))

# button img
start_img = pygame.image.load('start_btn.png').convert_alpha()
quit_img = pygame.image.load('quit_btn.png').convert_alpha()
again_img = pygame.image.load('again_btn.png').convert_alpha()
gameover_img = pygame.image.load('gameover_sign.png').convert_alpha()
gameover_img = pygame.transform.scale(gameover_img, (gameover_img.get_width()*10, gameover_img.get_height()*10))
# title
title_img = pygame.image.load('title.png').convert_alpha()
title_img = pygame.transform.scale(title_img, (title_img.get_width()*8, title_img.get_height()*8))
win_img = pygame.image.load('wintext.png').convert_alpha()
win_img = pygame.transform.scale(win_img, (win_img.get_width()//3*2, win_img.get_height()//3*2))

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
img = pygame.transform.scale(img, (int(TILE_SIZE*1.5), int(TILE_SIZE)))
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

print(len(img_list))
# -- bullet
bullet_img = pygame.image.load('Bullet.png').convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (int(bullet_img.get_width()*1.2), int(bullet_img.get_height() * 1.2)))

# --------- Load images into different classes -------- #
# -- items and water image (animation)
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
mushroom_img = []
for i in range(6):
    img = pygame.image.load(f'Mushroom/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    mushroom_img.append(img)
woodstep_img = []
img = pygame.image.load('Tileset/decorations/7.png').convert_alpha()
img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
woodstep_img.append(img)
items_dict = {
    'Red_flask' : red_flask_img,
    'Chest' : chest_img,
    'Coin' : coin_img,
    'Key' : key_img,
    'Bottle' : bottle_img,
    'Box' : box_img,
    'Mushroom' : mushroom_img,
    'Strike' : strike_img,
    'Wood' : woodstep_img
}
## water img
river_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/rivers/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE)))
    river_img.append(img)
wave_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/wave/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (int(TILE_SIZE*2), int(TILE_SIZE)))
    wave_img.append(img)

waterfall_img = []
for i in range(3):
    img = pygame.image.load(f'Tileset/waterfall/{i}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, int(TILE_SIZE*2)))
    waterfall_img.append(img)

water_dict = {
    'River' : river_img,
    'Wave' : wave_img,
    'Waterfall' : waterfall_img
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
        screen.blit(bg_2, ((x * width) - bg_scroll * 0.6, 0))
        screen.blit(bg_3, ((x * width) - bg_scroll * 0.6, screen_height - bg_3.get_height()+100))
# function to reset level
def reset_level():
    enemy_list.empty()
    bullet_list.empty()
    item_list.empty()
    decoration_list.empty()
    exit_list.empty()
    door_list.empty()
    woodstep_list.empty()
    box_list.empty()
    water_list.empty()
    waterfall_list.empty()
    button_list.empty()
    lever_list.empty()
    mushroom_list.empty()
    strike_list.empty()

    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COLS
        data.append(r)
    return data
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
                    if tile >= 0 and tile <= 11:
                        self.obstacle_list.append(tile_data)

                    elif tile >= 12 and tile <= 13: # left and right arrow sign
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(decoration)

                    elif tile >= 14 and tile <= 15:# strikes
                        strike = Items('Strike', x * TILE_SIZE, y * TILE_SIZE)
                        strike_list.add(strike)
                    elif tile == 16:# push box
                        box = Items('Box', x * TILE_SIZE, y * TILE_SIZE)
                        box_list.add(box)

                    elif tile == 17: # coin, 
                        coin = Items('Coin', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(coin)                      
                    elif tile == 18: # flask, 
                        red_flask = Items('Red_flask', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(red_flask)
                    elif tile == 19: # treasure box, 
                        chest = Items('Chest', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(chest)
                    elif tile == 20: # bottle, 
                        bottle = Items('Bottle', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(bottle)
                    elif tile == 21: # sign, 
                        sign = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(sign)
                    elif tile == 22: # key
                        key = Items('Key', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(key)

                    elif tile == 23:# lever
                        lever = Trigger('Lever', x * TILE_SIZE, y * TILE_SIZE)
                        lever_list.add(lever) 
                    elif tile == 24:# player                       
                        player = Figure('player', x * TILE_SIZE, y * TILE_SIZE, 2, 5, 50)
                        #all_sprite_list.add(player)

                    elif tile == 25:# enemies
                        trunk = Figure('Trunk', x * TILE_SIZE, y * TILE_SIZE, 1, 2, 50)
                        enemy_list.add(trunk)
                    elif tile == 26:
                        mushroom = Items('Mushroom', x * TILE_SIZE, y * TILE_SIZE)
                        mushroom_list.add(mushroom)
                    elif tile == 27:
                        goblin = Figure('Goblin', x * TILE_SIZE, y * TILE_SIZE, 2, 2, 70)
                        enemy_list.add(goblin)
                        
                    elif tile >= 28 and tile <= 29:# decoration grass
                        grass = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(grass) 
                    elif tile >= 30 and tile <= 31:# bloom and not-bloom flower
                        flower = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(flower)
                    elif tile == 32:# root
                        root = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(root) 
                    elif tile == 33:# button
                        button = Trigger('Button', x * TILE_SIZE, y * TILE_SIZE)
                        button_list.add(button) 
                    elif tile == 35: # woodstep
                        woodstep = Items('Wood', x * TILE_SIZE, y * TILE_SIZE)
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
                    elif tile == 41:# river, wave and waterfall
                        river = Water('River', x * TILE_SIZE, y * TILE_SIZE)
                        water_list.add(river)
                    elif tile == 42:
                        wave = Water('Wave', x * TILE_SIZE, y * TILE_SIZE)
                        water_list.add(wave)
                    elif tile == 43:
                        waterfall = Water('Waterfall', x * TILE_SIZE, y * TILE_SIZE)
                        waterfall_list.add(waterfall)
                    elif tile == 44:
                        pass
        if level == 1:
            return player, button, box, exit, strike
        elif level == 0:
            return player, box, woodstep, strike, lever
        else:
            return player, button, lever, box, exit, woodstep, strike
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
        self.player_collide = False
        
    def update(self):
        self.rect.x += screen_scroll
        # functionality
        if self.type == 'Button':
            self.press()
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - player.height
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
            #self.turn()
            if self.turning:
                self.update_action(1)
            else:
                self.update_action(0)
        #print(self.turning)

    def turn(self):    
        
        if pygame.sprite.collide_rect(self, player) or pygame.sprite.collide_rect(self, enemy):
            if not self.turning:
                self.turning = True
                lever_fx.play()
            else:
                self.turning = False
                lever_fx.play()
        

    def press(self):
        
        if pygame.sprite.collide_rect(self, player) or pygame.sprite.collide_rect(self, enemy) \
            or pygame.sprite.collide_rect(self, box):
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

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += screen_scroll # scroll the world map

class Water(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = item_type
        self.ani_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = water_dict[item_type][self.ani_index]

        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE, y + TILE_SIZE - (self.image.get_height()))
        if self.type == 'Waterfall':
            self.rect.midtop = (x + TILE_SIZE-15, y + TILE_SIZE - (self.image.get_height()//2))

    def update(self):
        self.rect.x += screen_scroll # scroll the world map
        # funtionality
        self.update_animation()
        if pygame.sprite.collide_rect(self, player):
            if self.type == 'River':
                player.health = 0
            elif self.type == 'Wave':
                pass
            elif self.type == 'Waterfall':
                pass

    def update_animation(self):
            animation_cooldown = 150 # speed of frame changes, the higher # the slower

            # update image depending on current frame
            
            self.image = water_dict[self.type][self.ani_index]
            
            # check if enough time has passed since the last update
            #               new time - last updated time > specific cooldown period
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks() # reset the timer
                self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(water_dict[self.type]):
                self.ani_index = 0
            
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Exit(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y )

    def update(self):
        self.rect.x += screen_scroll # scroll the world map
        # funtionality

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
        self.rect.midtop = (x + TILE_SIZE // 2, y )
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        # open
        self.open = False
        self.idle = True

    def update(self):
        self.update_animation()
        #self.collision()
        self.rect.x += screen_scroll
        # open
        self.open = button.press_down

        if self.open:
            #door_fx.play()
            self.update_action(1) # opening
            self.open = False
            self.idle = False
        elif self.open == False and self.idle == False:
            #door_fx.play()
            self.update_action(2)
            if self.ani_index == len(self.animation_list[self.action]):
                self.idle = True
        if self.idle:
            self.update_action(0)
            if pygame.sprite.collide_rect(self, player):
                if self.rect.collidepoint(player.rect.midright):
                    player.rect.x = self.rect.x - player.width
                if self.rect.collidepoint(player.rect.midleft):
                    player.rect.x = self.rect.x + player.width
        
    def collision(self):
        if self.update_action(0):
            if pygame.sprite.collide_rect(self, player):
                if self.rect.collidepoint(player.rect.midright):
                    player.rect.x = self.rect.x - player.width
                if self.rect.collidepoint(player.rect.midleft):
                    player.rect.x = self.rect.x + player.width

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
                if self.char_type == 'worm'or self.char_type == 'Trunk' or self.char_type == 'Goblin':
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
        
        # check if fallen off the map
        if self.rect.bottom > screen_height:
            self.health = 0
            
        # check if off screen
        if self.char_type == 'player':
            if self.rect.left + dir_x < 0 or self.rect.right + dir_x > screen_width:
                dir_x = 0
        # chenck for collision with exit
        level_complete = False
        if pygame.sprite.spritecollide(self, exit_list, False) and self.key:
            level_complete = True

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
            if bg_scroll <= 0:
                bg_scroll == 0
            if screen_scroll <= 0:
                screen_scroll == 0
            #print(self.rect.x, self.rect.y)
            

        return screen_scroll, level_complete # need to return back to the main game


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
            shot_fx.play()

    def attack(self):
        
        self.update_action(3) # Attack
        #print(self.attack_cooldown)
        if player.alive: # if character is alive (player and enemy for now)
            
            if self.attack_cooldown == 0:
                self.attack_cooldown = 30
                player.health -= 1
                hit_fx.play()
                player.update_action(4)
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1   
                
    def ai(self):
        randomnum = int(random.randint(1, 200))
        if self.alive and player.alive:
            if self.idling == False and randomnum == 1: # let the enemy move randomly by picking a random #
                self.update_action(0) # Idle
                self.idling = True
            # check if the player goes into enemy's vision range
            if self.vision.colliderect(player.rect):
                if self.char_type == 'Trunk':
                    self.update_action(3) #attack
                    self.shoot_bullet()
                if self.char_type == 'Goblin' or self.char_type == 'worm':
                    self.Movement(self.ai_moving_left, self.ai_moving_right)
                    self.speed = 2
                    if self.rect.colliderect(player.rect):
                        self.speed = 0
                        self.attack()
                    else:
                        self.Movement(self.ai_moving_left, self.ai_moving_right)
                        self.update_action(1) # run
                else:
                    randomnum = int(random.randint(1, 200)) 
                    self.idling = False
                    #self.update_action(1)
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
            if level == 0 or level == 2 or level == 3:
                if pygame.sprite.collide_rect(self, lever):
                    lever.turning = True
            
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
                hit_fx.play()
                player.health -= 1
                player.update_action(4) #hit
                self.kill() #bullet disappear
        for enemy in enemy_list:
            if pygame.sprite.spritecollide(enemy, bullet_list, False):
                if enemy.alive: # if character is alive (player and enemy for now)
                    hit_fx.play()
                    enemy.health -= 1
                    enemy.update_action(4) #hit
                    self.kill() #bullet disappear

class Items(pygame.sprite.Sprite):
    def __init__(self, item_type, x, y):
        super().__init__()  
        self.type = item_type
        self.action = 0 # for chest only
        self.ani_index = 0
        self.update_time = pygame.time.get_ticks()
        self.image = items_dict[item_type][self.ani_index]

        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - self.image.get_height())

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #box
        self.update_x = 0
        #woodstep
        self.old_pos = self.rect.y
        #mushroom
        self.collide_wood = False
        #strikes
        self.velocity_y = 0
        self.update_y = 0
        self.strike_fall = False
        self.vision = pygame.Rect(0, 0, TILE_SIZE*4, TILE_SIZE*6)
        #box
        self.collide_button = False

    def update(self):
        # scroll
        self.rect.x += screen_scroll # scroll the world map
        self.vision.x += screen_scroll

        # funtionality     
        self.update_animation()
        if self.type == 'Box':
            self.box()
        if self.type == "Mushroom":
            self.mushroom()
        if self.type == 'Strikes':
            self.strikes()
        if self.type == 'Wood':
            self.woodstep()

        # if collide
        if pygame.sprite.collide_rect(self, player):
            # check what kind of item the player meet
            if self.type == 'Red flask':
                player.health += 1
                if player.health == player.max_health:
                    player.health = player.max_health
            elif self.type == 'Chest':
                collect_sound.play()
                player.score += 5
            elif self.type == 'Coin':
                collect_sound.play()
                player.score += 1
            elif self.type == 'Key':
                collect2_sound.play()
                player.key = True
            elif self.type == 'Strike':
                print('hit')
                strike_fx.play()
                player.health -= 1
            for enemy in enemy_list:
                if pygame.sprite.collide_rect(self, enemy):
                    if self.type == 'Strikes':
                        enemy.health -= 1

            # delete the item
            if self.type == 'Chest' or self.type == 'Coin' or self.type == 'Key' or self.type == 'Red flask':
                self.kill()

    def woodstep(self):
        #update_y = 0
        if lever.turning:
            self.update_y = -1
            if self.rect.y + self.update_y <= self.old_pos-(2 * TILE_SIZE):
                self.update_y = 0
        else:
            self.update_y = 1
            if self.rect.y + self.update_y >= self.old_pos:
                self.update_y = 0
            #print(lever.turning)
        self.rect.y += self.update_y

        #collision with player and enemies
        if pygame.sprite.collide_rect(self, player):
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - player.height
                player.inair = False
            else:
                if player.rect.collidepoint(self.rect.midleft):
                    player.rect.x = self.rect.x - player.width
                if player.rect.collidepoint(self.rect.midright):
                    player.rect.x = self.rect.x + player.width
        for enemy in enemy_list:
            if pygame.sprite.collide_rect(self, enemy):
                if self.rect.collidepoint(enemy.rect.midbottom):
                    enemy.rect.y = self.rect.y - enemy.height
                    enemy.inair = False
                #else:
                if enemy.rect.collidepoint(self.rect.midleft):
                    enemy.rect.x = self.rect.x - enemy.width
                if enemy.rect.collidepoint(self.rect.midright):
                    enemy.rect.x = self.rect.x + enemy.width
            
    def strikes(self):
        self.velocity_y += GRAVITY
        self.vision.centerx = self.rect.x
        self.vision.y = self.rect.y
        #pygame.draw.rect(screen, RED, self.vision) #vision range
        if self.vision.colliderect(player.rect):
            print('strike collide')
            self.strike_fall = True
            
        if self.strike_fall:
            if self.velocity_y >= 3:
                self.velocity_y = 3
        else:
            self.velocity_y = 0
        self.update_y = self.velocity_y
       
        # bondaries
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x, self.rect.y + self.update_y, self.width, self.height):
                if self.velocity_y > 0:
                    self.velocity_y = 0
                    self.rect.y = tile[1].top
                if self.rect.bottom == tile[1].top:
                    self.kill()
        #update y location
        self.rect.y += self.update_y     

    def mushroom(self):
        if pygame.sprite.collide_rect(self, player):
            spring_fx.play()
            # bondaries
            if player.rect.collidepoint(self.rect.midleft):
                player.rect.x = self.rect.x - player.width
            if player.rect.collidepoint(self.rect.midright):
                player.rect.x = self.rect.x + player.width
            # spring
            if player.rect.collidepoint(self.rect.midtop):
                player.rect.y = self.rect.y - player.height
                player.velocity_y = -18
        # move up and down as the woodstep moves
        if pygame.sprite.collide_rect(self, woodstep):
            self.collide_wood = True
        if self.collide_wood:
            self.rect.y = woodstep.rect.y - self.height
       
    def box(self):
        self.direction = player.direction# by passing player's direction, the movement of the box would be more fluent
        self.velocity_y += GRAVITY
        update_x = 0
        # collision with the strikes
        for strike in strike_list:
            if pygame.sprite.collide_rect(self, strike):
                    self.rect.y = strike.rect.y - self.height
                    self.velocity_y = 0
        # let the box fall
        self.update_y += self.velocity_y 
        #check collision with the player
        if pygame.sprite.collide_rect(self, player):
            # y direction
            if player.rect.collidepoint(self.rect.midtop):
                player.velocity_y = 0
                player.rect.y = self.rect.y - player.height
                
                player.inair = False
            # x direction
            #else:
                
            elif player.rect.collidepoint(self.rect.midleft) or player.rect.collidepoint(self.rect.topleft):
                player.rect.x = self.rect.x - self.width
                if player_move_right:
                    update_x = player.speed
                    #self.rect.x += player.speed
            elif player.rect.collidepoint(self.rect.midright) or player.rect.collidepoint(self.rect.topright):
                player.rect.x = self.rect.x + self.width
                if player_move_left:
                    update_x = -player.speed
        # check collision with enemies
        for enemy in enemy_list:
            if pygame.sprite.collide_rect(self, enemy):
                if enemy.rect.collidepoint(self.rect.midleft):
                    enemy.rect.x = self.rect.x - self.width
                if enemy.rect.collidepoint(self.rect.midright):
                    enemy.rect.x = self.rect.x + self.width
        
        '''
            if collide_x == True and collide_y == False:
                self.rect.y = self.rect.y
                update_x = self.direction * player.speed
                player.rect.x = self.rect.x - int(player.width * player.direction)
        '''
        '''
            if collide_y == True and collide_x == False: #fix this by using player.inair?
                self.rect.x = self.rect.x
                player.rect.x = player.rect.x
                player.velocity_y = 0
                player.inair = False
                player.rect.y = self.rect.y - player.height

        self.update_y += self.velocity_y
        '''
        
        # check bondaries
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect.x + update_x, self.rect.y, self.width, self.height): # left/right
                #self.rect.x = self.rect.x
                update_x = 0
                self.rect.y = self.rect.y
            elif tile[1].colliderect(self.rect.x, self.rect.y + self.update_y, self.width, self.height):
                #self.rect.x = self.rect.x
                #player.rect.x = self.rect.x - self.width
                if self.velocity_y > 0:
                    self.velocity_y = 0
                    self.update_y = tile[1].top - self.rect.bottom
        

        self.rect.x += update_x
        self.rect.y += self.update_y

    def update_animation(self):
            animation_cooldown = 150 # speed of frame changes, the higher # the slower

            # update image depending on current frame
            
            self.image = items_dict[self.type][self.ani_index]
            
            # check if enough time has passed since the last update
            #               new time - last updated time > specific cooldown period
            if pygame.time.get_ticks() - self.update_time > animation_cooldown:
                self.update_time = pygame.time.get_ticks() # reset the timer
                self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(items_dict[self.type]):
                self.ani_index = 0
            
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class ScreenFade():
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1: # whole screen fade
            pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, screen_width//2, screen_height))
            pygame.draw.rect(screen, self.colour, (screen_width//2 + self.fade_counter, 0, screen_width, screen_height))
            pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, screen_width, screen_height//2))
            pygame.draw.rect(screen, self.colour, (0, screen_height//2 + self.fade_counter, screen_width, screen_height))

        if self.direction == 2: # vertical screen fade down
            pygame.draw.rect(screen, self.colour, (0, 0, screen_width, 0 + self.fade_counter))
        if self.fade_counter >= screen_width:
            fade_complete = True

        return fade_complete


# create screen fades
intro_fade = ScreenFade(1, BLACK, 4)
death_fade = ScreenFade(2, BLACK, 4)
win_fade = ScreenFade(2, BLACK, 4)

# Create button
start_btn = button.Button(screen_width//2 - 200, screen_height//2, start_img, 4)
exit_btn = button.Button(screen_width//2 + 50, screen_height//2, quit_img, 4)
again_btn = button.Button(screen_width//2 - again_img.get_width()*2, screen_height//2 +120, again_img, 4)
exit_btn2 = button.Button(screen_width//2 - 50, screen_height//2 +150, quit_img, 4)

# ------ SPRITES ------ #
#--- sprite group
all_sprite_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()
decoration_list = pygame.sprite.Group()
water_list = pygame.sprite.Group()
exit_list = pygame.sprite.Group()
door_list = pygame.sprite.Group()
button_list = pygame.sprite.Group()
lever_list = pygame.sprite.Group()
strike_list = pygame.sprite.Group()
mushroom_list = pygame.sprite.Group()
woodstep_list = pygame.sprite.Group()
box_list = pygame.sprite.Group()
waterfall_list = pygame.sprite.Group()

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
if level == 1:
    player, button, box, exit, strike = world.process_data(world_data)
elif level == 0:
    player, box, woodstep, strike, lever = world.process_data(world_data)
else:
    player, button, lever, box, exit, woodstep, strike = world.process_data(world_data)
# ---- MAIN PROGRAM LOOP ---- #
run = True
while run:   
    clock.tick(60)
    
    screen.fill(WHITE)
    draw_bg()
    world.draw()
        
    if start_game == False:
        screen.blit(title_img, (screen_width//2 - title_img.get_width()//2, screen_height//3 - 50))
        # add buttons
        if start_btn.draw(screen):
            click_sound.play()
            start_game = True
            start_intro = True
        if exit_btn.draw(screen):
            click_sound.play()
            run = False
    if start_game == True:
        # show variables
        draw_text('Health: ', font, RED, 10, 35)
        for x in range(player.health):
            screen.blit(heart_img, (70 + (x*20), 35))
        draw_text(f'Coins: {player.score}', font, RED, 10, 55)
        draw_text('Key: ', font, RED, 10, 75)
        for x in range(player.key):
            screen.blit(key_img[0], (50, 70))
    # draw different objects
    door_list.draw(screen)
    door_list.update()
    exit_list.draw(screen)
    exit_list.update()
    
    for waterfall in waterfall_list:
        waterfall.draw()
        waterfall.update()

    player.draw()
    player.update()
    
    for enemy in enemy_list:
        enemy.ai()
        enemy.draw()
        enemy.update()
    
    for wood in woodstep_list:
        wood.woodstep()
        wood.update()
        wood.draw()

    for water in water_list:
        water.draw()
        water.update()
        
    item_list.draw(screen)
    item_list.update()
    
    for mushroom in mushroom_list:
        mushroom.mushroom()
        mushroom.update()
        mushroom.draw()

    for item in strike_list:
        item.update()
        item.strikes()
        item.draw()

    for box in box_list:
        box.update()
        box.box()
        box.draw()
    
    for buttons in button_list:
        buttons.press()
        buttons.update()
        buttons.draw()
    
    for lever in lever_list:
        #lever.turn()
        lever.draw()
        lever.update()  
    
    bullet_list.draw(screen)
    bullet_list.update()
    decoration_list.draw(screen)
    decoration_list.update()
    
    # show intro
    if start_intro:
        if intro_fade.fade():          
            start_intro = False
            intro_fade.fade_counter = 0 # complete intro fade, so that we can re run it 

    # update player sction
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
        
        screen_scroll, level_complete = player.Movement(player_move_left, player_move_right)
        
        bg_scroll -= screen_scroll
        #print(bg_scroll)
        # check if player has completed the level
        if level_complete:
            level_fx.play()
            start_intro = True
            level += 1
            bg_scroll = 0
            world_data = reset_level()
            print(level)
            if level <= MAX_LEVELS:
                #load in level data and create world
                with open(f'level{level}_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)

                world = World()
                if level == 1:
                    player, button, box, exit, strike = world.process_data(world_data)
                elif level == 0:
                    player, box, woodstep, strike, lever = world.process_data(world_data)
                else:
                    player, button, lever, box, exit, woodstep, strike = world.process_data(world_data)
        elif level == 4:
            screen_scroll = 0
            if win_fade.fade():
                screen.blit(win_img, (screen_width//2 - win_img.get_width()//2, screen_height//4))
                #world_data = reset_level()
                if exit_btn2.draw(screen):
                    click_sound.play()
                    win_fade.fade_counter = 0 # reset to 0 so we can re run it
                    run = False

    else:
        screen_scroll = 0
        if death_fade.fade():    
            #draw_bg()
            screen.blit(gameover_img, (screen_width//2 - gameover_img.get_width()//2, screen_height//2 - gameover_img.get_height()//2))
            if again_btn.draw(screen):
                click_sound.play()
                death_fade.fade_counter = 0 # reset to 0 so we can re run it
                start_intro = True
                bg_scroll = 0
                world_data = reset_level() #create blank world
                #load in level data and create world
                with open(f'level{level}_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)

                world = World()
                if level == 1:
                    player, button, box, exit, strike = world.process_data(world_data)
                elif level == 0:
                    player, box, woodstep, strike, lever = world.process_data(world_data)
                else:
                    player, button, lever, box, exit, woodstep, strike = world.process_data(world_data)

    
    for event in pygame.event.get():
        # QUIT Game
        if event.type == pygame.QUIT:
            run = False
        if start_game == True:
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
                    jump_fx.play()     
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