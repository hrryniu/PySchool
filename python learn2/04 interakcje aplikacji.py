import tkinter as tk
# root = tk.Tk()
# root.geometry("300x100")
#
# def click():
#     print("I'm Batman!")
#
# button = tk.Button(text="Click me!", command=click)
# button.pack(expand=True)
#
# root.mainloop()

def button_clicked(event):
    print("Button clicked!")

def key_pressed(event):
    print("Key pressed:", event.keysym)

def mouse_enter(event):
    print("Mouse entered the widget!")

def mouse_leave(event):
    print("Mouse left the widget!")

root= tk.Tk()
root.geometry("300x200")

button= tk.Button(text="Click Me!")
button.bind("<Button-1>", button_clicked)
button.pack(expand=True)

entry = tk.Entry()
entry.bind("<KeyPress>", key_pressed)
entry.bind("<Enter>", mouse_enter)
entry.bind("<Leave>", mouse_leave)
entry.pack(expand=True)

root.mainloop()
