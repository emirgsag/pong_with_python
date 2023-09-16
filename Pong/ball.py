from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.random_heading()
        self.score_1 = 0
        self.score_2 = 0
        self.move_speed = 0.007

    def move(self):
        self.border()
        self.forward(7)

    def random_heading(self):
        self.setheading(randint(155, 235))

    def border(self):
        if self.ycor() > 305:
            self.setheading(360 - self.heading())

        elif self.ycor() < -305:
            self.setheading(360 - self.heading())

    def at_goal_post_1(self):
        for y in range(-315, 316):
            if self.distance(-560, y) <= 10:
                return True

    def player_2_goals(self):
        self.score_2 += 1
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        self.write(arg="Goal!!!", move=False, align="center", font=("Arial", 40, "normal"))

    def at_goal_post_2(self):
        for y in range(-315, 316):
            if self.distance(560, y) <= 10:
                return True

    def player_1_goals(self):
        self.score_1 += 1
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        self.write(arg="Goal!!!", move=False, align="center", font=("Arial", 40, "normal"))

    def player_1_wins(self):
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        self.write(arg="Player 1 Wins!!!", move=False, align="center", font=("Arial", 40, "normal"))

    def player_2_wins(self):
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        self.write(arg="Player 2 Wins!!!", move=False, align="center", font=("Arial", 40, "normal"))

    def recenter(self):
        self.hideturtle()
        self.random_heading()
        self.clear()
        self.move_speed = 0.007
        self.showturtle()
