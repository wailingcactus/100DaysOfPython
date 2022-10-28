from turtle import Turtle

class Label(Turtle):
    def __init__(self, x ,y , state):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(x = x, y = y)
        self.write(f'{state}')

