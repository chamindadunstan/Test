import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter.colorchooser import askcolor


class FileDialogApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter File Dialog (OOP)")
        self.resizable(False, False)
        self.geometry("550x250")

        # Row height distribution
        self.rowconfigure(0, weight=1)  # 10%
        self.rowconfigure(1, weight=1)  # 10%
        self.rowconfigure(2, weight=7)  # 70%
        self.rowconfigure(3, weight=1)  # 10%

        self.columnconfigure(0, weight=1)

        self.create_widgets()

    # ---------------------------------------------------
    # UI Setup
    # ---------------------------------------------------
    def create_widgets(self):
        # Row 0: Open Files button
        self.open_files_btn = ttk.Button(
            self, text="Open Files", command=self.select_files
        )
        self.open_files_btn.grid(column=0, row=0, sticky="w", padx=10, pady=5)

        # Row 1: Text editor
        self.text = tk.Text(self, height=12)
        self.text.grid(column=0, row=1, sticky="nsew")

        # Row 2: Open a File button
        self.open_file_btn = ttk.Button(
            self, text="Open a File", command=self.open_text_file
        )
        self.open_file_btn.grid(column=0, row=2, sticky="w", padx=10, pady=5)

        # Row 3: Open a File button
        self.open_file_btn = ttk.Button(
            self, text="Select a Color", command=self.change_color
        )
        self.open_file_btn.grid(column=0, row=2, sticky="e", padx=10, pady=5)

    # ---------------------------------------------------
    # Logic
    # ---------------------------------------------------
    def select_files(self):
        filetypes = (("text files", "*.txt"), ("All files", "*.*"))

        filenames = fd.askopenfilenames(
            title="Open files", initialdir="/", filetypes=filetypes
        )

        if filenames:
            showinfo(title="Selected Files", message="\n".join(filenames))

    def open_text_file(self):
        filetypes = (("text files", "*.txt"), ("All files", "*.*"))

        f = fd.askopenfile(filetypes=filetypes)
        if f is None:
            return

        self.text.insert("1.0", f.read())
        f.close()

    def change_color(self):
        colors = askcolor(title="Tkinter Color Chooser")
        if colors[1] is not None:
            self.configure(bg=colors[1])


if __name__ == "__main__":
    app = FileDialogApp()
    app.mainloop()
