from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while (game_is_on):
    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce(r_paddle, l_paddle)

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.increase_speed()
        ball.bounce(r_paddle, l_paddle)

    # Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.increase_speed()
        ball.bounce(r_paddle, l_paddle)

    # Detect out of bounds
    if ball.xcor() > 370 or ball.xcor() < -370:
        if ball.xcor() > 370:
            ball.last_winner = "right"
            scoreboard.r_point()
        elif ball.xcor() < -370:
            ball.last_winner = "left"
            scoreboard.l_point()

        ball.reset_ball()

    ball.move()
    screen.update()
    sleep(0.05)

screen.exitonclick()
