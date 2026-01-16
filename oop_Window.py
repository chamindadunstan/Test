import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# Tkinter Object-Oriented Window
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x50')

        # create and place the main frame
        MainFrame(self).pack(fill="both", expand=True)


# Tkinter Object-Oriented Frames
class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.options = {'fill': 'both', 'padx': 5, 'pady': 5, 'ipadx': 5}

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack(**self.options)

        # button
        self.button = ttk.Button(
            self, text='Click Me', command=self.button_clicked)
        self.button.pack(**self.options)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')


# run the app
if __name__ == "__main__":
    app = App()
    app.mainloop()
