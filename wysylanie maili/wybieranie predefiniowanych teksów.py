import tkinter as tk

#import keyboard
import pyperclip

def load_data_from_file(filename):  #funkcja, ktora z pliku csv robi słownik
    data ={}
    with open(filename, "r") as file:
        for line in file:
            key,value= line.strip().split(";",1)#to jest podział na klucz i wartość, dzielimy po średniku i takich podziałów ma być maksymalnie 1
            data[key] =value
    return data

def on_entry_update(event):
    if event.keysym == "Return":
        on_listbox_selection()
    elif event.keysym not in ('Up', 'Down'):
    #print(entry.get())
        update_listbox()

def on_listbox_selection(event):
    selection = listbox.curselection()
    # print(selection),listbox.get(selection[0])

    if selection:
       key = listbox.get(selection[0])
       text = data[key]
       print(text)
       pyperclip.copy(text)

def update_listbox():
    listbox.delete(0, tk.END)
    text = entry.get().lower()
    for key in data:
        if text in key.lower():
            listbox.insert(tk.END,key)

# def toogle_window(event=None):
#     if root.state() == "normal":
#         root.withdraw()
#     else:
#         root.deiconify()
#         root.attributes("-topmost", True)
#         root.after_idle(root.attributes, "-topmost", False)


data= load_data_from_file('dane.txt')  #odbieramy dane z zewnetrznego pliku
#tworzymy okno
root = tk.Tk()
root.title("ClipboardMaster") #nazwa okna
#poniżej wykorzystuję bibliotekę keyboard i okno będzie się odpalać po odpaleniu skrótu klawiszowego
# root.withdraw()

#pole tekstowe
entry= tk.Entry(root)
entry.pack(fill=tk.BOTH, padx=10, pady=10)
entry.bind('<KeyRelease>', on_entry_update)#w momencie puszczenia klawisza odpala sie funkcja wyswietlająca klawisze w terminalu

#kolejne pole tekstowe
listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady= 10)
listbox.bind('<<ListboxSelect>>', on_listbox_selection)

#keyboard.add_hotkey("alt+q", toogle_window)

root.mainloop()
