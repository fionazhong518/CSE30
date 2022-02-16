# Turtle graphic in Pygame

import turtle, random

"""
tim = turtle.Turtle()

tim.color('red')
tim.pensize('5') # pen size
tim.shape('turtle') # arrow, circle, turtle

tim.forward(100) # move forward by 100 pixel
tim.left(90) # turn left by 90 degrees
tim.penup()

tim.forward(100) # pixels
tim.right(90)

tim.pendown()
tim.color('green')
tim.forward(100)

dave = turtle.Turtle()
dave.color('blue')
dave.pensize(20)

dave.backward(100)
dave.speed(1) #higher laster
"""

"""
tim = turtle.Turtle()
colors = ['red','blue', 'green', 'purple', 'yellow', 'orange', 'black']
# set colors for turtle
tim.color('red', 'blue')

# set pen width
tim.width(5)

#fill in shape with color
tim.begin_fill()
tim.circle(50) # only one for circle
tim.end_fill() # filled in blue when finish drawing

tim.penup()
tim.forward(150)
tim.pendown()

tim.color('yellow', 'black') # draw yellow, fill black
tim.begin_fill()
for x in range(4):
    tim.forward(100)
    tim.right(90)
tim.end_fill()

for x in range(5):
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor])
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    tim.penup()
    tim.setpos(rand1, rand2) # move left and down
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0, 80))
    tim.end_fill()
"""

"""
# draw turtle line based on key pressing and mouse click
tim = turtle.Turtle()
colors = ['red','blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    tim.setheading(90) # face north
    tim.forward(100) # go 100 pivels

def down():
    tim.setheading(270) # face south
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

def clickleft(x, y):
    # change the color
    tim.color(random.choice(colors)) # select radom items from a list 

def clickright(x, y):
    tim.stamp()

turtle.listen()

# click anywhere on the screen, so onscreenclick
turtle.onscreenclick(clickleft, 1) # 1 = left mouse buttom
turtle.onscreenclick(clickright, 2) # 1 = left mouse buttom, 2 = right buttom, 3 = middle buttom

# determine what key to hit
turtle.onkey(up, 'Up') # activate up() base on 'up'key
turtle.onkey(down, 'Down') # activate () base on 'down'key
turtle.onkey(left, 'Left') # activate () base on '<--'key
turtle.onkey(right, 'Right') # activate () base on '-->'key

turtle.mainloop() # program would close if not be called
"""
from turtle import Turtle, Screen
screen = Screen()
t = Turtle("turtle")
t.speed(-1) # speed

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y)) # set direction pointing towards the mouse obj
    t.goto(x, y)
    t.ondrag(dragging) # continue to drag? keep calling this function

def clickright(x, y): # need x and y parameters
    t.clear() # clear the screen

def main():
    turtle.listen() # listen for any mouse/key events

    t.ondrag(dragging) # pass in x/y value and drag

    turtle.onscreenclick(clickright, 2) # right mouse buttom

    screen.mainloop() # keep running the functions untill right click

main()