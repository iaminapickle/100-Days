from tkinter import *
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
timer_flag = False
timer = None
WIDTH = 400
HEIGHT = 300
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global timer_flag

    window.after_cancel(timer)
    label.config(text = "Timer!", fg = GREEN)
    tick.config(text = "")
    canvas.itemconfig(timer_text, text = "00:00")
    reps = 0
    timer_flag = False
# ---------------------------- TIMER MECHANISM ------------------------------- #
def update_text(min):
    if reps % 2 == 1:
        label.config(text = "Work!", fg = GREEN)
    elif reps % 8 == 0:
        label.config(text = "Long Break!", fg = RED)
    else:
        label.config(text = "Short Break!", fg = PINK)

def start_timer():
    if timer_flag == True:
        return

    global reps
    reps += 1

    if reps % 2 == 1:
        min = 0.25
    elif reps % 8 == 0:
        min = LONG_BREAK_MIN
    else:
        min = SHORT_BREAK_MIN

    if reps % 2 == 0:
        if len(tick["text"]) == 4:
            string = ""
        else:
            string = tick["text"] + "\u2713"
        tick.config(text = string, font = (FONT_NAME, 20, "bold"))

    update_text(min)
    count_down(min * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_flag
    global timer

    timer_flag = True

    if count == 0:
        timer_flag = False
        start_timer()
        return

    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"

    minutes = int(count // 60)
    if minutes < 10:
        minutes = f"0{minutes}"

    string = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text = string)
    timer = window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)
window.resizable(False, False)


canvas = Canvas(width = WIDTH, height = HEIGHT, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(WIDTH / 2, HEIGHT / 2, image = tomato_img)
timer_text = canvas.create_text(WIDTH / 2, HEIGHT / 2, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 35, "bold"))
label.grid(row = 0, column = 1)

start_button = Button(text = "Start", width = 4, command = start_timer)
start_button.grid(row = 2, column = 0)

reset_button = Button(text = "Reset", width = 4, command = reset_timer)
reset_button.grid(row = 2, column = 3)

tick = Label(text = "", bg = YELLOW)
tick.grid(row = 3, column = 1)

window.mainloop()
