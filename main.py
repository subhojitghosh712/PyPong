from turtle import Turtle,Screen

screen = Screen()
screen.title("Ping Pong Game By Subhojit Ghosh")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

def goup():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def godown():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(goup,"Up")
screen.onkey(godown,"Down")

paddle = Turtle()
paddle.penup()
paddle.goto(350,0)
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")

game = True
while game:
    screen.update()

screen.exitonclick()