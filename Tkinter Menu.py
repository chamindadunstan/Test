from tkinter import tk, Menu
from tkinter import ttk

# root window
root = tk()
root.geometry('320x150')
root.title('Menu Demo')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)
# --------------------------------
# Menubutton variable
selected_color = tk.StringVar()
selected_color.trace_add(
    'write',
    lambda *args: root.config(bg=selected_color.get())
)

# Create the menu button
colors = ('Red', 'Green', 'Blue')

# Create the Menubutton
menu_button = ttk.Menubutton(root, text='Select a color')

# Create a new menu instance
menu = tk.Menu(menu_button, tearoff=0)

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=selected_color
    )


menu_button["menu"] = menu
menu_button.pack(expand=True)

# run the application
root.mainloop()
