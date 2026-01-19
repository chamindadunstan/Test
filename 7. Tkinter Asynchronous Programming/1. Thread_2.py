import tkinter as tk
from tkinter import ttk
import time
from threading import Thread


def task():
    # Simulate a long-running task
    for i in range(5):
        print(f"Task running... {i+1}/5")
        time.sleep(1)

    print("Task completed!")


def handle_click():
    t = Thread(target=task)
    t.start()


root = tk.Tk()
root.geometry("300x100")
root.title("Tkinter Thread Example")

button = ttk.Button(
    root,
    text="Start Thread",
    command=handle_click
)
button.pack(padx=10, pady=10)

root.mainloop()
