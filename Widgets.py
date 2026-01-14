import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# main window
root = tk.Tk()
root.geometry("1000x500")
root.resizable(False, False)
root.title("Button Demo")

# exit button
exit_button = ttk.Button(root, text="Exit", command=lambda: root.quit())

exit_button.pack(ipadx=5, ipady=5, expand=True)


# download button handler
def handle_click():
    showinfo(
        title="Information",
        message="Download button clicked!"
    )


download_icon = tk.PhotoImage(file="./assets/download.png")
download_button = ttk.Button(
    root, image=download_icon,
    text="Download",
    compound=tk.LEFT,
    command=handle_click
)

download_button.pack(
    ipadx=15,
    ipady=15,
    expand=True)


root.mainloop()
root.mainloop()
