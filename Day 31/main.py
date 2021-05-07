from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

WIDTH = 800
HEIGHT = 526

def change():
    global rand_word
    rand_word = random.choice(list(data))
    canvas.itemconfig(canvas_Image, image = cardFlip_Image)
    canvas.itemconfig(word, text = rand_word["English"], fill = "white")
    canvas.itemconfig(lang, text = "English", fill = "white")

def no():
    global cur
    window.after_cancel(cur)
    rand_word = random.choice(list(data))
    canvas.itemconfig(canvas_Image, image = card_Image)
    canvas.itemconfig(word, text = rand_word["French"], fill = "black")
    canvas.itemconfig(lang, text = "French", fill = "black")
    cur = window.after(3000, change)

def yes():
    global cur
    global data
    window.after_cancel(cur)
    rand_word = random.choice(list(data))
    data.remove(rand_word)

    canvas.itemconfig(canvas_Image, image = card_Image)
    canvas.itemconfig(word, text = rand_word["French"], fill = "black")
    canvas.itemconfig(lang, text = "French", fill = "black")

    tmp = pandas.DataFrame(data)
    tmp.to_csv("data/words_to_learn.csv", index = False)

    cur = window.after(3000, change)

try:
    df = pandas.read_csv("data/words_to_learn.csv")
except:
    df = pandas.read_csv("data/french_words.csv")

data = df.to_dict('records')

window = Tk()
window.title("Flashcard App")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
cur = window.after(3000, change)

cardFlip_Image = PhotoImage(file = "images/card_back.png")
card_Image = PhotoImage(file = "images/card_front.png")
canvas = Canvas(height = HEIGHT, width = WIDTH, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas_Image = canvas.create_image(0, 0, image = card_Image, anchor = NW)
lang = canvas.create_text(400, 150, text = "French", font = ("Ariel", 40, "italic"))

rand_word = random.choice(list(data))
word = canvas.create_text(400, 263, text = rand_word["French"], font = ("Ariel", 80, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

no_Image = PhotoImage(file = "images/wrong.png")
no_Button = Button(image = no_Image, highlightthickness = 0, command = no)
no_Button.grid(row = 1, column = 0)

yes_Image = PhotoImage(file = "images/right.png")
yes_Button = Button(image = yes_Image, highlightthickness = 0, command = yes)
yes_Button.grid(row = 1, column = 1)

window.mainloop()
