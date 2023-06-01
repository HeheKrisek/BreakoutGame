from turtle import Turtle


class Brick(Turtle):

    def __init__(self):
        super().__init__()

    def create_brick(self, x1, y1, color):
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4, outline=None)
        self.goto(x=x1, y=y1)
        self.showturtle()
