from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup UI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

Snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    #Detection of food
    if Snake.head.distance(food) < 15:
        food.refresh()
        Snake.extend()
        scoreboard.increase_score()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for block in Snake.blocks:
        if block == Snake.head:
            pass
        elif Snake.head.distance(block) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()



