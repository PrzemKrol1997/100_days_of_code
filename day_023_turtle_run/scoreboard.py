from turtle import Turtle
import time
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.teleport(x = -150,y = 270)
        self.up()
        self.color("black")
        self.write_score()

    def reset_score(self):
        if self.score > self.highscore:
            with open("highscore.txt", mode="w") as file:
                self.highscore =self.score
                file.write(f"{self.highscore}")
        self.score = 0
        self.teleport(x=-150, y=270)
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"level: {self.score}, High Score: {self.highscore}", move=False, align='center', font=FONT)

    def increase_score(self):
        self.score +=1
        self.write_score()

