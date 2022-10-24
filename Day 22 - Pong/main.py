import turtle
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

x_bound = 800
y_bound = 600

screen = Screen()
screen.bgcolor("black")

screen.setup(width=x_bound, height=y_bound)
screen.title('Pong')
scoreboard = Scoreboard()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if abs(ball.ycor()) >= (y_bound/2) - 20 or abs(ball.xcor()) >= (x_bound/2) - 20:
        ball.bounce_y()

    #Detech collision with paddle\
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < - 320:
        ball.bounce_x()
    #Detect hitting right wall
    if ball.xcor() > 380:
        ball.setposition(0,0)
        ball.bounce_x()
        scoreboard.l_point()
    #Detect hitting left wall
    if ball.xcor() < - 380:
        ball.setposition(0, 0)
        ball.bounce_x()
        scoreboard.r_point()
    scoreboard.update_scoreboard()







turtle.exitonclick()