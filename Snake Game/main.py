from turtle import Screen
from food import Food
from score_board import Score
from snake import Snake
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ping-Pong Game")
screen.listen()

snake = Snake()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

food = Food()

score = Score()

delay = 0.1
n = 0
snake_on_move = True
while snake_on_move:
    snake_head = snake.snake_list[0]
    time.sleep(delay)
    snake.move()
    score.score(n)
    screen.update()


    if snake_head.distance(food) < 20:
        position_x = snake.snake_list[-1].xcor()
        position_y = snake.snake_list[-1].ycor()
        snake.extend(position_x, position_x)
        delay *= 0.9
        food.refresh_food()
        n += 1

    if snake_head.xcor() < -290 or snake_head.xcor() > 280 or snake_head.ycor() < -285 or snake_head.ycor() > 280:
        score.update(n)
        snake.update()
        delay = 0.1
        n = 0


    for tails in snake.snake_list[2::]:
        if snake_head.distance(tails) < 20:
            score.update(n)
            snake.update()
            delay = 0.1
            n = 0



screen.exitonclick()