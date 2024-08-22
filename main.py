from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#083b14")
screen.title("The Classic Snake Game")
screen.tracer(0)




snake = Snake()
food = Food()
score = Scoreboard()
over = Gameover()



def complete_reset():
    over.clear()
    snake.reset()
    score.reset()
    run_game()

screen.listen()
screen.onkey(key="Up", fun=snake.snake_up)
screen.onkey(key="Down", fun=snake.snake_down)
screen.onkey(key="Left", fun=snake.snake_left)
screen.onkey(key="Right", fun=snake.snake_right)
screen.onkey(key="y", fun=complete_reset)
screen.onkey(key="n",fun=screen.bye)


def run_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detecting Collision with food
        if snake.head.distance(food) < 15:
            food.refresh()

            #updating Score
            score.increase_score()

            #increasing the length of snake
            snake.extend()

        #Detecting collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
            over.write_on_over()
            game_is_on = False

        #Detecting collision with its tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                game_is_on = False
                over.write_on_over()


run_game()

screen.exitonclick()