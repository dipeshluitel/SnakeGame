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
speed = 0.1
score.display_score(points)
while game_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # Detect the food Collision
    if snake.head.distance(food) < 20:
        points = points+1
        speed = speed - 0.007
        food.new_coordinate()
        snake.extend()
        score.display_score(points)

    # Detect the collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    # Detect collision with own tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()
screen.exitonclick()
