from turtle import Turtle

STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))
STEPS = 20

class Snake:
    def __init__(self):

        self.snake_list = []
        self.create_snake()


    def create_snake(self):
        for positions in STARTING_POSITION:
            self.snake = Turtle("square")
            self.snake.color("white")
            self.snake.penup()
            self.snake.goto(positions)
            self.snake_list.append(self.snake)

    def extend(self, position_x, position_y):
        self.snake = Turtle("square")
        self.snake.color("white")
        self.snake.penup()
        self.snake.goto(x=position_x, y=position_y)
        self.snake_list.append(self.snake)

    def update(self):
        for tails in self.snake_list:
            tails.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()


    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.snake_list[0].forward(STEPS)

    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)

    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)

