from turtle import Turtle

X_DIRECTION_SPEED = 10
Y_DIRECTION_SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x_direction = X_DIRECTION_SPEED
        self.y_direction = Y_DIRECTION_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_direction,self.ycor() + self.y_direction)

    def bounce_y(self):
        self.y_direction = -self.y_direction

    def bounce_x(self):
        self.x_direction = -self.x_direction

    def reset(self):
        self.goto(0,0)
        self.x_direction = -self.x_direction