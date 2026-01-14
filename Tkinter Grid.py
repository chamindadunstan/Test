import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry("400x400")
root.title('Login')


# grid 3x2
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)


# username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=0, sticky=tk.EW, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

# password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=1, sticky=tk.EW, padx=5, pady=5)

password_entry = ttk.Entry(root,  show="*")
password_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

# login button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


# image below login btn (row 2)
img = tk.PhotoImage(file="assets/Tkinter Grid.png")
image_label = tk.Label(root, image=img)
image_label.image = img                     # type: ignore[attr-defined]
image_label.grid(column=0, row=4, columnspan=2, pady=5)


root.mainloop()
