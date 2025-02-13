import turtle as t

def move_forward():
    henry.forward(20)

def move_back():
    henry.back(20)

def turn_right():
    henry.right(10)

def turn_left():
    henry.left(10)

def clear():
    screen.resetscreen()

henry = t.Turtle()
henry.shape("turtle")




screen = t.Screen()
screen.listen()
screen.onkey(fun=move_forward,key="w")
screen.onkey(fun=move_back,key="s")
screen.onkey(fun=turn_left,key="a")
screen.onkey(fun=turn_right,key="d")
screen.onkey(fun=clear,key="c")


screen.exitonclick()
