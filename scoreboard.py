from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_one_score = 0
        self.player_two_score = 0
        self.display_score()

    def player_one_point(self):
        self.player_one_score += 1

    def player_two_point(self):
        self.player_two_score += 1

    def display_score(self):
        self.goto(-100, 200)
        self.write(self.player_one_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.player_two_score, align="center", font=("Courier", 80, "normal"))