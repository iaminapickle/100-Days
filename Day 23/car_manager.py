from car import Car
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        colour = choice(COLORS)
        car = Car(colour, self.speed)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.go_left(self.speed)
            if car.xcor() < -320:
                self.cars.remove(car)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
