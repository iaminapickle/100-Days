from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = round(miles * 1.609344, 2)
    km_label.config(text = f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width = 300, height = 150)
window.config(padx = 50, pady = 50)

input = Entry(width = 10)
input.grid(row = 0, column = 1)

label1 = Label(text = "Miles")
label1.grid(row = 0, column = 2)

label2 = Label(text = "is equal to")
label2.grid(row = 1, column = 0)

label3 = Label(text = "Km")
label3.grid(row = 1, column = 3)

km_label = Label(text = "0")
km_label.grid(row = 1, column = 1)

button = Button(text = "Convert", command = button_clicked)
button.grid(row = 2, column = 1)

window.mainloop()
