import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)



tim = Turtle()
tim.shape('turtle')
tim.color('cyan')
tim.speed('fastest')


loops = 100
angle = 360/loops

for i in range(loops):
    tim.color(random_color())
    tim.circle(100)
    tim.right(angle)

screen = Screen()
screen.exitonclick()