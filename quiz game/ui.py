from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUI:

    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=35, bg=THEME_COLOR)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=250, text="Question", fill=THEME_COLOR, font=("Ariel", 15, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 10, "bold"))
        self.score_label.grid(column=1, row=0)

        self.tic_pic = PhotoImage(file="images/true.png")
        self.true = Button(image=self.tic_pic, bg=THEME_COLOR, highlightthickness=0, command=self.true_ans)
        self.true.grid(row=2, column=1)

        self.cross_pic = PhotoImage(file="images/false.png")
        self.false = Button(image=self.cross_pic, bg=THEME_COLOR, highlightthickness=0, command=self.false_answer)
        self.false.grid(row=2, column=0)

        self.new_question()

        self.window.mainloop()

    def new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the End of the Quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_ans(self):
        user_answer = "true"
        self.answer_check(user_answer)

    def false_answer(self):
        user_answer = "false"
        self.answer_check(user_answer)

    def answer_check(self,answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(self.canvas, bg="green")
            self.window.after(1000, self.new_question)
        else:
            self.canvas.config(self.canvas, bg="red")
            self.window.after(1000, self.new_question)






