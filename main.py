import turtle
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



screen.listen()
screen.onkey(key="Up", fun=snake.snake_up)
screen.onkey(key="Down", fun=snake.snake_down)
screen.onkey(key="Left", fun=snake.snake_left)
screen.onkey(key="Right", fun=snake.snake_right)






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
        # game_is_on = False
        # gameover = Gameover()
        # gameover.write_on_over()
        # if screen.onkey(key="y",fun=):
        #     game_is_on = True
        #     score.reset()
        # elif screen.onkey(key="n", fun=):
        #     pass
        score.reset()
        snake.reset()



    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            score.reset()
            snake.reset()




screen.exitonclick()