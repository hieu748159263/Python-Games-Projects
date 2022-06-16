from tkinter import *
from time import strftime


def update():

    time_string = strftime('%I:%M:%S %p')
    time_label.config(text=time_string)
    date_string = strftime('%A, %B %d, %Y')
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Clock")
clock_icon = PhotoImage(file='watch.png')
window.iconphoto(True, clock_icon)

time_label = Label(window, font=("Arial", 50))
time_label.pack()
date_label = Label(window, font=("Ink Free", 30), fg="#FFFFFF", bg="black")
date_label.pack()

update()
window.mainloop()
