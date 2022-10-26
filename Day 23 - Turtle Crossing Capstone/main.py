import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

turtle = Player()
cars = []
scoreboard = Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(turtle.move, "Up")

    if random.randint(0,10) == 1:
        car = CarManager()
        cars.append(car)
    for car in cars:
        car.move()
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.ycor() > 280:
        turtle.refresh()
        scoreboard.increase_score()
        for car in cars:
            car.increase_speed()

screen.exitonclick()

