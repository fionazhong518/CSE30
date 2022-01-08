 
import pygame, os

TILE_SIZE = 32
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

class Door(pygame.sprite.Sprite):
    def __init__(self, img_type, x, y):
        super().__init__()
        self.img_type = img_type
        self.animation_list = []
        self.action = 0
        self.ani_index = 0
        # Load Animation Image
        animation_type = ['default', 'opening', 'closing']
        for animation in animation_type:
            aList = [] # create a temporary list to collect frames of img
            frame_total = len(os.listdir(f'Tileset/{self.img_type}/{animation}'))-1 # new way to count # of files in one folder
            print(frame_total)
            for i in range(frame_total):
                img = pygame.image.load(f"{self.img_type}/{animation}/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*2), int(img.get_height()*2)))
                aList.append(img)
            # update all frames to the specific list within the big list
            self.animation_list.append(aList)
        # img
        self.image = self.animation_list[self.action][self.ani_index]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + TILE_SIZE // 2, y + TILE_SIZE - (self.image.get_height()))
        

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
            self.ani_index = 0

    def update_action(self, new_action):
        # check if the new action is different to the previous one
        if new_action != self.action:
            self.action = new_action
            # reset the variables that are used to update the animation
            self.ani_index = 0
            self.update_time = pygame.time.get_ticks()

    def update(self):
        self.update_animation()
        #self.rect.x += screen_scroll
door_list = pygame.sprite.Group()
door = Door("Door", 32, 32)
door_list.add(door) 
run = True
while run:

    
    clock.tick(60)
    
    screen.fill(WHITE)
    door_list.draw(screen)
    door_list.update()
    for event in pygame.event.get():
        # QUIT Game
        if event.type == pygame.QUIT:
            run = False
"""
        ### 0-Idle
        aList = [] # create a temporary list to collect frames of img
        for i in range(12):
            img = pygame.image.load(f"{self.char_type}/Idle/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
            aList.append(img)
        self.animation_list.append(aList)
        ### 1- Run
        aList = []
        for i in range(14):
            img = pygame.image.load(f"{self.char_type}/Run/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
            aList.append(img)
        self.animation_list.append(aList)
        ### 2-Jump
        aList = []
        for i in range(9):
            img = pygame.image.load(f"{self.char_type}/Jump/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
            aList.append(img)
        self.animation_list.append(aList)
        ### 3-Shoot
        aList = []
        for i in range(9):
            img = pygame.image.load(f"{self.char_type}/Shoot/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
            aList.append(img)
        self.animation_list.append(aList)
        # add all types of img(small list) to the animation_list (big list)
        self.image = self.animation_list[self.action][self.ani_index]
"""
"""
        aList = []
        for i in range(4):
            img = pygame.image.load(f"Items/Chest/chest_close/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*TILE_SIZE), int(img.get_height()*TILE_SIZE)))
            aList.append(img)
        chest_img.append(aList)
        aList = []
        for i in range(4):
            img = pygame.image.load(f"Items/Chest/chest_open/{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width()*TILE_SIZE), int(img.get_height()*TILE_SIZE)))
            aList.append(img)
"""