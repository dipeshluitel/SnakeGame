from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            past_high_score = int(file.read())
        self.highscore = past_high_score
        self.score = 0
        self.hideturtle()
        self.penup()

    def display_score(self):
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.write(f"SCORE : {self.score}\t\tHighScore : {self.highscore} ", move=False, align='center',
                   font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.display_score()
