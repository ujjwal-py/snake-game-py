from turtle import Turtle

FONT = ("Lucida Console", 18, "bold")
with open("highscore.txt") as save_file:
    saved_score = save_file.read()



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.score = 0
        self.highscore = int(saved_score)
        self.update_score()


    def update_score(self):
        self.clear()
        # self.score = self.score+1
        self.write(arg=f"Score - {self.score} HighScore - {self.highscore}",align="center", font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()
    # def gameover(self):
    #     self.goto(0,0)
    #     self.color("white")
    #     self.write(arg="GAME OVER!", align="center", font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt","w") as saving_score:
                new_high = saving_score.write(str(self.highscore))
        self.score = 0
        self.update_score()



