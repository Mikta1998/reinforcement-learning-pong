from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def left_paddle_size(self):
        self.shapesize(stretch_wid=5, stretch_len=1)

    def right_paddle_size(self):
        self.shapesize(stretch_wid=30, stretch_len=1)

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)