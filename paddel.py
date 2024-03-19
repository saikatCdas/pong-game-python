from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create(position)

    def create(self, position):
        self.shape("square")
        self.color('White')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)