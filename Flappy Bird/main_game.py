"""
Name: Igloo Shuttle
author: Fiona Zhong
date created: 2022-01-09
"""

import pygame, os, csv, button,random
from pygame.locals import *
from pygame import mixer

pygame.init()
mixer.init()

clock = pygame.time.Clock()

# game setup
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 544
TILE_SIZE = 32#SCREEN_HEIGHT // ROWS
TILE_TYPES = 28
ROWS = 20
COL = 640

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')


#define game variables
GRAVITY = 0.5
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ground_scroll = 0
scroll_speed = 0
flying = False
shoot = False
start_game = False
game_over = False
start_intro = False

# ----- load font
pygame.font.init()
font = pygame.font.SysFont('Futura', 15)
# --------------- load sounds
pygame.mixer.music.load('sound/bg_music.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
strike_fx = pygame.mixer.Sound('sound/pop.wav')
strike_fx.set_volume(0.5)
collect_fx = pygame.mixer.Sound('sound/collect2.wav')
collect_fx.set_volume(0.5)
heal_fx = pygame.mixer.Sound('sound/heal.wav')
heal_fx.set_volume(0.5)
hit_fx = pygame.mixer.Sound('sound/spring.wav')
hit_fx.set_volume(0.5)
shoot_fx = pygame.mixer.Sound('sound/shoot.wav')
shoot_fx.set_volume(0.5)
#---------------load images
# buttons
restart_img = pygame.image.load('restart.png')
quit_img = pygame.image.load('quit_btn.png')
start_img = pygame.image.load('start_btn.png')
again_img = pygame.image.load('again_btn.png')

# text image
title_img = pygame.image.load('Title.png').convert_alpha()
title_img = pygame.transform.scale(title_img, (title_img.get_width()-180, title_img.get_height()-180))
win_img = pygame.image.load('win_text.png').convert_alpha()
win_img = pygame.transform.scale(win_img, (win_img.get_width()//2, win_img.get_height()//2))
lose_img = pygame.image.load('lose_text.png').convert_alpha()
lose_img = pygame.transform.scale(lose_img, (lose_img.get_width()//3*2, lose_img.get_height()//3*2))

# background
bg_colour = (127, 189, 232)
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
snowman_img = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f'tileset/{x}.png').convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)
    if x >=15 and x <=17:
        decoration_img.append(img)
    if x == 18:
        snowman_img.append(img)
    if x >= 19 and x <= 21:
        strike_img.append(img)
    if x == 23:
        sign_img.append(img)
    
# --------- load img into different classes
heart_img = []
for i in range(3):
    img = pygame.image.load(f"heart/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    heart_img.append(img)
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
item_dict = {
    'coin' : coin_img,
    'heart': heart_img,
    'sign': sign_img
}
# bullet
bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (TILE_SIZE//2, TILE_SIZE//2))
# create snow
snow_list = []
for i in range(300):
    x = random.randrange(0, SCREEN_WIDTH)
    y = random.randrange(-100, 0)
    snow_list.append([x, y])
# ----------- draw text and bg ----------- #
def draw_bg():
    screen.fill(bg_colour)
    screen.blit(bg_img, (0, 0))
    screen.blit(cloud1_img, (ground_scroll+SCREEN_WIDTH, 100))
    screen.blit(cloud2_img, (ground_scroll+SCREEN_WIDTH+300, 60))
    screen.blit(cloud2_img, (ground_scroll+SCREEN_WIDTH+400, 120))

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))

def draw_snow():
    # draw snow
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1 # move y down
        # check off screen
        if snow_list[i][1] > SCREEN_HEIGHT//3:
            # recreate random snow flakes
            x = random.randrange(0, SCREEN_WIDTH)
            y = random.randrange(-100, -1)
            snow_list[i][0] = x
            snow_list[i][1] = y

def reset_game():
    decoration_list.empty()
    strike_list.empty()
    blade_list.empty()
    item_list.empty()
    sign_list.empty()
    bat_list.empty()
    snowman_list.empty()
    enemy_list.empty()
    player_list.empty()
    bullet_list.empty()
    # create empty tile list
    data = []
    for row in range(ROWS):
        r = [-1] * COL
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
                    if tile >= 0 and tile <= 14:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 15 and tile <= 17:
                        decoration = Decoration(img, x * TILE_SIZE, y * TILE_SIZE)
                        decoration_list.add(decoration)
                    elif tile  == 18: #snowman
                        snowman = Figure('snowman', x * TILE_SIZE, y * TILE_SIZE, 0, 1)
                        snowman_list.add(snowman)
                        enemy_list.add(snowman)
                    elif tile == 19: #strikes
                        strike = Obstacle(img,'up_strike', x * TILE_SIZE, y * TILE_SIZE)
                        strike_list.add(strike)
                    elif tile == 20:
                        strike = Obstacle(img,'down_strike', x * TILE_SIZE, y * TILE_SIZE)
                        strike_list.add(strike)
                    elif tile == 21:
                        strike = Obstacle(img,'left_strike', x * TILE_SIZE, y * TILE_SIZE)
                        strike_list.add(strike)
                    elif tile == 22: #bat
                        bat = Figure('bat', x * TILE_SIZE, y * TILE_SIZE, -3, 0.8)
                        bat_list.add(bat)
                        enemy_list.add(bat)
                    elif tile == 23: # sign
                        sign = Item('sign', x * TILE_SIZE, y * TILE_SIZE)
                        sign_list.add(sign)
                    elif tile == 24: #coin
                        coin = Item('coin', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(coin)
                    elif tile == 25: # blade
                        blade = Obstacle(blade_img,'blade', x * TILE_SIZE, y * TILE_SIZE)
                        blade_list.add(blade)
                    elif tile == 26: #player
                        player = Figure('player',100, SCREEN_HEIGHT//2, 3, 1.2)
                        player_list.add(player)
                    elif tile == 27:
                        heart = Item('heart', x * TILE_SIZE, y * TILE_SIZE)
                        item_list.add(heart)

        return player, strike
    def draw(self):
        for tile in self.obstacle_list:
            tile[1][0] += scroll_speed
            screen.blit(tile[0], tile[1])
        #print(ground_scroll)

class Decoration(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))

    def update(self):
        self.rect.x += scroll_speed # scroll the world map

class Figure(pygame.sprite.Sprite):
    def __init__(self,cha_type, x, y, speed, scale):
        super().__init__()
        self.cha_type = cha_type
        self.animation_list = []
        self.action = 0
        self.ani_index = 0
        self.counter = 0

        # Load animation image #
        if self.cha_type != 'snowman':
            if self.cha_type == 'player':
                animation_type = ['fly','fall','dead']
            elif self.cha_type == 'bat':
                animation_type = ['fly','dead']
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
        else:
            self.image = snowman_img[0] # the snowman doesn't have animation
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        if self.cha_type != 'player':
            self.rect.center = [x + self.width//2, y+self.height//2]
        else:
            self.rect.center = [x, y]
        

        # movement and shooting
        self.speed = speed
        self.velocity_y = 0
        self.clicked = False
        self.fall = False
        self.shoot_cooldown = 0
        self.shooting = False

        # lives and score
        self.alive = True
        self.live = 15
        self.max_live = 15
        self.score = 0

        # variables for enemies only
        if cha_type == 'snowman':
            self.direction = -1
        else:
            self.direction = 1
        self.idling = True
        self.vision = pygame.Rect(0, 0, 250, 50)
        self.attack_cooldown = 0

    def update(self):
        if self.cha_type != 'snowman':
            self.update_animation()
        self.check_alive()
        # set the shooting cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def movement(self):
        scroll_speed = 0
        # reset direction variables
        dx = 0
        dy = 0
        # fall
        if self.cha_type == 'player':
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

            dy += self.velocity_y

        # enemy movement
        if self.cha_type == 'bat':
            dx = self.speed
            dy = 0
        else:
            dx = 0

        level_complete = False
        if pygame.sprite.spritecollide(self, sign_list, False):
            level_complete = True
        # update scrolling 
        if self.cha_type == 'player':
            scroll_speed = -self.speed

        # check collision with the obstables
        if pygame.sprite.spritecollide(self, strike_list, False) or pygame.sprite.spritecollide(self, blade_list, False):
            scroll_speed = 0
        for blade in blade_list:
            if blade.rect.collidepoint(self.rect.midright):
                scroll_speed = 0
            if blade.rect.collidepoint(self.rect.midtop):
                self.velocity_y = 0
                dy = blade.rect.bottom - self.rect.top
                self.clicked = False
            if blade.rect.collidepoint(self.rect.midbottom):
                self.velocity_y = 0
                dy = blade.rect.top - self.rect.bottom
                self.fall = False
        for strike in strike_list:
            if strike.rect.collidepoint(self.rect.midright):
                scroll_speed = 0
            if strike.rect.collidepoint(self.rect.midtop):
                self.velocity_y = 0
                dy = strike.rect.bottom - self.rect.top
                self.clicked = False
            if strike.rect.collidepoint(self.rect.midbottom):
                self.velocity_y = 0
                dy = strike.rect.top - self.rect.bottom
                self.fall = False
        
        # check if hit the wall
        for tile in world.obstacle_list:
            # check in horizontal direction
            if tile[1].collidepoint(self.rect.midright):
                scroll_speed = 0
            
            # check in vertical direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if tile[1].collidepoint(self.rect.midtop):# top collision
                    self.velocity_y = 0
                    dy = tile[1].bottom - self.rect.top
                    self.clicked = False

                elif tile[1].collidepoint(self.rect.midbottom): # bottom collision
                    self.velocity_y = 0
                    dy = tile[1].top - self.rect.bottom
                    self.fall = False
            if self.cha_type == 'bat':
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    self.speed = 0
                    #self.kill()
        # update position
        self.rect.x += dx
        self.rect.y += dy
 
        return scroll_speed, level_complete

    def bat(self):
        if self.idling == True:
            self.update_action(0) #fly
            self.speed = 0
        if self.alive and player.alive:
            if self.vision.colliderect(player.rect):
                self.idling = False
                self.speed = -3
            if self.idling == False:
                self.movement() #
                if self.rect.colliderect(player.rect):
                    self.attack()
            # create a rect to monitor if the player approaches
            self.vision.center = (self.rect.x - self.width*3, self.rect.centery)
            #pygame.draw.rect(screen, RED, self.vision)
        elif self.alive == False:
            self.update_action(1) # dead
        # scrolling
        self.rect.x += scroll_speed
            
    def attack(self):
        if player.alive:
            if self.attack_cooldown == 0:
                self.attack_cooldown = 10
                player.live -= 1
                hit_fx.play()
            if self.attack_cooldown > 0:
                self.attack_cooldown -= 1

    def snowman(self):
        # create a rect to monitor if the player approaches
        self.vision.center = (self.rect.x - self.width*3, self.rect.centery)
        #pygame.draw.rect(screen, RED, self.vision)

        if self.alive and player.alive:
            if self.vision.colliderect(player.rect):
                #self.idling = False
                self.shoot()
            
        # update scrolling
        self.rect.x += scroll_speed      
    def shoot(self):
        # this function would only run if the SPACE is pressed
        if self.shoot_cooldown == 0:
            self.shoot_cooldown = 15

            bullet = Bullet(self.rect.centerx + 25* self.direction, self.rect.centery + 5, self.direction)
            bullet_list.add(bullet)
            shoot_fx.play()

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
        animation_cooldown = 20 # speed of frame changes, the higher # the slower

        if self.counter > animation_cooldown:
            self.counter = 0 # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(self.animation_list[self.action]):
                if self.cha_type == 'bat':
                    self.ani_index = 0
                    if self.action == 1:
                        self.ani_index = len(self.animation_list[self.action]) - 1 # stop at the last frame

                else:
                    self.ani_index = len(self.animation_list[self.action]) - 1 # stop at the last frame
         # update image depending on current frame
        self.image = self.animation_list[self.action][self.ani_index]
        
    def check_alive(self):
        if self.live <= 0:
            self.live = 0
            self.speed = 0
            self.alive = False
            if self.cha_type == 'player':
                self.update_action(2) # dead
            elif self.cha_type == 'bat':
                self.update_action(1)

    def draw(self):
        screen.blit(self.image,(self.rect.x, self.rect.y))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 10
        self.direction = direction
        if self.direction < 0:
            self.image = pygame.transform.flip(bullet_img, True, False)
        else:
            self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def update(self):
        # move bullet
        self.rect.x += (self.speed*self.direction) + scroll_speed
        # check if off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
        # hit the player and enemies
        if pygame.sprite.spritecollide(player, bullet_list, False):
            if player.alive:
                player.live -= 1
                hit_fx.play()
                self.kill()
        for enemy in enemy_list:
            if pygame.sprite.spritecollide(enemy, bullet_list, False):
                if enemy.alive:
                    enemy.live -= 4
                    hit_fx.play()
                    self.kill()
                    print(enemy.live)
            
        # check collision with blocks
        for tile in world.obstacle_list:
            if tile[1].colliderect(self.rect):
                self.kill()
        # check collision with characters
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, img,type, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.counter = 0
        self.ani_index = 0
        if self.type == 'blade':
            self.image = img[self.ani_index]
            self.rect = self.image.get_rect()
        else:
            self.image = img
            self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))
        self.hurt_cooldown = 0

    def update(self):
        self.rect.x += scroll_speed # scroll the world map
        if self.type == 'blade':
            self.update_animation()
            
        # set the hurt cooldown
        if self.hurt_cooldown > 0:
            self.hurt_cooldown -= 1
    
    def blade_collide(self):
        if pygame.sprite.collide_rect(self,player) and self.hurt_cooldown == 0:
            self.hurt_cooldown = 20
            player.live -= 1

    def strike_collide(self):
        #player.speed = player.speed
        
        if pygame.sprite.collide_rect(self,player) and self.hurt_cooldown == 0 and player.alive:
            self.hurt_cooldown = 20
            if self.type == 'up_strike':
                if player.rect.collidepoint(self.rect.midtop):
                    player.live -= 1
                    strike_fx.play()
                
            if self.type == 'down_strike':
                if self.rect.collidepoint(player.rect.midtop):
                    player.live -= 1
                    strike_fx.play()


            if self.type == 'left_strike':
                if self.rect.collidepoint(player.rect.midright):
                    player.live -= 1
                    strike_fx.play()
 
    def update_animation(self):
        # animation
        self.counter += 10
        animation_cooldown = 50 # speed of frame changes, the higher # the slower

        if self.counter > animation_cooldown:
            self.counter = 0 # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(blade_img):
                self.ani_index = 0
        # update image depending on current frame
        self.image = blade_img[self.ani_index]

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Item(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        self.action = 0
        self.ani_index = 0
        self.counter = 0
        self.image = item_dict[type][self.ani_index]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE //2, y )

    def update(self):
        self.rect.x += scroll_speed

        #functionality
        if self.type != 'sign': 
            self.update_animation()
        if pygame.sprite.collide_rect(self, player):
            if self.type == 'coin':
                player.score += 1
                collect_fx.play()
                self.kill()
            if self.type == 'heart':
                player.live += 1
                heal_fx.play()
                if player.live >= player.max_live:
                    player.live = player.max_live
                self.kill()
    
    def update_animation(self):
        # animation
        self.counter += 10
        animation_cooldown = 20 # speed of frame changes, the higher # the slower

        if self.counter > animation_cooldown:
            self.counter = 0 # reset the timer
            self.ani_index = self.ani_index + 1 # pop to the next img

            # aviod animation list run out of the range (back to the start)
            if self.ani_index >= len(item_dict[self.type]):
                self.ani_index = 0
        # update image depending on current frame
        self.image = item_dict[self.type][self.ani_index]

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class ScreenFade(pygame.sprite.Sprite):
    def __init__(self, direction, colour, speed):
        self.direction = direction
        self.colour = colour
        self.speed = speed
        self.fade_counter = 0

    def fade(self):
        fade_complete = False
        self.fade_counter += self.speed
        if self.direction == 1: # whole screen fade
            pygame.draw.rect(screen, self.colour, (0 - self.fade_counter, 0, SCREEN_WIDTH//2, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (SCREEN_WIDTH//2 + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, 0 - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT//2))
            pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT//2 + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))

        if self.direction == 2: # vertical screen fade down
            pygame.draw.rect(screen, self.colour, (0, 0, SCREEN_WIDTH, 0 + self.fade_counter))
        if self.direction == 3:
            pygame.draw.rect(screen, self.colour, (SCREEN_WIDTH - self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (-SCREEN_WIDTH + self.fade_counter, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, -SCREEN_HEIGHT + self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))
            pygame.draw.rect(screen, self.colour, (0, SCREEN_HEIGHT - self.fade_counter, SCREEN_WIDTH, SCREEN_HEIGHT))

        if self.direction != 3:
            if self.fade_counter >= SCREEN_WIDTH:
                fade_complete = True
        else:
            if self.fade_counter >= SCREEN_WIDTH//2:
                fade_complete = True
        #print(fade_complete)
        return fade_complete

# create screen fades
intro_fade = ScreenFade(1, BLACK, 6)
death_fade = ScreenFade(2, BLACK, 6)
win_fade = ScreenFade(3, BLACK, 6)

# create buttons
start_btn = button.Button(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2+100, start_img, 3)
quit_btn = button.Button(SCREEN_WIDTH//2 + 50, SCREEN_HEIGHT//2+100, quit_img, 3)
restart_btn = button.Button(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2+100, restart_img, 1)
again_btn = button.Button(SCREEN_WIDTH//2 - 150, SCREEN_HEIGHT//2+100, again_img, 3)

# ----------- create sprite groups --------- #
decoration_list = pygame.sprite.Group()
strike_list = pygame.sprite.Group()
blade_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()
sign_list = pygame.sprite.Group()
bat_list = pygame.sprite.Group()
snowman_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

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
    screen.fill(bg_colour)

    if start_game == False:
        screen.blit(title_img, (SCREEN_WIDTH//2 - title_img.get_width()//2, SCREEN_HEIGHT//3 - 50))
        # create buttons
        if start_btn.draw(screen):
            start_game = True
            start_intro = True
        if quit_btn.draw(screen):
            run = False

    if start_game == True:
        #draw background
        draw_bg()
        world.draw()
        # draw text
        live_img = heart_img[0]
        live_img = pygame.transform.scale(live_img, (TILE_SIZE//2, TILE_SIZE//2))
        draw_text('Your Lives: ',font, WHITE, 10, 20)
        screen.blit(live_img, (100, 20))
        draw_text( f'x {player.live}', font, WHITE, 120, 20)

        # draw sprites
        player.draw()
        player.update()

        decoration_list.draw(screen)
        decoration_list.update()

        bullet_list.draw(screen)
        bullet_list.update()
        for snowman in snowman_list:
            snowman.snowman()
            snowman.update()
            snowman.draw()
        for bat in bat_list:
            bat.update()
            bat.bat()
            bat.draw()
        for strike in strike_list:
            strike.update()
            strike.strike_collide()
            strike.draw()
            
        for blade in blade_list:
            blade.update()
            blade.blade_collide()
            blade.draw()

        item_list.draw(screen)
        item_list.update()

        sign_list.draw(screen)
        sign_list.update()
    # intro fade
    if start_intro:
        if intro_fade.fade():
            start_intro = False
            intro_fade.fade_counter = 0 # set back to 0 so we can run it again

    # player's action
    if player.alive and game_over == False:
        scroll_speed, level_complete = player.movement()
        if shoot:
            player.shoot()

        if player.clicked:
            player.update_action(0) # fly
        elif player.clicked == False and player.fall == True:
            player.update_action(1) # fall

        # update scrolling
        ground_scroll = -scroll_speed
        if abs(ground_scroll) > 5:
            ground_scroll = 5

        # complete the game
        if level_complete:
            scroll_speed = 0
            game_over = True
            #world_data = reset_game()
                    
    if player.alive == False:
        scroll_speed = 0
        game_over = True
        flying = False
        player.update_action(2) # dead

    # defeat
    if player.alive == False and game_over == True: 
        scroll_speed = 0
        if death_fade.fade():
            screen.blit(lose_img, (SCREEN_WIDTH//2 - lose_img.get_width()//2, SCREEN_HEIGHT//3-50))
            draw_text(f'Your Coins:{player.score}', font, bg_colour, SCREEN_WIDTH//2-50, SCREEN_HEIGHT-200)
            if restart_btn.draw(screen):
                death_fade.fade_counter = 0
                start_intro = True
                level_complete = False
                game_over = False
                pygame.mixer.music.play(-1, 0.0, 5000)
                world_data = reset_game()
                #load in level data and create world
                with open('level0_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)

                world = World()
                player, strike = world.process_data(world_data)
            if quit_btn.draw(screen):
                run = False
    # win
    if level_complete and game_over:
        if win_fade.fade():
            screen.fill(BLACK)
            draw_snow()   
            # print text
            screen.blit(win_img, (SCREEN_WIDTH//2 - win_img.get_width()//2, SCREEN_HEIGHT//3))
            draw_text(f'Your Coins:{player.score}', font, bg_colour, SCREEN_WIDTH//2-50, SCREEN_HEIGHT-200)
            
            if again_btn.draw(screen):
                win_fade.fade_counter = 0
                start_intro = True
                level_complete = False
                game_over = False
                pygame.mixer.music.play(-1, 0.0, 5000)
                world_data = reset_game()
                #load in level data and create world
                with open('level0_data.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',')
                    for x, row in enumerate(reader):
                        for y, tile in enumerate(row):
                            world_data[x][y] = int(tile)

                world = World()
                player, strike = world.process_data(world_data)
            if quit_btn.draw(screen):
                run = False
    #print(player.alive)
    '''
    #print(scroll_speed)
    # check for gameover and reset
    if game_over == True:
        restart_btn.draw()
    '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flying == False and game_over == False:
                flying = True
        # key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot = True

        # key release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shoot = False

    pygame.display.update()

pygame.quit()