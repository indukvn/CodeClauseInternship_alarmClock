from tkinter import *
from tkinter import messagebox
import time, sys
from PIL import Image, ImageTk
from pygame import mixer

root = Tk()
root.title("Alarm Clock")
root.geometry("450x455")
canvas = Canvas(root, width=450, height=455)
image = ImageTk.PhotoImage(Image.open("alarm.jpg"))
canvas.create_image(0, 0, anchor= NW, image= image)
canvas.pack()
header = Frame(root)


def alarm():
    alarm_time = timing.get()
    if alarm_time == "":
        messagebox.askretrycancel("Error", "Please Set Alarm Timing")

    while True:
        time.sleep(1)
        if alarm_time == time.strftime("%H:%M"):
            playmusic()


def playmusic():
    mixer.init()
    mixer.music.load("alarm.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(30)
        mixer.music.stop()
        sys.exit()


input_time = Frame(root)
input_time.place(x=80, y=385)

btn = Frame(root)
btn.place(x=260, y=380)

timing = Entry(input_time, font=("Arial Narrow", 20), width=8)
timing.grid(row=0, column=2)

set_btn = Button(btn, text= "Set Alarm", font=("Arial Narrow", 16, "bold"), command=alarm)
set_btn.grid(row=2, column=2)


root.mainloop()