import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x110')
        self.resizable(False, False)
        self.title('Login')

        # UI options
        self.paddings = {'padx': 5, 'pady': 5}
        self.style = ttk.Style(self)
        self.style.configure('Custom.TEntry', font=('Helvetica', 11))

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, **self.paddings)

        username_entry = ttk.Entry(
            self, textvariable=username, style='Custom.TEntry'
        )
        username_entry.grid(column=1, row=0, sticky=tk.E, **self.paddings)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, **self.paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", style='Custom.TEntry')
        password_entry.grid(column=1, row=1, sticky=tk.E, **self.paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **self.paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('custom.TLabel', font=('Helvetica', 11))
        self.style.configure('customTButton', font=('Helvetica', 11))


if __name__ == "__main__":
    app = App()
    app.mainloop()
