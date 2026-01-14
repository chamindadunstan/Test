import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import webbrowser

root = tk.Tk()
root.title("Text Widget Example")

# Adding a scrollbar to a Text widget
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# create a scrollbar and add it to the frame
v_scrollbar = ttk.Scrollbar(frame)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# create a text widget and add it to the frame
text = tk.Text(frame, height=8)
text.config(
    font=("Consolas", 12),
    fg="#CA1C1C",
    bg="#282C34",
    insertbackground="white"
)
text.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# configure scrollbar
text['yscrollcommand'] = v_scrollbar.set
v_scrollbar.config(command=text.yview)

# insert some text into the text widget
text.insert(tk.END, "\n" * 20)

text.insert(
    index='1.0',
    chars='Click here to visit pythontutorial.net'
)

# add link
text.tag_add("link", "1.0", "1.10")
text.tag_config("link", foreground="blue", underline=True)

# link click
text.tag_bind(
    "link",
    "<Button-1>",
    lambda e: webbrowser.open("https://www.pythontutorial.net")
)

# link hover
text.tag_bind(
    "link",
    "<Enter>",
    lambda e: text.config(cursor="hand2")
)

# link leave
text.tag_bind(
    "link",
    "<Leave>",
    lambda e: text.config(cursor="")
)

# embed an image
image = tk.PhotoImage(file="./assets/python.png")
text.image_create("1.0", image=image)

# get text button
get_button = ttk.Button(
    root,
    text='Get Text',
    command=lambda: showinfo(
        title='Text Data',
        message=text.get('2.0', tk.END)
    )
)
get_button.pack(padx=10, pady=10, side=tk.LEFT)

# clear text button
clear_button = ttk.Button(
    root,
    text='Clear All Text',
    command=lambda: text.delete('1.0', tk.END)
)

clear_button.pack(padx=10, pady=10, side=tk.RIGHT)


root.mainloop()
