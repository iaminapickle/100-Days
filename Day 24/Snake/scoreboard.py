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
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())
        self.write(f"Score = {self.score} | High Score = {self.high_score}", align = ALIGNMENT, font = FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score} | High Score = {self.high_score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("highscore.txt", "w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = -1
        self.update()
