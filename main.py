from turtle import Screen
from ball import *
from paddle import *
from scoreboard import *
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
left_paddle.left_paddle_size()
right_paddle.right_paddle_size()
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    elif ball.distance(right_paddle) < 300 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.xcor() > 400:
        ball.reset()
        scoreboard.player_one_point()
        scoreboard.clear()
        scoreboard.display_score()
    elif ball.xcor() < -400:
        ball.reset()
        scoreboard.player_two_point()
        scoreboard.clear()
        scoreboard.display_score()

screen.exitonclick()