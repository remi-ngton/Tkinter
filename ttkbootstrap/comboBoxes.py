from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window("Combobox", "superhero")

root.geometry('1024x768')
def clicker():
    my_label.config(text=f"You clicked on {my_combo.get()}!")

# Create button click function
def click_bind(e):
    my_label.config(text=f"You clicked on {my_combo.get()}!")


#Create Label
my_label = ttkb.Label(root, text="Konnichiwa Sekai!", font=("Helvetica", 18))
my_label.pack(pady=30)

# Create dropdown options
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ,"Sunday"]

# Create Combobox
my_combo = ttkb.Combobox(root, bootstyle="success", value=days)
my_combo.pack(pady=20)

# Set Combo default
my_combo.current(0)

# Create a button
my_button = ttkb.Button(root, bootstyle="danger", text="Click Me?", command=clicker)
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)

root.mainloop()
