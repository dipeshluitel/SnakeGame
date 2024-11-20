from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.hideturtle()
        self.penup()

    def display_score(self):
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.write(f"SCORE : {self.score}\t\tHighScore : {self.highscore} ", move=False, align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.display_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=('arial', 60, 'bold'))
