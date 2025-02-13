from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.left(90)
        self.shape("turtle")
        self.color("green")
        self.goto(STARTING_POSITION)


    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def top(self):
        if self.ycor() > (FINISH_LINE_Y -10):
            self.goto(STARTING_POSITION)
            return True
        else:
            return False

    def reset(self):
        self.goto(STARTING_POSITION)