from turtle import Turtle
PADDLE_SPEAD=40
UP = 90
DOWN = 270
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

STARTING_POSITIONS_Player_1=(SCREEN_WIDTH/2-20,0)
STARTING_POSITIONS_Player_2=(-(SCREEN_WIDTH/2-20),0)

class Paddle(Turtle):
    def __init__(self,player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.up()
        self.shapesize(stretch_wid=5, stretch_len=1)
        if player == 1:
            self.goto(STARTING_POSITIONS_Player_1)
        else:
            self.goto(STARTING_POSITIONS_Player_2)



    def paddle_up(self):
        if self.ycor() < (SCREEN_HEIGHT/2 -20):
                x_cor = self.xcor()
                y_cor = self.ycor() + PADDLE_SPEAD
                self.goto(x_cor, y_cor)


    def paddle_down(self):
        if self.ycor() > -(SCREEN_HEIGHT/2 -20):
            x_cor = self.xcor()
            y_cor = self.ycor() - PADDLE_SPEAD
            self.goto(x_cor, y_cor)