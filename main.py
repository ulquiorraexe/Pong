from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r = Paddle((350, 0))
l = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r.go_up)
screen.onkey(key="Down", fun=r.go_down)
screen.onkey(key="w", fun=l.go_up)
screen.onkey(key="s", fun=l.go_down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if ball.distance(r) < 50 and r.xcor() > 320 or ball.distance(l) < 50 and l.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()





screen.exitonclick()
