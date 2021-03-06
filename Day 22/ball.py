from turtle import Turtle
from math import atan, degrees

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed(0)
        self.up()
        self.goto(0, 0)
        self.ball_speed = 10
        self.setheading(45)

    def move(self):
        self.forward(self.ball_speed)

    def find_bounce_direction(self):
        heading = self.heading()
        if heading < 90 and heading > 0:
            return "up_right"
        elif heading < 180 and heading > 90:
            return "up_left"
        elif heading < 270 and heading > 180:
            return "down_left"
        elif heading < 360 and heading >270:
            return "down_right"

    def bounce(self, r_paddle, l_paddle):
        bounce_direction = self.find_bounce_direction()
        if self.ycor() > 280 or self.ycor() < -280:

            if bounce_direction == "up_right" or bounce_direction == "down_left":
                add = -90
            elif bounce_direction == "up_left" or bounce_direction == "down_right":
                add = 90

        elif self.distance(r_paddle) < 50 and self.xcor() > 340:
            if bounce_direction == "down_right":
                add = -90
            elif bounce_direction == "up_right":
                add = 90

        elif self.distance(l_paddle) < 50 and self.xcor() < -340:
            if bounce_direction == "up_left":
                add = -90
            elif bounce_direction == "down_left":
                add = 90

        self.setheading(self.heading() + add)

    def reset_ball(self):
        self.ball_speed = 10
        last_winner = self.last_winner

        if last_winner == "left":
            self.setheading(45)
        elif last_winner == "right":
            self.setheading(135)

        self.goto(0, 0)

    def increase_speed(self):
        self.ball_speed += 5
