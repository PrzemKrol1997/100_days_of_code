from random import choice
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
STARTING_POSITION_Y =list(range(-250, 251, 20))


def teleport_to_start(car):
    car.teleport(x=290, y=choice(STARTING_POSITION_Y))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.level = 0
        self.create_car()

    def create_car(self):
        new_car = Turtle(shape="square")
        new_car.color(choice(COLORS))
        new_car.up()
        new_car.right(180)
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        teleport_to_start(new_car)
        self.all_cars.append(new_car)

    def car_forward(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*self.level)

    def reset(self):
        self.level = 0





