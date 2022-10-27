from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.draw_score()

    def draw_score(self):
        self.color('white')
        self.ht()
        self.penup()
        self.setposition(0, 270)
        self.write(f"Score: {self.score}", move=False, align='center', font=('Calibri', 11, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game over", move=False, align='center', font=('Calibri', 20, 'normal'))
        
    def increase_score(self):
        self.reset()
        self.score += 1
        self.draw_score()
        print(f'Score increased to {self.score}!')