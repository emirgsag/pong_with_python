from turtle import Turtle


class Designer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(5)
        self.penup()
        self.goto(0, -282)
        self.setheading(90)
        for _ in range(9):
            self.pendown()
            self.forward(34)
            self.penup()
            self.forward(34)
