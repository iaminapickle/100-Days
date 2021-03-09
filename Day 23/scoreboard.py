from turtle import Turtle
FONT = ("Courier", 24, "normal")
POSITION = (-280, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.level = 0
        self.goto(POSITION)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font = FONT, align = "left")
