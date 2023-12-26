from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_SCORE=0
L_PADDLE_SCORE=0

scoreboard=Scoreboard()
ball=Ball()
screen=Screen()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
screen.title("Pong Game")
screen.bgcolor("black")
screen.screensize(canvwidth=800,canvheight=600)


screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320:
        ball.bounce_x()

    if ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    if ball.xcor()>380:
       L_PADDLE_SCORE+=1
       ball.goto(0,0)
       ball.x_move=-10
       ball.y_move = -10
       scoreboard.clear()

    if ball.xcor()<-380:
       R_PADDLE_SCORE+=1
       ball.goto(0,0)
       ball.x_move=10
       ball.y_move =10
       scoreboard.clear()

    scoreboard.score(R_PADDLE_SCORE,L_PADDLE_SCORE)

screen.exitonclick()