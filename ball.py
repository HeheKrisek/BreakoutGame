from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.hideturtle()
        self.speed("slowest")
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.showturtle()

    def move(self, speed1, speed2):
        new_x = self.xcor() + speed1
        new_y = self.ycor() + speed2
        self.goto(new_x, new_y)
