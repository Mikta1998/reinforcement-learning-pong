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

player_one = Paddle((350,0))
player_two = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(player_one.move_up, "Up")
screen.onkey(player_one.move_down, "Down")

screen.onkey(player_two.move_up, "w")
screen.onkey(player_two.move_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(player_one) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif ball.distance(player_two) < 50 and ball.xcor() < -320:
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