# Space Shooter by Mr. V (borrowed/modified from programarcadegames.com)

import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('Space Shooter')

clock = pygame.time.Clock()

# Load and set up graphics.
background_image = pygame.image.load("saturn_family1.jpg")
player_image = pygame.image.load("player.png")

# Main Program Function


def main():
    # Laser Variables
    laser_x = 300
    laser_y = -400

    # Timer variable
    frame_count = 0
    can_shoot = True
    shoot_frame = 0

    # Player Invisibility
    draw_player = True
    invisible_frame = 0

    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if draw_player:
                    draw_player = False
                    invisible_frame = frame_count

                if can_shoot:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    laser_x = mouse_x + 45
                    laser_y = mouse_y
                    can_shoot = False
                    shoot_frame = frame_count

        # Move Laser
        laser_y += -5

        # Check laser cooldown
        if can_shoot == False and frame_count - shoot_frame > 120:
            can_shoot = True

        # Check invisibility cooldown
        if draw_player == False and frame_count - invisible_frame > 120:
            draw_player = True

        # Increment frameCount
        frame_count += 1

        # Copy image to screen:
        screen.blit(background_image, [0, 0])

        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw laser
        pygame.draw.rect(screen, RED, [laser_x, laser_y, 10, 40])

        # Copy image to screen:
        if draw_player:
            screen.blit(player_image, [mouse_x, mouse_y])

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
# end main()


# Call main to begin program
main()