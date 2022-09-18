# Imports
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

# Screen setup 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Generating objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listening for keystrokes
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop 
is_game_on = True
while is_game_on:
    # It sets snake's "speed"
    screen.update()
    sleep(0.1)

    # Moves snake
    snake.move()

    # Colission with food
    if snake.head.distance(food) < 20:
        # Food changes position
        food.refresh()
        # Score gets increased
        scoreboard.add_score()
        # Snake grows
        snake.grow()

    # Colission with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Colission with tail
    for seg in snake.body[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            scoreboard.game_over()















screen.exitonclick()