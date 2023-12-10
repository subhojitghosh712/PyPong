from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(0, 200)
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 40, "bold"))

    def game_over(self, player):
        if player == "L":
            self.clear()
            self.goto(0, 0)
            self.color("yellow")
            self.write("Left Paddle Player Wins !!", align="center", font=("Courier", 20, "bold"))

        elif player == "R":
            self.clear()
            self.goto(0, 0)
            self.color("yellow")
            self.write("Right Paddle Player Wins !!", align="center", font=("Courier", 20, "bold"))

        else:
            pass