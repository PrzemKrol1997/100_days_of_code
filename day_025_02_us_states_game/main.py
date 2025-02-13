import turtle
import pandas
FONT=('Arial', 8, 'normal')


states_list = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("USA state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# print(states_list.state)
henry = turtle.Turtle()
henry.up()
henry.hideturtle()
guessed_states=[]


while len(guessed_states) < 50:
    is_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed",prompt="Enter state name").title()
    if is_state == "Exit":
        break

    for name_of_state in states_list.state:
        if is_state == name_of_state and name_of_state not in guessed_states:
            x_location = states_list[states_list.state == name_of_state]["x"].values[0]
            y_location = states_list[states_list.state == name_of_state]["y"].values[0]
            guessed_states.append(name_of_state)
            henry.teleport(x_location,y_location)
            henry.write(f"{name_of_state}",align="center",font=FONT)

henry.teleport(0, 0)

if len(guessed_states) == 50:
    henry.write(f"Congratulation, you have guest all 50 states", align="center", font=('Arial', 24, 'normal'))
else:
    henry.write(f"You have guessed {len(guessed_states)}/50 states\nWe have created list of missed states in missed_states file", align="center", font=('Arial', 18, 'normal'))
    missed_state =[name_of_state for name_of_state in states_list.state if name_of_state not in guessed_states]
    # for name_of_state in states_list.state:
    #     if name_of_state not in guessed_states:
    #         missed_state.append(name_of_state)
    data = pandas.DataFrame(missed_state)
    data.to_csv("missed_states.csv")

turtle.mainloop()
