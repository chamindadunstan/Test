import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('350x200')
        self.title('TTK State Demo')

        # Button widget
        button = ttk.Button(self, text='Demo Button')
        button.pack(pady=20)

        # Style configuration
        style = ttk.Style(self)
        style.configure('TButton', font=('Helvetica', 16))

        # Map all states separately
        style.map(
            'TButton',
            foreground=[
                ('active', 'red'),         # mouse over
                ('pressed', 'blue'),       # button pressed
                ('disabled', 'gray'),      # disabled
                ('focus', 'green'),        # widget has focus
                ('background', 'purple'),  # window not focused (Win/macOS)
                ('readonly', 'orange'),    # readonly state
                ('selected', 'brown'),     # selected (e.g., radio/checkbox)
                ('alternate', 'pink'),     # reserved for app use
                ('invalid', 'yellow')      # invalid input
            ]
        )

        # Buttons to toggle states
        ttk.Button(self, text="Disable Button",
                   command=lambda: button.state(['disabled'])).pack()

        ttk.Button(self, text="Enable Button",
                   command=lambda: button.state(['!disabled'])).pack()

        ttk.Button(self, text="Focus Button",
                   command=lambda: button.focus_set()).pack()

        ttk.Button(self, text="Mark Invalid",
                   command=lambda: button.state(['invalid'])).pack()

        ttk.Button(self, text="Clear Invalid",
                   command=lambda: button.state(['!invalid'])).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
