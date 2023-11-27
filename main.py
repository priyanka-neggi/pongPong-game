from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import ScoreBoard
score = ScoreBoard()
screen = Screen()
screen.title("PONG")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
# paddle
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(5, 1)
# paddle.penup()
# paddle.goto(350, 0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.level)
    screen.update()
    ball.move()
    # detect collision with upper and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision  with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    # detect collision  with right paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() > -350:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_score()
    if ball.xcor() < -390:
        ball.reset_position()
        score.right_score()


screen.exitonclick()
