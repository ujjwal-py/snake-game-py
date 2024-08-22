import turtle
from turtle import Turtle

FONT = ("Tahoma", 16, "normal")




class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.pen()
        self.goto(0,0)


    def write_on_over(self):
        self.write(arg=f"GAME OVER!\nContinue? (Press y for Yes, n for Exit)",
                   align="center",
                   font=FONT)

    def remove_writing(self):
        self.clear()

