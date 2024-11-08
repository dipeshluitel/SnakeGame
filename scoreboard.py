from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def display_score(self, score):
        self.clear()
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.write(f"SCORE : {score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=('arial', 60, 'bold'))
