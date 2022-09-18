from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()

        # Setting food up
        self.shape("square")
        self.penup()
        self.color("red")
        self.speed("fastest")

        self.refresh()


    # Food while eaten moves to different place
    def refresh(self):
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)