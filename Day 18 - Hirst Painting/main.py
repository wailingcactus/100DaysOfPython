import random
from color_list import color_list
from turtle import *

tim = Turtle()
tim.hideturtle()
tim.penup()
initial_x = -250
initial_y = -250
tim.setposition(initial_x,initial_y)
tim.speed('fastest')
colormode(255)

for rows in range(1,11):
    for columns in range(10):
        dot_color = (random.choice(color_list))
        tim.dot(20, dot_color)
        tim.forward(50)
    tim.setposition(initial_x,initial_y+50*rows)

screen = Screen()
screen.exitonclick()