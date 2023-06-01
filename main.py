import random
import time
from turtle import Screen
from ball import Ball
from brick import Brick
from paddle import Paddle
from scoreboard import Scoreboard


def faster(ball_speed):
    if ball_speed > 0.004:
        ball_speed -= 0.002
        print(ball_speed)

    return ball_speed


def addscore(score):
    global ball_speed
    global speed1
    score += 1
    scoreboard.update_score(score)
    print(score)
    if score % 28 == 0:
        ball.goto(0, 0)
        if 0.04 - score*0.0001 > 0.004:
            ball_speed = 0.04 - score*0.0001

        fillbricks()
        pad.goto(0, -275)
        speed1 = 0
        time.sleep(1)

    return score


def fillbricks():
    global bricks_row_1
    global bricks_row_2
    global bricks_row_3
    global bricks_row_4
    bricks_row_1 = []
    bricks_row_2 = []
    bricks_row_3 = []
    bricks_row_4 = []
    for i in range(-3, 4):
        brck = Brick()
        bricks_row_1.append(brck)
        brck.create_brick(i * 95, 260, "red")

    for i in range(-3, 4):
        brck = Brick()
        bricks_row_2.append(brck)
        brck.create_brick(i * 90, 220, "orange")

    for i in range(-3, 4):
        brck = Brick()
        bricks_row_3.append(brck)
        brck.create_brick(i * 95, 180, "yellow")

    for i in range(-3, 4):
        brck = Brick()
        bricks_row_4.append(brck)
        brck.create_brick(i * 90, 140, "green")


def game_over():
    global game_loop
    global score
    global speed1
    global ball_speed
    global bricks_row_1
    global bricks_row_2
    global bricks_row_3
    global bricks_row_4
    scoreboard.update_highscore()
    scoreboard.game_over()
    game_loop = False
    time.sleep(3)
    for brc in bricks_row_1:
        brc.goto(500, 500)
    for brc in bricks_row_2:
        brc.goto(500, 500)
    for brc in bricks_row_3:
        brc.goto(500, 500)
    for brc in bricks_row_4:
        brc.goto(500, 500)
    fillbricks()
    score = 0
    scoreboard.update_score(score)
    pad.goto(0, -275)
    ball.goto(0, 0)
    speed1 = 0
    ball_speed = 0.04
    time.sleep(1)
    game_loop = True


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()

pad = Paddle()
pad.create_paddle(0, -275)

ball = Ball()

fillbricks()

screen.listen()
screen.onkeypress(pad.rgt, "d")
screen.onkeypress(pad.lft,"a")

game_loop = True
speed1 = 0
speed2 = -5
ball_speed = 0.04
score = 0

while game_loop:
    time.sleep(ball_speed)
    screen.update()
    ball.move(speed1, speed2)

    # detect ball collision with top/left/right
    if ball.ycor() > 280:
        speed2 = -speed2

    if ball.xcor() > 380 or ball.xcor() < -380:
        speed1 = -speed1

    # detect collision with paddle
    if pad.distance(ball) < 65 and ball.ycor() == -260:
        if speed1 == 0:
            rndm = random.randint(0, 1)
            if rndm == 1:
                speed1 = 5
            else:
                speed1 = -5

        speed2 = -speed2

    # detect if the ball gets out
    if ball.ycor() < -300:
        game_over()

    # prevent moving the paddle off the screen
    if pad.xcor() > 350:
        pad.setx(350)

    elif pad.xcor() < -350:
        pad.setx(-350)

    # destroy red bricks
    for brick in bricks_row_1:
        if brick.distance(ball) < 45 and ball.ycor() > 260:
            brick.goto(500,500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 240:
            brick.goto(500,500)
            speed1 = -speed1
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 230:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

    # destroy orange bricks
    for brick in bricks_row_2:
        if brick.distance(ball) < 45 and ball.ycor() > 220:
            brick.goto(500,500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 200:
            brick.goto(500,500)
            speed1 = -speed1
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 190:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

    # destroy yellow bricks
    for brick in bricks_row_3:
        if brick.distance(ball) < 45 and ball.ycor() > 180:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 160:
            brick.goto(500, 500)
            speed1 = -speed1
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 150:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

    # destroy green bricks
    for brick in bricks_row_4:
        if brick.distance(ball) < 45 and ball.ycor() > 140:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 120:
            brick.goto(500, 500)
            speed1 = -speed1
            ball_speed = faster(ball_speed)
            score = addscore(score)

        elif brick.distance(ball) < 45 and ball.ycor() > 110:
            brick.goto(500, 500)
            speed2 = -speed2
            ball_speed = faster(ball_speed)
            score = addscore(score)


screen.exitonclick()