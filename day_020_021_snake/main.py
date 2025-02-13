import turtle as t
import time
from scoreboard import ScoreBoard
from snake import Snake
from foood import Food
import pygame
REFRESH_TIME = 0.1


pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
t.tracer(0)
food =Food()
snake = Snake()
score_board = ScoreBoard()
screen.listen()
screen.onkey(snake.snake_up,"Up")
screen.onkey(snake.snake_down,"Down")
screen.onkey(snake.snake_left,"Left")
screen.onkey(snake.snake_right,"Right")

game_is_on = True
while game_is_on:
    t.update()
    time.sleep(REFRESH_TIME)
    snake.snake_move()
    if snake.head.distance(food) < 15:
        food.new_food()
        score_board.increase_score()
        snake.extend()
    game_is_on = snake.snake_collision()



score_board.game_over()




screen.exitonclick()