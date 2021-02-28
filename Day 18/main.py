from turtle import Turtle, Screen
from random import randint
timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed(0)

def random_colour():
    return (randint(0, 255), randint(0, 255), randint(0, 255))

for i in range(0, 361, 10):
    colour = random_colour()
    timmy.pencolor(colour)
    timmy.seth(i)
    timmy.circle(100)

screen.exitonclick()
