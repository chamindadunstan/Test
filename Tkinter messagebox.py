import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo, askyesno
from tkinter.messagebox import askokcancel, WARNING, askretrycancel


class MessageBoxApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MessageBox (OOP)')
        self.resizable(False, False)
        self.geometry('300x350')

        self.options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}

        self.create_widgets()

    def create_widgets(self):
        ttk.Button(
            self,
            text='Show an error message',
            command=self.show_error
        ).pack(**self.options)

        ttk.Button(
            self,
            text='Show an information message',
            command=self.show_info
        ).pack(**self.options)

        ttk.Button(
            self,
            text='Show a warning message',
            command=self.show_warning
        ).pack(**self.options)

        ttk.Button(
            self,
            text='Ask Yes/No',
            command=self.confirm_askyesno
        ).pack(**self.options)

        ttk.Button(
            self,
            text='Delete All',
            command=self.confirm_askokcancel
        ).pack(**self.options)

        ttk.Button(
            self,
            text='Connect to the Database Server',
            command=self.confirm_askretrycancel
        ).pack(**self.options)
    # ---------------------------
    # Messagebox handlers (OOP)
    # ---------------------------

    # showerror
    def show_error(self):
        showerror(
            title='Error',
            message='This is an error message.'
        )

    # showinfo
    def show_info(self):
        showinfo(
            title='Information',
            message='This is an information message.'
        )

    # showwarning
    def show_warning(self):
        showwarning(
            title='Warning',
            message='This is a warning message.'
        )

    # askyesno
    def confirm_askyesno(self):
        answer = askyesno(
            title='Confirmation',
            message='Are you sure that you want to quit?'
        )
        if answer:
            self.destroy()

    # askokcancel
    def confirm_askokcancel(self):
        answer = askokcancel(
            title='Confirmation',
            message='Deleting will delete all the data.',
            icon=WARNING)

        if answer:
            showinfo(
                title='Deletion Status',
                message='The data is deleted successfully')

    # askretrycancel
    def confirm_askretrycancel(self):
        answer = askretrycancel(
            title='Connection Issue',
            message='The database server is unreachable. Do you want to retry?'
        )
        if answer:
            showinfo(
                title='Information',
                message='Attempt to connect to the database again.')


if __name__ == "__main__":
    app = MessageBoxApp()
    app.mainloop()
