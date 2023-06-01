from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 275)
        self.color("white")
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        self.hideturtle()

    def update_score(self, newscore):
        self.score = newscore
        self.goto(0, 275)
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def update_highscore(self):
        if self.score > self.high_score:
            with open("score.txt", mode='w') as data:
                data.write(str(self.score))
            with open("score.txt") as data:
                self.high_score = int(data.read())

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", font=('Arial', 30, "bold"), align=ALIGNMENT)
        self.goto(0, -20)
        self.write(f"Highest score: {self.high_score}", font=('Arial', 10, "bold"), align=ALIGNMENT)