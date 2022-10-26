from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.score = 0
        self.write(f'Score = {self.score}', align = "left", font = FONT)

    def increase_score(self):
        self.score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f'Score = {self.score}', align="left", font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write('Game over', align="Center", font=FONT)
