from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            self.highest_score = int(file.read())

    def __int__(self):
        super().__init__()
        self.highest_score = 0

    def score(self,value):
        self.color("white")
        self.penup()
        self.ht()
        self.goto(-290, 270)
        self.clear()
        self.write(f"Score: {value}                Highest Score: {int(self.highest_score)}", False, align="left", font=("Courier", 18, "normal"))

    def update(self, value):

        if value > int(self.highest_score):
            self.highest_score = value
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highest_score}")






