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
checks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global title_label
    reps += 1

    # Turn them into seconds before counting
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    # If it's the 25-min work rep, count down WORK_MIN
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_min)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_min)
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_min)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    min = math.floor(count / 60) # floor() in math module: Return the largest integer <= x
    sec = count % 60
    if sec == 0:
        sec = "00"
    elif sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        # after(): Execute a command after a time delay
        global timer
        timer = window.after(1000, count_down, count - 1) # 1000 milliseconds = 1 second
    else:
        start_timer()
        global checks
        if reps % 2 == 0:
            checks += "✔️"
            check_label.config(text=checks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) # (103, 112) is the xcor and ycor of the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Title on the top of the tomato
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Start button
start_button = Button(text="Start", highlightthickness=0, width=5, command=start_timer)
start_button.grid(row=2, column=0)

# Reset button
reset_button = Button(text="Reset", highlightthickness=0, width=5, command=reset_timer)
reset_button.grid(row=2, column=2)

# Check
check_label = Label(bg=YELLOW)
check_label.grid(row=3, column=1)

window,mainloop()
