from turtle import Turtle
FONT =('Arial', 14, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.score = 0
        self.teleport(x=0,y=280)
        self.color("white")
        self.write_score_board()

    def write_score_board(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score_board()


    def game_over(self):
        self.teleport(x=0, y=0)
        self.write(f"GAME OVER!", move=False, align='center', font=FONT)