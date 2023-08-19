from tkinter import *
import ttkbootstrap as ttkb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = ttkb.Window(title="Date Entry", themename="cyborg")

root.geometry("1024x768")


def datey():
    my_label.config(text=f"You Picked: {my_date.entry.get()}")


def thing():
    cal = Querybox
    my_label.config(text=f"You Picked: {cal.get_date()}")
my_date = ttkb.DateEntry(root, bootstyle="info", startdate=date(2022, 11, 21), firstweekday=0)
my_date.pack(pady=50)

my_button = ttkb.Button(root, text="Get Date", bootstyle="danger outline", command=datey)
my_button.pack(pady=20)

my_button2 = ttkb.Button(root, text="Get Calendar", bootstyle="success outline", command=thing)
my_button2.pack(pady=20)

my_label = ttkb.Label(root, text="You Picked: ")
my_label.pack(pady=20)

root.mainloop()
