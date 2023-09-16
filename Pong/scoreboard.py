from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, value_1, value_2):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(0, 240)
        self.write(arg=f"{value_1}     {value_2}", move=False, align="center", font=("Arial", 50, "normal"))

    def update(self, value_1, value_2):
        self.clear()
        self.write(arg=f"{value_1}     {value_2}", move=False, align="center", font=("Arial", 50, "normal"))
