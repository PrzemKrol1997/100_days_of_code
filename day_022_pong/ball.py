from turtle import Turtle
import random

BALL_SPEED =15
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.move_speed = 0.1
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        self.reset_ball()

    def ball_move(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.check_collision()
        if self.direction_x == -1:
            xcor -= BALL_SPEED
        else:
            xcor += BALL_SPEED
        if self.direction_y == -1:
            ycor -= BALL_SPEED
        else:
            ycor += BALL_SPEED
        self.goto(x=xcor,y=ycor)

    def check_collision(self):
        if self.ycor() > (SCREEN_HEIGHT/2-20) or self.ycor() < -(SCREEN_HEIGHT/2-20):
            self.direction_y *= -1
            self.move_speed *= 0.9

    def check_point(self):
        if self.xcor() > (SCREEN_WIDTH/2 -10):
            self.reset_ball()
            return -1
        elif self.xcor() < -(SCREEN_WIDTH/2 -10):
            self.reset_ball()
            return 1
        else:
            return 0


    def reset_ball(self):
        self.goto(x=0,y=0)
        self.direction_x *= -1
        self.direction_y *= -1
        self.move_speed = 0.1