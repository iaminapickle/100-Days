from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score = {self.score}", align = ALIGNMENT, font = FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align = ALIGNMENT, font = FONT)
