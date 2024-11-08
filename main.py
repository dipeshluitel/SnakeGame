import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


snake = Snake()
food = Food()
score = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
points = 0
score.display_score(points)
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 20:
        points = points+1
        food.new_coordinate()
        score.display_score(points)

screen.exitonclick()
    