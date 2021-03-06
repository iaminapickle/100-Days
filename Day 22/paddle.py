from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, start_coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed(0)
        self.up()
        self.goto(start_coord)
        self.setheading(90)
        self.shapesize(stretch_len = 5)


    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
