from turtle import Screen
from Snake import Snake
from food import Food
import time

# Setup UI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

Snake = Snake()
food = Food()

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

    if Snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()



