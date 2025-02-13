#create classes for paddles, scoreboard, ball
#generate middle line for the screen

import turtle as t
import time
from pong_screen import PongScreen
from paddle import Paddle
import pygame
from ball import Ball
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HIT_DISTANCE = 50

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


screen = t.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
t.tracer(0)
paddle1 =Paddle(1)
paddle2 =Paddle(2)
pong_screen = PongScreen()
screen.listen()

ball = Ball()

screen.onkey(paddle1.paddle_up, "Up")
screen.onkey(paddle1.paddle_down, "Down")
screen.onkey(paddle2.paddle_up, "w")
screen.onkey(paddle2.paddle_down, "s")

game_is_on = True
while game_is_on:
    t.update()
    time.sleep(ball.move_speed)
    ball.ball_move()
    if ball.distance(paddle2) < HIT_DISTANCE and ball.xcor() < -(SCREEN_WIDTH/2-40):
        ball.direction_x *= -1
    if ball.distance(paddle1) < HIT_DISTANCE and ball.xcor() > (SCREEN_WIDTH/2-40):
        ball.direction_x *= -1
    point = ball.check_point()
    if point == 1:
        pong_screen.point_player2()
        point = 0
    elif point == -1:
        pong_screen.point_player1()
        point = 0
    game_is_on = pong_screen.is_game_on()




# score_board.game_over()
#
#
#

screen.exitonclick()