import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


root = tk.Tk()
root.geometry('400x300')
root.title('IntVar Demo')


quantity_var = tk.IntVar()

label = ttk.Label(root, text='Quantity:')
label.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)

quantity_entry = ttk.Entry(root, textvariable=quantity_var)
quantity_entry.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)


button = ttk.Button(
    root,
    text='Submit',
    command=lambda: showinfo(title='Quantity', message=str(quantity_var.get()))
)

button.pack(side=tk.LEFT, padx=5, pady=10, anchor=tk.W)

root.mainloop()
