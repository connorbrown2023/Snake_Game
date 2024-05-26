import time
from turtle import Screen, Turtle

# Setup UI
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

starting_positions  = [(0,0), (-20, 0), (-40, 0)]

Blocks = []

for position in starting_positions:
    new_block = Turtle("square")
    new_block.color("white")
    new_block.penup()
    new_block.goto(position)
    Blocks.append(new_block)

game_is_on = True

while game_is_on:
    for block in Blocks:
        block.forward(20)
        screen.update()
        time.sleep(1)


screen.exitonclick()



