import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
import pygame

RANDOM_GENERATE_CARS = 6


pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
henry = Player()
score_board =Scoreboard()
screen.listen()
screen.onkey(henry.move_up, "Up")
car_manager =CarManager()


game_is_on = True
pace_of_game = RANDOM_GENERATE_CARS

while game_is_on:

    car_manager.car_forward()

    if RANDOM_GENERATE_CARS-int(car_manager.level/2) < 3:
        pace_of_game = 3
    generate_car = random.randint(1,pace_of_game)

    if generate_car == 1 :
        car_manager.create_car()

    for car in car_manager.all_cars:
        if car.distance(henry) < 20:
            score_board.reset_score()
            henry.reset()
            car_manager.reset()

    if henry.top():
        score_board.increase_score()
        car_manager.level +=1

    time.sleep(0.1)
    screen.update()

screen.exitonclick()

