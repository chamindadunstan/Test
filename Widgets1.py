import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from calendar import month_name

# create the main window
root = tk.Tk()
root.geometry("800x400")
root.title("Structured Layout")
root.resizable(True, True)

# create the sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=2, column=1, sticky=tk.SE)

# Configure grid: 3 rows, 2 columns
root.rowconfigure(0, weight=1)  # Frame 1
root.rowconfigure(1, weight=3)  # Frame 2 & 4
root.rowconfigure(2, weight=1)  # Frame 3

root.columnconfigure(0, weight=1)  # Left side (Frame 2)
root.columnconfigure(1, weight=1)  # Right side (Frame 4)

# Frame 1 — top full width
frame_1 = tk.Frame(root, bg="lightblue", bd=2, relief="groove")
frame_1.grid(row=0, column=0, columnspan=2, sticky="nsew")
ttk.Label(
    frame_1, text="Frame 1_Tkinter Listbox", foreground="red").pack(pady=10)
# PanedWindow INSIDE frame_1
pw = ttk.PanedWindow(frame_1, orient=tk.HORIZONTAL)
pw.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Frame 2 — bottom left
frame_2 = tk.Frame(root, bg="lightgreen", bd=2, relief="groove")
frame_2.grid(row=1, column=0, sticky="nsew")
ttk.Label(
    frame_2, text="Frame 2_Tkinter Radio Button", foreground="red"
    ).pack(pady=10)

# Frame 4 — bottom right
frame_4 = tk.Frame(root, bg="lightyellow", bd=2, relief="groove")
frame_4.grid(row=1, column=1, sticky="nsew")
ttk.Label(
    frame_4, text="Frame 4_Tkinter Checkbox", foreground="red").pack(pady=10)


# Frame 3 — bottom full width
frame_3 = tk.Frame(root, bg="lightgray", bd=2, relief="groove")
frame_3.grid(row=2, column=0, columnspan=2, sticky="nsew")
ttk.Label(
    frame_3, text="Frame 3_Tkinter Combobox", foreground="red").pack(pady=10)

# Horizontal separator between Frame 1 and Frame 2/4
separator1 = ttk.Separator(root, orient=tk.HORIZONTAL)
separator1.grid(row=0, column=0, columnspan=2, sticky="ew", pady=5)
# Vertical separator between Frame 2 and Frame 4
separator2 = ttk.Separator(root, orient=tk.VERTICAL)
separator2.grid(row=1, column=1, sticky="ns", padx=5)

# Tkinter PanedWindow ---------------------------------------------------
# change style to classic (Windows only)
# to show the sash and handle
style = ttk.Style()
style.theme_use('classic')


# Frame 1 ---------------------------------------------------
# Left listbox
# create a variabe object
languages = (
    "Java", "C", "C++", "C#", "Python", "Go", "JavaScript", "PHP", "Swift")

list_variable = tk.Variable(value=languages)


# label inside frame_1
label = ttk.Label(frame_1, text="Select your favorite programming languages:")
label.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)
# listbox inside frame_1
left_listbox = tk.Listbox(
    pw,
    listvariable=list_variable,
    height=6,
    selectmode=tk.MULTIPLE,
)
pw.add(left_listbox)  # pannel window


def handle_item_select(event):
    selected_indices = left_listbox.curselection()
    selected_languages = ",".join(
        [left_listbox.get(i) for i in selected_indices])

    showinfo(
        title="Information", message=f"You selected: {selected_languages}")


left_listbox.bind("<<ListboxSelect>>", handle_item_select)

# Right listbox
right_list = tk.Listbox(pw)
pw.add(right_list)

# place the panedwindow on the root window
pw.pack(fill=tk.BOTH, expand=True)


# ---------------- Frame 2 CONTENT ---------------- #
def show_selected_size():
    showinfo(title="Result", message=selected_size.get())


selected_size = tk.StringVar()
sizes = (
    ("Small", "S"),
    ("Medium", "M"),
    ("Large", "L"),
    ("Extra Large", "XL"),
    ("Extra Extra Large", "XXL"),
)

# label inside frame_2
label = ttk.Label(frame_2, text="What's your t-shirt size?")
label.pack(fill="x", padx=5, pady=5)

# radio buttons inside frame_2
for size in sizes:
    r = ttk.Radiobutton(
        frame_2, text=size[0], value=size[1], variable=selected_size)
    r.pack(fill="x", padx=5, pady=5)

# button inside frame_2
button = ttk.Button(
    frame_2, text="Get Selected Size", command=show_selected_size)

button.pack(fill="x", padx=5, pady=5)

# ---------------- Frame 3 CONTENT ---------------- #
# label
label = ttk.Label(frame_3, text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(frame_3, textvariable=selected_month)

# get first 3 letters of every month name
month_cb["values"] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb["state"] = "readonly"

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """handle the month changed event"""
    showinfo(title="Result", message=f"You selected {selected_month.get()}!")


month_cb.bind("<<ComboboxSelected>>", month_changed)


# ---------------- Frame 4 CONTENT ---------------- #
def show_message():
    showinfo(
        title='Result',
        message='You agreed.' if agreement_var.get() else 'You did not agree.'
    )


agreement_var = tk.BooleanVar()

checkbox = ttk.Checkbutton(
    frame_4,
    text='I agree',
    command=show_message,
    variable=agreement_var
)

checkbox.pack()
# ---------------------------------------------------

root.mainloop()
