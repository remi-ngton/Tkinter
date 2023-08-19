from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window("My Application", "cyborg")

root.geometry('500x500')

# style
my_style = ttkb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))

my_button = ttkb.Button(text="Konnichiwa Sekai!", bootstyle="style", style="success.Outline.TButton", width=20)
my_button.pack(pady=40)

root.mainloop()
