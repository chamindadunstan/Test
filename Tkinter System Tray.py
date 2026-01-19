import tkinter as tk
import pystray
import threading
from PIL import Image


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("System Tray App")
        self.geometry('500x250')
        self.protocol('WM_DELETE_WINDOW', self.minimize_to_tray)

    def minimize_to_tray(self):
        self.withdraw()
        image = Image.open("./assets/app.ico")

        menu = pystray.Menu(
            pystray.MenuItem('Show', self.show_window),
            pystray.MenuItem('Quit', self.quit_window)
        )

        self.icon = pystray.Icon("MyApp", image, "My App", menu)
        threading.Thread(target=self.icon.run, daemon=True).start()
        print("Tray icon running…")

    def quit_window(self, icon, item):
        icon.stop()
        self.destroy()

    def show_window(self, icon, item):
        icon.stop()
        self.after(100, self.deiconify)


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
