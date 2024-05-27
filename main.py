import time
from turtle import Screen
from Snake import snake

# Setup UI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

Snake = snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    Snake.move()



screen.exitonclick()



