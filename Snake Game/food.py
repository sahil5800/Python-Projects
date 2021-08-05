from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.refresh_food()

    def refresh_food(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
