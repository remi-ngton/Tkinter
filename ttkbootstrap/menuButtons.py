from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window(title="Menu Button",themename="cyborg")

root.geometry('1024x768')

def stuff(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=f"You selected {x}")


my_menu = ttkb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=20)

# Create basic menu
inside_menu = ttkb.Menu(my_menu)

# Add items to inside menu
items_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info', 'outline primary', 'outline secondary', 'outline danger', 'outline info']:
    inside_menu.add_radiobutton(label=x, variable=items_var, command=lambda x=x: stuff(x))

# Associate the inside menu with the menubutton
my_menu['menu'] = inside_menu

# Create a label
my_label = ttkb.Label(root, text="")
my_label.pack(pady=40)

root.mainloop()
