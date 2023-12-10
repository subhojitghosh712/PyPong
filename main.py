from turtle import Turtle,Screen
from paddle import Paddle

screen = Screen()
screen.title("Ping Pong Game By Subhojit Ghosh")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddleL = Paddle((350, 0))
paddleR = Paddle((-350, 0))

screen.listen()
screen.onkey(paddleL.goup, "Up")
screen.onkey(paddleL.godown, "Down")

screen.onkey(paddleR.goup, "w")
screen.onkey(paddleR.godown, "s")

game = True
while game:
    screen.update()

screen.exitonclick()