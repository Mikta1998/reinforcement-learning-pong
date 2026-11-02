from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(starting_position)

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)