from turtle import Turtle
FONT =('Arial', 14, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.hideturtle()
        self.teleport(x=0,y=280)
        self.color("white")
        self.write_score_board()

    def write_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.highscore}", move=False, align='center', font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                self.highscore =self.score
                file.write(f"{self.highscore}")
        self.score = 0
        self.write_score_board()

    def increase_score(self):
        self.score += 1
        self.write_score_board()


    # def game_over(self):
    #     self.teleport(x=0, y=0)
    #     self.write(f"GAME OVER!", move=False, align='center', font=FONT)
    #     self.teleport(x=0, y=280)