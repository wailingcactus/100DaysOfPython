from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.seth(180)
        self.goto(280, random.randint(-280,280))
        #Should separate
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        self.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

