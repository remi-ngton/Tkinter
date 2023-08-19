from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window(title="Entry Box", themename="superhero")

root.geometry("1024x768")

# Create Entry Function
def speak():
    my_label.config(text=f"You typed {my_entry.get()}!")

# Create Enrty Widget
my_entry = ttkb.Entry(root, bootstyle="success", font=("Helvetica", 18), foreground="green", width=15, show="*")
my_entry.pack(pady=50)


# Create Button
my_button = ttkb.Button(root, bootstyle="danger outline", text="Click ME!", command=speak)
my_button.pack(pady=20)

# Create Label
my_label = ttkb.Label(root, text="")
my_label.pack(pady=20)


root.mainloop()
