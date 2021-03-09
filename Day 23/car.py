from turtle import Turtle
from random import randint

class Car(Turtle):
    def __init__(self, colour, speed):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_len = 2)
        self.setheading(180)
        self.color(colour)
        self.speed(0)
        self.up()
        self.goto(320, randint(-290, 290))

    def go_left(self, speed):
        self.forward(speed)
