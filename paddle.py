from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()

    def create_paddle(self, x1, y1):
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=5, outline=None)
        self.goto(x=x1, y=y1)
        self.showturtle()

    def rgt(self):
        new_y = self.ycor()
        new_x = self.xcor()
        self.goto(new_x + 20, new_y)

    def lft(self):
        new_y = self.ycor()
        new_x = self.xcor()
        self.goto(new_x - 20, new_y)