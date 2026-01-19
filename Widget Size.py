import tkinter as tk

root = tk.Tk()
root.title('Tkinter Widget Size')
root.geometry("600x400")

label1 = tk.Label(master=root, text="Sizing", bg='red', fg='white', width=20)
label1.pack(
    # Remove the fill and run the program to see the effect
    fill=tk.X
)

root.mainloop()
