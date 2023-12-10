from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Ping Pong Game By Subhojit Ghosh")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddleR = Paddle((350, 0))
paddleL = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()
scoreboard.update()

screen.listen()
screen.onkey(paddleR.goup, "Up")
screen.onkey(paddleR.godown, "Down")

screen.onkey(paddleL.goup, "w")
screen.onkey(paddleL.godown, "s")

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddleR) < 50 and ball.xcor() > 320 or ball.distance(paddleL) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update()

    if scoreboard.l_score == 5:
        game = False
        scoreboard.game_over("L")

    if scoreboard.r_score == 5:
        game = False
        scoreboard.game_over("R")


screen.exitonclick()