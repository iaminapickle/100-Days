import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

car_manager = CarManager()
car_manager.create_car()

scoreboard = Scoreboard()
game_is_on = True

start = time.perf_counter()
mul = random.random()

while game_is_on:
    time.sleep(0.05)
    # If player has reached the end
    if player.ycor() >= FINISH_LINE_Y:
        player.restart()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
    # Check collision
    for car in car_manager.cars:
        if player.distance(car) < 25:
            game_is_on = False

    # Randomly add cars
    dif = time.perf_counter() - start
    if dif > mul * 0.5:
        start = time.perf_counter()
        mul = random.random()
        car_manager.create_car()

    # Move all cars
    car_manager.move_cars()

    screen.update()

screen.exitonclick()
