import turtle as t
import time

TURTLE_SPEAD=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS=[(0,0),(0,-20),(0,-40)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def snake_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                self.reset_snake()
                return True
        if self.head.xcor() > 290 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            self.reset_snake()
            return True
        return False


    def reset_snake(self):
        for segment in self.segments:
            segment.teleport(x=1000,y=1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_segment(self, position):
        new_segment =t.Turtle(shape="square")
        new_segment.color("white")
        new_segment.up()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def snake_move(self):
        for seg_numb in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[seg_numb - 1].xcor()
            y_cor = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(x_cor, y_cor)
        self.head.forward(TURTLE_SPEAD)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(180)





