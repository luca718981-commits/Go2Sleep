import tkinter as tk
import webbrowser

root = tk.Tk()
root.title("Go to Sleep")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, text="Go to sleep", font=("Arial", 16))
label.pack(pady=20)

def yes_clicked():
    root.destroy()

def no_clicked():
    webbrowser.open("https://www.youtube.com/watch?v=9EiinQ1QNXU")

def swap(event):
    root.update_idletasks()
    bx = no_button.winfo_x()
    by = no_button.winfo_y()
    if abs(event.x - bx) < 50 and abs(event.y - by) < 50:
        yes_x, yes_y = yes_button.winfo_x(), yes_button.winfo_y()
        no_x, no_y = no_button.winfo_x(), no_button.winfo_y()
        yes_button.place(x=no_x, y=no_y)
        no_button.place(x=yes_x, y=yes_y)

yes_button = tk.Button(root, text="Yes", width=10, command=yes_clicked)
yes_button.place(x=60, y=120)

no_button = tk.Button(root, text="No", width=10, command=no_clicked)
no_button.place(x=160, y=120)

root.bind("<Motion>", swap)

root.mainloop()
