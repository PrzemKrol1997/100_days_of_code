import random
import turtle as t


def turtle_move(contestant):
    contestant.forward(random.randint(5,20))


def random_turtle_move(table_move):
    random.shuffle(table_move)
    for move in table_move:
        turtle_move(move)

def check_bet(player_choice,winner_turtle):
    t.write(f"{winner_turtle} wins!!  ",True,"left",font=('Arial', 12, 'normal'))
    if player_choice == winner_turtle:
        t.write("You have bet correctly, you win!!",True,"left",font=('Arial', 12, 'normal'))
    else:
        t.write("You have bet incorrectly, you lose.",True,"left",font=('Arial', 12, 'normal'))


def check_finish(table):
    for contestant in range(len(table)):
        if table[contestant].pos()[0] > 350:
            return table[contestant].color()[0]
    return True


screen = t.Screen()
screen.setup(width=800,height=440)
starting_position_x = -500/2
starting_position_y = -400/2
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
table_of_turtles =[]
i=0


for turtle in rainbow_colors:
    table_of_turtles.append(t.Turtle(shape="turtle"))
    table_of_turtles[i].color(turtle)
    table_of_turtles[i].speed(0)
    table_of_turtles[i].teleport(starting_position_x, starting_position_y)
    starting_position_y += 50
    i += 1

bet = t.textinput("bet on turtle colour","(red/orange/yellow/green/blue/indigo/violet): ")

winner = True
while winner == True:
    random_turtle_move(table_of_turtles)
    winner = check_finish(table_of_turtles)
check_bet(winner_turtle=winner,player_choice=bet)



screen.exitonclick()