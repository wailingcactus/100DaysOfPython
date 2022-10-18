from turtle import Screen, Turtle
import time

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.color("white")
            turtle.penup()
            turtle.setposition(x=-20 * i, y=0)
            self.segments.append(turtle)

    def move_snake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)