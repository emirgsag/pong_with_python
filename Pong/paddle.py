from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, number):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.color("white")
        self.penup()
        if number == 1:
            self.goto(-530, 0)
        elif number == 2:
            self.goto(530, 0)
        self.speed("fastest")
        self.setheading(90)

    def move(self):
        self.border()
        self.forward(6)

    def up(self):
        self.setheading(90)

    def down(self):
        self.setheading(270)

    def border(self):
        for x in range(-560, 561):
            if self.distance(x, 280) < 15:
                self.setheading(270)

            elif self.distance(x, -280) < 15:
                self.setheading(90)
