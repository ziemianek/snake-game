from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 16)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        # This attribute keeps score count
        self.score = 0

        # Setting scoreboard up
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()


    # This method is responsible for updating info about the score
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    # Adding score, clearing previous score, updating score
    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        

    # Displays "game over" text in the center of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT)