import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('800x600')

# First row frame
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, pady=10)

label1 = tk.Label(top_frame, text='Tkinter', bg='red', fg='white')
label2 = tk.Label(top_frame, text='Pack Layout', bg='green', fg='white')
label3 = tk.Label(top_frame, text='Fill', bg='blue', fg='white')
label4 = tk.Label(top_frame, text='Demo', bg='purple', fg='white')

# side=tk.TOP, BOTTOM, LEFT, RIGHT
# fill=tk.X ,Y, BOTH, NONE
# expand=True, False
# Internal paddings:ipadx, ipady
label1.pack(side=tk.LEFT, expand=True, fill=tk.X)
label2.pack(side=tk.LEFT, expand=False, ipadx=40)
label3.pack(side=tk.LEFT, expand=False, ipady=40)
label4.pack(side=tk.TOP, expand=True, fill=tk.BOTH, ipadx=80, ipady=80)

# Second row frame *****************
second_frame = tk.Frame(root)
second_frame.pack(fill=tk.X, pady=10)

# Anchor ‘n’, ‘e’, ‘s’, ‘w’, ‘ne’, ‘nw’, ‘se’, ‘sw’, or ‘center’
# box 1
box1 = tk.Label(second_frame, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, anchor=tk.E,  expand=True)

# box 2
box2 = tk.Label(second_frame, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, anchor=tk.W, expand=True)

# Third row frame *****************
third_frame = tk.Frame(root)
third_frame.pack(fill=tk.X, pady=10)

name_label = ttk.Label(third_frame, text="Name:")
name_label.pack(side=tk.LEFT, padx=5)

name_entry = ttk.Entry(third_frame)
name_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)


button = ttk.Button(third_frame, text="Submit")
button.pack(side=tk.LEFT, padx=5)

# Forth row frame *****************
forth_frame = tk.Frame(root)
forth_frame.pack(fill=tk.X, pady=10)

fields = {}

fields['username_label'] = ttk.Label(forth_frame, text='Username:')
fields['username'] = ttk.Entry(root)

fields['password_label'] = ttk.Label(forth_frame, text='Password:')
fields['password'] = ttk.Entry(root, show="*")


for field in fields.values():
    field.pack(anchor=tk.W, padx=10, pady=5, fill=tk.X)

ttk.Button(text='Login').pack(anchor=tk.W, padx=10, pady=10)


root.mainloop()
