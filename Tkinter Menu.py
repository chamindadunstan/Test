import tkinter as tk
from tkinter import ttk
from tkinter import Menu


class MenuDemoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Menu Demo (OOP)")
        self.geometry("320x250")

        # Configure grid: 4 rows
        self.rowconfigure(0, weight=1)  # Frame 1
        self.rowconfigure(1, weight=1)  # Frame 2
        self.rowconfigure(2, weight=1)  # Frame 3
        self.rowconfigure(3, weight=1)  # Frame 4

        self.columnconfigure(0, weight=1)
        # Build UI
        self.create_frames()
        self.create_menubar()
        self.create_menubutton()

    # ---------------------------------------------------
    # Create Frames
    # ---------------------------------------------------
    def create_frames(self):
        # Frame 1
        self.frame_1 = tk.Frame(self, bg="lightblue", bd=2, relief="groove")
        self.frame_1.grid(row=0, column=0, sticky="nsew")
        ttk.Label(self.frame_1, text="Frame 1_create a menubar",
                  foreground="red").pack(pady=10)

        # Frame 2
        self.frame_2 = tk.Frame(self, bg="lightgreen", bd=2, relief="groove")
        self.frame_2.grid(row=1, column=0, sticky="nsew")
        ttk.Label(self.frame_2, text="Frame 2_ Menubutton",
                  foreground="red").grid(row=0, column=0, pady=10, sticky="w")

        # Frame 3
        self.frame_3 = tk.Frame(self, bg="lightgray", bd=2, relief="groove")
        self.frame_3.grid(row=2, column=0, sticky="nsew")
        ttk.Label(self.frame_3, text="Frame 3_OptionMenu", foreground="red"
                  ).grid(row=0, column=0, pady=10)

        # Frame 4
        self.frame_4 = tk.Frame(self, bg="lightyellow", bd=2, relief="groove")
        self.frame_4.grid(row=3, column=0, sticky="nsew")
        ttk.Label(self.frame_4, text="Frame 4_", foreground="red"
                  ).pack(pady=10)

# ---------------------------------------------------
    # Create Menubar
    # ---------------------------------------------------
    def create_menubar(self):
        menubar = Menu(self)
        self.config(menu=menubar)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='New')
        file_menu.add_command(label='Open...')
        file_menu.add_command(label='Close')
        file_menu.add_separator()

        # Submenu
        sub_menu = Menu(file_menu, tearoff=0)
        sub_menu.add_command(label='Keyboard Shortcuts')
        sub_menu.add_command(label='Color Themes')
        file_menu.add_cascade(label="Preferences", menu=sub_menu)

        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.destroy)

        menubar.add_cascade(label="File", menu=file_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label='Welcome')
        help_menu.add_command(label='About...')
        menubar.add_cascade(label="Help", menu=help_menu)

    # ---------------------------------------------------
    # Create Menubutton in Frame 2
    # ---------------------------------------------------
    def create_menubutton(self):
        self.selected_color = tk.StringVar()
        self.selected_color.trace_add('write', self.on_color_selected)

        colors = ('Red', 'Green', 'Blue')

        menu_button = ttk.Menubutton(self.frame_2, text='Select a color')
        menu_button.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        menu = Menu(menu_button, tearoff=0)
        for color in colors:
            menu.add_radiobutton(
                label=color,
                value=color,
                variable=self.selected_color
            )

        menu_button["menu"] = menu

        # Label to show selected color
        self.color_label = ttk.Label(self.frame_2, text="No color selected")
        self.color_label.grid(row=2, column=0, pady=5, sticky="w")

    def on_color_selected(self, *args):
        selected_color = self.selected_color.get()

        # Update label text
        self.color_label.config(text=f"Selected color: {selected_color}")

        # Change Frame 2 background
        self.frame_2.config(bg=selected_color.lower())

    # OptionMenu ---------------------------------------
    # OptionMenu is a specialized widget designed specifically
    # for selecting one value from a list.
    # initialize data
        self.languages = ('Python', 'JavaScript', 'Java',
                          'Swift', 'GoLang', 'C#', 'C++', 'Scala')

        # set up variable
        self.option_var = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # Make Frame 3 expandable
        self.frame_3.rowconfigure(0, weight=1)
        self.frame_3.rowconfigure(1, weight=1)
        self.frame_3.rowconfigure(2, weight=1)
        self.frame_3.rowconfigure(3, weight=1)
        self.frame_3.columnconfigure(0, weight=1)

        # Label inside Frame 3 (Row 1)
        label = ttk.Label(
            self.frame_3,  text='Select your most favorite language:')
        label.grid(column=0, row=1, sticky=tk.W, **paddings)

        # OptionMenu inside Frame 3 (Row 2)
        option_menu = ttk.OptionMenu(
            self.frame_3,
            self.option_var,
            self.languages[0],
            *self.languages,
            command=self.option_changed)

        option_menu.grid(column=0, row=2, sticky=tk.W, **paddings)

        # Output label inside Frame 3 (Row 3)
        self.output_label = ttk.Label(self.frame_3, foreground='red')
        self.output_label.grid(column=0, row=3, sticky=tk.W, **paddings)

        self.frame_3.update_idletasks()

    def option_changed(self, *args):
        self.output_label['text'] = f'You selected: {self.option_var.get()}'


if __name__ == "__main__":
    app = MenuDemoApp()
    app.mainloop()
