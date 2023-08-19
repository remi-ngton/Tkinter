from tkinter import *
import ttkbootstrap as ttkb

root = ttkb.Window(title="Flood Gauge", themename="superhero")

root.geometry("1024x768")

def starter():
    # Start the gauge
    my_gauge.start()

def stoper():
    my_gauge.stop()


def incrementer():
    my_gauge.step(10)
    my_label.config(text=f"Position: {my_gauge.variable.get() +10}")

def decrementer():
    my_gauge.step(-10)

my_gauge = ttkb.Floodgauge(root, bootstyle="info", font=("Helvetica", 18), mask="Position: {}%", maximum=100, orient="vertical", value=50, mode="indeterminate")
my_gauge.pack(pady=50, fill=Y, expand=YES)

start_button = ttkb.Button(root, text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=10)

stop_button = ttkb.Button(root, text="Stop", bootstyle="danger outline", command=stoper)
stop_button.pack(pady=10)

increment_button = ttkb.Button(root, text="Increment", bootstyle="danger outline", command=incrementer)
increment_button.pack(pady=10)

decrement_button = ttkb.Button(text="Decrement", bootstyle="danger outline", command=decrementer)
decrement_button.pack(pady=10)

my_label = ttkb.Label(root, text="Position: ")
my_label.pack(pady=20)


root.mainloop()
