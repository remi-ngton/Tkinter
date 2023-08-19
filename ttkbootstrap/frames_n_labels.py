from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window(title="Frames and Labels", themename="cyborg")

root.geometry('1024x768')


def thing():
    pass


my_frame = Frame(root)#, bootstyle="dark")
my_frame.pack(pady=40)

my_entry = ttkb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(padx=20, pady=20)

my_button = ttkb.Button(my_frame, text="Click Me!", bootstyle="dark", command=thing)
my_button.pack(pady=20, padx=20)

my_label = ttkb.Label(root, text="Hello There!", font=("Helvetica", 18), bootstyle="dark inverse")
my_label.pack(pady=20)

root.mainloop()
