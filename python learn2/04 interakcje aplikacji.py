import tkinter as tk
root = tk.Tk()
root.geometry("300x100")

def click():
    print("I'm Batman!")

button = tk.Button(text="Click me!", command=click)
button.pack(expand=True)

root.mainloop()