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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer() :
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Title_label.config(text="Pomodoro Timer")
    checkmark_label.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        Title_label.config(fg=RED, text="Take a long Break!!")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        Title_label.config(fg=PINK, text="Take a short break!")
    else:
        count_down(work_sec)
        Title_label.config(fg=GREEN, text="Work time!")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    elif count_seconds == 0:
        count_seconds = "00"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        checkmark_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=75, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

Title_label = Label(text="Pomodoro Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
Title_label.grid(row=0, column=1)

start_button = Button(text="start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(font=FONT_NAME, fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

window.mainloop()
