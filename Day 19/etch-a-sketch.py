from turtle import Turtle, Screen
from random import choice, randint

turtle_list = []
colour_list = ["red", "orange", "yellow", "green", "blue", "purple"]

is_race_on = False

for i in range (0, 6):
    colour = choice(colour_list)
    colour_list.remove(colour)
    tmp = Turtle(shape = "turtle")
    tmp.color(colour)
    turtle_list.append(tmp)

screen = Screen()
screen.setup(width = 600, height = 400)

user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ").lower()


y = -150
for i in turtle_list:
    i.penup()
    i.goto(x = -250, y = y)
    y += 50

if user_bet:
    is_race_on = True

winner = None
while is_race_on:
    for i in turtle_list:
        rand_distance = randint(0, 10)
        i.forward(rand_distance)

        if i.xcor() > 275:
            winner = i
            break
    if winner:
        break

if winner.color() == user_bet:
    print(f"You win! {winner.color()[0].title()} turtle won the race.")
else:
    print(f"You lose! {winner.color()[0].title()} turtle won the race.")


screen.listen()
screen.exitonclick()
