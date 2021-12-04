'''
def f():
    print("Hello")
    f()
 
f()
 
def g():
    print("g")
'''
def f(level):
    # Print the level we are at
    print("Recursion call, level",level)
    # If we haven't reached level ten...
    if level < 10:
        # Call this function again
        # and add one to the level
        f(level+1)
 
# Start the recursive calls at level 1
#f(1)

# This program calculates a factorial
# WITHOUT using recursion
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        answer = answer * i
    return answer

# This program calculates a factorial
# WITH recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)

'''Example of Factorial Calculator'''
# This program calculates a factorial
# WITHOUT using recursion
 
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        print(i, "*", answer, "=", i * answer)
        answer = answer * i
    return answer
 
print("I can calculate a factorial!")
user_input = input("Enter a number:")
n = int(user_input)
answer = factorial_nonrecursive(n)
print(answer)
 
# This program calculates a factorial
# WITH recursion
 
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        x = factorial_recursive(n - 1)
        print( n, "*", x, "=", n * x )
        return n * x
 
print("I can calculate a factorial!")
user_input = input("Enter a number:")
n = int(user_input)
answer = factorial_recursive(n)
print(answer)


"""
 Recursively draw rectangles.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
import pygame
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
 
def recursive_draw(x, y, width, height):
    """ Recursive rectangle function. """
    pygame.draw.rect(screen, BLACK,
                     [x, y, width, height],
                     1)
 
    # Is the rectangle wide enough to draw again?
    if(width > 14):
        # Scale down
        x += width * .1
        y += height * .1
        width *= .8
        height *= .8
        # Recursively draw again
        recursive_draw(x, y, width, height)
 
pygame.init()
 
# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # Set the screen background
    screen.fill(WHITE)
 
    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    recursive_draw(0, 0, 700, 500)
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()