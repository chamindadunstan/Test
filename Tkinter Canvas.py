import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Text')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


canvas.create_text(
    (300, 100),
    text="Canvas Demo",
    fill="orange",
    font='tkDefaeultFont 24'
)

root.mainloop()
