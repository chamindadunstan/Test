import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

# create the main window
root = tk.Tk()
root.geometry('400x180')
root.title('Listbox')

# create a variabe object
languages = (
    'Java', 'C', 'C++', 'C#', 'Python',
    'Go', 'JavaScript', 'PHP', 'Swift'
)

list_variable = tk.Variable(value=languages)


# label
label = ttk.Label(
    root,
    text='Select your favorite programming languages:'
)
label.pack(padx=10, pady=0, side=tk.TOP, fill=tk.X)

listbox = tk.Listbox(
    root,
    listvariable=list_variable,
    height=6,
    selectmode=tk.MULTIPLE,
)

listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)


def handle_item_select(event):
    selected_indices = listbox.curselection()
    selected_languages = ",".join([listbox.get(i) for i in selected_indices])

    showinfo(
        title='Information',
        message=f'You selected: {selected_languages}'
    )


listbox.bind('<<ListboxSelect>>', handle_item_select)

root.mainloop()
