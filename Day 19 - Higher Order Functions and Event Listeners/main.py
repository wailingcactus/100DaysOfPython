from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width = 500, height = 400)
bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race?")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles =[]
for i in range(len(colors)):
    new_turtle = Turtle(shape ='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x = -230, y =-100 + i * 50)
    all_turtles.append(new_turtle)

race_on = False

if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= (230):
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You win. {winning_color} wins")
            else:
                print(f"You lose. {winning_color} wins")
            race_on = False

screen.exitonclick()