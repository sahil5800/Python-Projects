import turtle
import pandas

screen = turtle.Screen()
screen.screensize(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
n = 0

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while n != 50:
    user_input = screen.textinput(title=f"Guess the State {n}/50", prompt="Your guess:").title()
    if user_input in all_states:
        n += 1
        answer = turtle.Turtle()
        answer.ht()
        answer.penup()
        city_name = data[data["state"] == f"{user_input}"]
        answer.goto(int(city_name.x), int(city_name.y))
        answer.write(user_input)
    elif user_input == "Exit":
        break
    else:
        pass
