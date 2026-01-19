import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Widgest Demo')


# Configure grid: 3 rows, 2 columns
root.rowconfigure(0, weight=1)  # Frame 1 & 2
root.rowconfigure(1, weight=2)  # Frame 3
root.rowconfigure(2, weight=1)  # Frame 4

root.columnconfigure(0, weight=1)  # Left side (Frame 1)
root.columnconfigure(1, weight=1)  # Right side (Frame 2)

# Frame 1 — top left
frame_1 = tk.Frame(root, bg="lightblue", bd=2, relief="groove")
frame_1.grid(row=0, column=0, sticky="nsew")
ttk.Label(
    frame_1, text="Frame 1_Tkinter slider", foreground="red"
    ).grid(row=0, column=0, columnspan=2, pady=5)

# Frame 2 — top right
frame_2 = tk.Frame(root, bg="lightgreen", bd=2, relief="groove")
frame_2.grid(row=0, column=1, sticky="nsew")
ttk.Label(
    frame_2, text="Frame 2_Tkinter Spinbox", foreground="red"
    ).pack(pady=5)

# Frame 3 — middle full width
frame_3 = tk.Frame(root, bg="lightgray", bd=2, relief="groove")
frame_3.grid(row=1, column=0, columnspan=2, sticky="nsew")
# Make two equal columns
frame_3.columnconfigure(0, weight=1)
frame_3.columnconfigure(1, weight=1)
# Title
ttk.Label(
    frame_3, text="Frame 3_Tkinter LabelFrame", foreground="red"
).grid(row=0, column=0, columnspan=2, pady=5)


# Frame 4 — bottom full width
frame_4 = tk.Frame(root, bg="lightyellow", bd=2, relief="groove")
frame_4.grid(row=2, column=0, columnspan=2, sticky="nsew")
ttk.Label(
    frame_4, text="Frame 4_Tkinter Checkbox", foreground="red"
    ).grid(row=0, column=0, pady=5)

# Separator after radio buttons
# or ttk.Separator cant use height=2, bg="red"
separator1 = tk.Frame(frame_3, width=2, bg="red")
separator1.grid(row=1, column=0, sticky="ns", padx=20, pady=10)


# ----------------------
# slider current value
current_value = tk.DoubleVar()


def get_current_value():
    return '{: .2f}'.format(current_value.get())


def slider_changed(event):
    value_label.configure(text=get_current_value())


# label for the slider
slider_label = ttk.Label(
    frame_1,
    text='Slider:'
)

slider_label.grid(
    row=1,
    column=0,
    sticky='w'
)

#  slider
slider = ttk.Scale(
    frame_1,
    from_=0,
    to=100,
    orient='horizontal',  # horizontal/vertical
    command=slider_changed,
    variable=current_value
)

slider.grid(
    row=1,
    column=1,
    sticky='we'
)

# current value label
current_value_label = ttk.Label(
    frame_1,
    text='Current Value:'
)

current_value_label.grid(
    row=2,
    columnspan=2,
    sticky='n',
    ipadx=10,
    ipady=10
)

# value label
value_label = ttk.Label(
    frame_1,
    text=get_current_value()
)
value_label.grid(
    row=3,
    columnspan=2,
    sticky='n'
)

# ----------------------

# Spinbox
current_value1 = tk.StringVar()
spin_box = ttk.Spinbox(
    frame_2,
    from_=0,
    to=50,
    # values=("0", "10", "20", "30", "40", "50"),
    textvariable=current_value1,
    wrap=True)

spin_box.pack()

# ----------------------
# LabelFrame inside Frame 3 (LEFT)
lf = ttk.LabelFrame(frame_3, text='Alignment')
lf.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

alignment_var = tk.StringVar()
alignments = ('Left', 'Center', 'Right')

# create radio buttons and place them on the label frame

grid_column = 0
for alignment in alignments:
    # create a radio button
    radio = ttk.Radiobutton(
        lf, text=alignment, value=alignment, variable=alignment_var)
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    # grid column
    grid_column += 1

# ----------------------
# label frame Anchor
# LabelFrame on the RIGHT
lf_anchor = ttk.LabelFrame(frame_3, text='Label Anchor')
lf_anchor.grid(row=1, column=1,  padx=20, pady=20, sticky=tk.NSEW)

anchor_var = tk.StringVar()
anchors = {
    'nw': {'row': 0, 'column': 1},
    'n': {'row': 0, 'column': 2},
    'ne': {'row': 0, 'column': 3},
    'en': {'row': 1, 'column': 4},
    'e': {'row': 2, 'column': 4},
    'es': {'row': 3, 'column': 4},
    'se': {'row': 4, 'column': 3},
    's': {'row': 4, 'column': 2},
    'sw': {'row': 4, 'column': 1},
    'ws': {'row': 3, 'column': 0},
    'w': {'row': 2, 'column': 0},
    'wn': {'row': 1, 'column': 0}
}


def change_label_anchor():
    lf_anchor['labelanchor'] = anchor_var.get()


# create radio buttons and place them on the label frame
for key, value in anchors.items():
    # create a radio button
    radio = ttk.Radiobutton(
        lf_anchor,
        text=key.upper(),
        value=key,
        command=change_label_anchor,
        variable=anchor_var
    ).grid(row=value['row'], column=value['column'], padx=5, pady=5)


# set the radio button selected
anchor_var.set(lf_anchor['labelanchor'])

# ----------------------
# progressbar


def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    if pb['value'] < 100:
        pb['value'] += 20
        value_label['text'] = update_progress_label()
    else:
        showinfo(message='The progress completed!')


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


pb = ttk.Progressbar(
    frame_4,
    orient='horizontal',
    mode='determinate',  # determinate/indeterminate
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    frame_4,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    frame_4,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


# ----------------------


root.mainloop()
