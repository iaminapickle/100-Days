from turtle import Turtle, Screen
from random import choice
# import colorgram
#
# colours = colorgram.extract("img.jpg", 26)
# rgb_list = []
#
# for i in colours:
#     rgb = (i.rgb.r, i.rgb.g, i.rgb.b)
#     rgb_list.append(rgb)
#
# print(rgb_list)

t = Turtle()
t.speed(0)
t.up()
t.goto(-200, -200)

screen = Screen()
screen.colormode(255)
colour_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175),
               (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
               (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]


for x in range(0, 10):
    for y in range(0, 10):
        colour = choice(colour_list)
        t.fillcolor(colour)
        t.color(colour)
        t.down()

        t.begin_fill()
        t.circle(10)
        t.end_fill()

        t.up()
        t.forward(70)
    t.up()
    t.back(70)
    if x % 2 == 0:
        t.left(90)
        t.forward(90)
        t.left(90)
    else:
        t.right(90)
        t.forward(50)
        t.right(90)

screen.exitonclick()
