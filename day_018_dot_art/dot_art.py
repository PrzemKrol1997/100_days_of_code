import colorgram
import turtle as t
import random
t.colormode(255)

colors = colorgram.extract('painting.jpg', 15)

def change_color():
    random_colour = random.randint(0, 14)
    r = colors[random_colour].rgb.r
    b = colors[random_colour].rgb.g
    g = colors[random_colour].rgb.b
    #print(f" r: {r}, g: {g},b: {b}")
    return r, g, b

henry = t.Turtle()
henry.shape("arrow")
henry.speed(10)
henry.up()
henry.hideturtle()
starting_position_x = -(768-28)/2  #760
starting_position_y = -(720-40)/2 #680
for _ in range (11):
    henry.teleport(starting_position_x, starting_position_y)
    for _ in range (11):
        henry.dot(20,change_color())
        henry.forward( 73)
    starting_position_y += 68




screen = t.Screen()
# print(screen.window_width())
# print(screen.window_height())
screen.exitonclick()
