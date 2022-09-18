from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self) -> None:
        # Using Turtle class to create snake with body length of three
        self.body = [Turtle(shape="square") for _ in range(3)]
        self.head = self.body[0]

        # Setting snake's body up
        for i in range(len(self.body)):
            self.body[i].penup()
            self.body[i].color("white")
            self.body[i].goto(-i*20, 0)


    def move(self):
        for i in range(len(self.body)-1, 0, -1):

            # Coords of the previous block become coords of the next block
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)

        # First block sets the directions
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def right(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)


    # Creating new segment of snake
    def grow(self):
        new_seg = Turtle(shape="square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(self.body[-1].position())

        self.body.append(new_seg)
        




