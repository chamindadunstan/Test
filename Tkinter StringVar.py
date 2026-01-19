import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title('Change Password')
root.geometry("300x200")

ERROR = 'Error.TLabel'
WARNING = 'Warning.TLabel'
SUCCESS = 'Success.TLabel'

style = ttk.Style(root)
style.configure('Error.TLabel', foreground='red')
style.configure('Success.TLabel', foreground='green')
style.configure('Warning.TLabel', foreground='orange')


def validate_password(*args):
    password = password_var.get()
    confirm_password = password_confirmation_var.get()

    if not password or not confirm_password:
        set_message("", WARNING)
        return

    if confirm_password == password:
        set_message(
            "The passwords match!", SUCCESS)
        return

    if password.startswith(confirm_password):
        set_message('The passwords are partially matching!', WARNING)
        return

    set_message("The passwords don't match!", ERROR)


def set_message(message, message_type=None):
    output_label['text'] = message
    if message_type is not None:
        output_label['style'] = message_type


pack_attr = {'anchor': tk.W, 'padx': 5, 'pady': 5, 'fill': tk.X}

output_label = ttk.Label(root, text='')
output_label.pack(**pack_attr)


# password field
ttk.Label(root, text='New Password:').pack(**pack_attr)
password_var = tk.StringVar()
password = ttk.Entry(root, textvariable=password_var, show='*')
password.pack(**pack_attr)
password.focus()


# password confirmation field
ttk.Label(root, text='Password Confirmation:').pack(**pack_attr)
password_confirmation_var = tk.StringVar()
password_confirmation = ttk.Entry(
    root, textvariable=password_confirmation_var, show='*')
password_confirmation.pack(**pack_attr)

password_confirmation_var.trace_add('write', validate_password)


# button
button = ttk.Button(
    root,
    text='Change Password'

)
button.pack(anchor=tk.W, padx=5, pady=5)


root.mainloop()
