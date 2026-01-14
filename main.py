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

label = tk.Label(root, text="Click the button below")
label.pack(pady=10)

btn = tk.Button(root, text="Say Hello", command=say_hello)
btn.pack()

root.mainloop()
