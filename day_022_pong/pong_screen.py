from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WIN_SCORE =5
FONT =('Arial', 14, 'normal')


class PongScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.up()
        self.score_player1 = 0
        self.score_player2 = 0
        self.color("white")
        self.line_turtle = Turtle()
        self.line_turtle.up()
        self.line_turtle.color("white")
        self.middle_line()
        self.teleport(x=0, y=(SCREEN_HEIGHT/2-20))
        self.write_score_board()

    def write_score_board(self):
        self.clear()
        self.write(f" {self.score_player1}        {self.score_player2}", move=False, align='center', font=FONT)

    def middle_line(self):
        self.line_turtle.teleport(x=0, y=-(SCREEN_HEIGHT/2-10))
        self.line_turtle.down()
        self.line_turtle.seth(90)
        i = 0
        for step in range(0,SCREEN_HEIGHT,20):
            self.line_turtle.forward(20)
            if i == 0:
                self.line_turtle.up()
                i = 1
            else:
                self.line_turtle.down()
                i = 0


    def point_player1(self):
        self.clear()
        self.score_player1 += 1
        self.write_score_board()


    def point_player2(self):
        self.clear()
        self.score_player2 += 1
        self.write_score_board()

    def is_game_on(self):
        if self.score_player1 >= WIN_SCORE:
            self.teleport(x=0, y=0)
            self.write(f" PLAYER 1 WINS \n Thank you for participating", move=False, align='center', font=FONT)
            return False
        elif self.score_player2 >= WIN_SCORE:
            self.teleport(x=0, y=0)
            self.write(f" PLAYER 2 WINS \n Thank you for participating", move=False, align='center', font=FONT)
            return False
        else:
            return True
