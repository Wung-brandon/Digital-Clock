import time
from tkinter import *


root = Tk()
root.title("Digital Clock")

def time_update():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000,time_update)

clock = Label(root,font=('ariel',40,'bold'),fg='white',bg='firebrick1')
clock.pack(fill=BOTH,expand=True)

time_update()

root.mainloop()