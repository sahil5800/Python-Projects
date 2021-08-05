from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
r = 1
marks = ""
clock = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(clock)
    global r
    r = 1
    canvas.itemconfig(time, text="00:00")
    timer.config(text="TIMER")
    global marks
    marks = ""
    tick.config(text=marks)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_min = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    global r
    if r % 8 == 0:
        count_down(long)
        r += 1
        timer.config(text="BREAK", bg=RED, fg="white")
    elif r % 2 == 0:
        count_down(short)
        r += 1
        timer.config(text="BREAK", fg=RED)
    else:
        count_down(work_min)
        r += 1
        timer.config(text="TIMER", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    global marks
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if r % 2 == 0:
            marks += "✔"
            tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
time = canvas.create_text(100, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, bg=RED, fg="white")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=RED, fg="white", command=reset)
reset_button.grid(column=2, row=2)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick.grid(column=1, row=3)


window.mainloop()
