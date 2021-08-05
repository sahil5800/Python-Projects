from turtle import Turtle, Screen
from random import randint

race_is_on = False
screen=Screen()
screen.screensize(canvwidth=500, canvheight=400)
color = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
n = -100
for i in range(6):
    max1 = Turtle("turtle")
    max1.penup()
    max1.color(color[i])
    max1.goto(x=-370,y=n)
    turtles.append(max1)
    n += 50

line = Turtle()
line.ht()
line.speed("fast")
line.penup()
line.goto(x=-340, y=-150)
line.left(90)
line.pendown()
line.forward(350)
line.penup()
line.goto(x=340, y=-150)
line.pendown()
line.forward(350)



user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race, Enter a Color: ")

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor()> 340:
            race_is_on = False
            win_color = turtle.pencolor()
            if win_color==user_bet:
                print(f"You Won!!! the {win_color} turtle wins")
            else:
                print(f"You lose!!! the {win_color} turtle wins")


        turtle.forward(randint(0,10))





