import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Example")
root.geometry("300x150")


def say_hello():
    print("Hello Tkinter!")


# Change Button Colors (bg, fg, active colors)
btn = tk.Button(
    root,
    text="Say Hello",
    command=say_hello,
    bg="#4CAF50",  # background color
    fg="white",  # text color
    activebackground="#45a049",
    activeforeground="white",
)
btn.pack()

# Change Font, Size, Weigh
btn = tk.Button(
    root,
    text="Styled Button",  # text="Disabled",
    font=("Segoe UI", 14, "bold"),
    state="normal",  # normal, active, disabled
)
btn.pack(pady=5)

# Change Border, Relief, and Thicknes
btn = tk.Button(
    root,
    text="Flat Button",
    relief="flat",  # flat, raised, sunken, groove, ridge
    bd=2,  # border width
)
btn.pack(pady=5)

# Rounded‑corner buttons (using highlightthickness trick)
btn = tk.Button(
    root,
    text="Rounded",
    bg="#2196F3",
    fg="white",
    relief="flat",
    highlightthickness=0,
    padx=15,
    pady=8,
)
btn.pack(pady=5)

# Full Modern Button Example (like Windows Calculator)
btn = tk.Button(
    root,
    text="7",
    font=("Segoe UI", 16),
    bg="#f3f3f3",
    fg="black",
    activebackground="#e5e5e5",
    activeforeground="black",
    relief="flat",
    bd=0,
    padx=20,
    pady=10,
)
btn.pack(pady=5)


# Hover Effects (very useful for modern UI
def on_enter(e):
    btn["background"] = "#555555"


def on_leave(e):
    btn["background"] = "#333333"


btn = tk.Button(
    root, text="Hover Me",
    bg="#333333",
    fg="white",
    relief="flat",
    padx=10,
    pady=5
)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)
btn.pack(pady=5)

# Button With Image (icons)
icon = tk.PhotoImage(file="assets/icon.png")

btn = tk.Button(
    root,
    image=icon,
    command=say_hello,
    relief="flat",
    bg="white"
)
btn.image = icon  # type: ignore[attr-defined]
btn.pack()


label = tk.Label(root, text="Click the button below")
label.pack(pady=10)

btn = tk.Button(root, text="Say Hello", command=say_hello)
btn.pack()

root.mainloop()
