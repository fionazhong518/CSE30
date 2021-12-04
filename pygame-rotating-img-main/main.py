import pygame
import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 600])

car_img = pygame.image.load("police-car.png")  # 150 x 75
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Calculate angle based on mouse position
    mouseX, mouseY = pygame.mouse.get_pos()
    angle = math.degrees(math.atan2(-(mouseY - 137), mouseX - 175))
    print(angle)

    # animate angle
    # angle += 1
    # print(angle)

    # Rotate using rotozoom()
    rotated_img = pygame.transform.rotozoom(car_img, angle, 1)
    rotated_rect = rotated_img.get_rect(center=(175, 137))

    # # Rotate using rotate()
    # rotated_img2 = pygame.transform.rotate(car_img, angle)
    # rotated_rect2 = rotated_img.get_rect(center=(375, 137))

    # Draw
    screen.fill((255, 255, 255))

    # pygame.draw.rect(screen, [0, 0, 255], rotated_rect)
    # screen.blit(car_img, [100, 100])
    screen.blit(rotated_img, rotated_rect)

    # screen.blit(car_img, [300, 100])
    # screen.blit(rotated_img2, rotated_rect2)

    pygame.display.flip()
    clock.tick(60)
