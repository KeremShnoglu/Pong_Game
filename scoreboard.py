from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
    def score(self,R_PADDLE_SCORE,L_PADDLE_SCORE):
        self.write(f"R_Paddle SCORE={R_PADDLE_SCORE} ,L_Paddle SCORE={L_PADDLE_SCORE} ",False,"center",20)