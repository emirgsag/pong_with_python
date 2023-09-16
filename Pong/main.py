from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard
from desginer import Designer

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1120, height=630)

designer = Designer()
screen.tracer(0)
paddle_1 = Paddle(1)
paddle_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard(0, 0)
screen.update()

screen.listen()
screen.onkeypress(fun=paddle_1.up, key="w")
screen.onkeypress(fun=paddle_1.down, key="s")

screen.onkeypress(fun=paddle_2.up, key="o")
screen.onkeypress(fun=paddle_2.down, key="l")

end_game = False
while not end_game:
    screen.tracer(0)
    paddle_1.move()
    paddle_2.move()
    ball.move()
    if 0 < ball.xcor() - paddle_1.xcor() < 7 and paddle_1.ycor() - 50 < ball.ycor() < paddle_1.ycor() + 50:
        ball.setheading(180 - ball.heading())
        ball.move_speed *= 0.9

    elif 0 < ball.xcor() - paddle_2.xcor() < 7 and paddle_2.ycor() - 50 < ball.ycor() < paddle_2.ycor() + 50:
        ball.setheading(180 - ball.heading())
        ball.move_speed *= 0.9

    if ball.at_goal_post_1():
        ball.player_2_goals()
        scoreboard.update(ball.score_1, ball.score_2)
        screen.update()
        sleep(1)
        ball.recenter()

    elif ball.at_goal_post_2():
        ball.player_1_goals()
        scoreboard.update(ball.score_1, ball.score_2)
        screen.update()
        sleep(1)
        ball.recenter()
        # ball.setheading(ball.heading() - 180)

    if ball.score_1 == 5:
        end_game = True
        ball.player_1_wins()
        screen.update()

    elif ball.score_2 == 5:
        end_game = True
        ball.player_2_wins()
        screen.update()

    screen.update()
    sleep(ball.move_speed)

screen.exitonclick()
