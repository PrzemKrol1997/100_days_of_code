from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280, 260)
        self.teleport(random_x,random_y)