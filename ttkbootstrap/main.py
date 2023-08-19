from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttkb

root = ttkb.Window(themename="cyborg")
#root = Tk()
root.title("TTK Bootstrap")
root.geometry('500x600')

def checker():
    if (var1.get() or var2.get() or var3.get() or var4.get() or var5.get()) == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")

# Create a Label
my_label = Label(text="Click the checkbutton below!", font=("Helvetica", 18))
my_label.pack(pady=(40,10))

#CheckButton
var1 = IntVar()
my_check = ttkb.Checkbutton(bootstyle="primary", text="Check me out!", variable=var1, onvalue=1, offvalue=0, command=checker)
my_check.pack(pady=10)

# Toolbutton
var2 = IntVar()
my_check2 = ttkb.Checkbutton(bootstyle="danger, toolbutton, outline", text="ToolButton!!", variable=var2, onvalue=1, offvalue=0, command=checker)
my_check2.pack(pady=20)


# Outline Toolbutton
var3 = IntVar()
my_check3 = ttkb.Checkbutton(bootstyle="danger, toolbutton", text="Outline ToolButton!!", variable=var3, onvalue=1, offvalue=0, command=checker)
my_check3.pack(pady=30)

# round Toolbutton
var4 = IntVar()
my_check4 = ttkb.Checkbutton(bootstyle="success, round-toggle", text="Round Toggle!!", variable=var4, onvalue=1, offvalue=0, command=checker)
my_check4.pack(pady=40)

# square Toolbutton
var5 = IntVar()
my_check5 = ttkb.Checkbutton(bootstyle="success, square-toggle", text="Square Toggle!!", variable=var5, onvalue=1, offvalue=0, command=checker)
my_check5.pack(pady=40)


root.mainloop()

