from turtle import Turtle, Screen
import random

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    henry.color(r, g, b)


def making_shapes(number_of_sides,):
    change_color()
    for _ in range(number_of_sides):
        henry.forward(100)
        henry.right(360 / number_of_sides)


def draw_spirograph(size_of_gap):
    for _ in range(int(round(360/size_of_gap,0))):
        change_color()
        henry.circle(100)
        henry.setheading(henry.heading() + size_of_gap)



henry = Turtle()
henry.shape("turtle")
henry.color("blue")
henry.width(1)
henry.speed(10)
# for sides in range(3,11):
#     making_shapes(sides)
# sides = [0,90,180,270]
# for steps in range(100):
#     change_color()
#     henry.right(random.choice(sides))
#     henry.forward(20)
draw_spirograph(10)



























screen = Screen()

screen.exitonclick()