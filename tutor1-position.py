from tkinter import*
#import tkinter as tk


root = Tk()

root.title("My First GUI")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
#root.resizable(False, False)

# -------------------- LABEL PACK(side=) SYSTEM -------------------------

# lbl1 = Label(root, text="Label Pertama Saya",font=("times new roman", 30, 'bold'))
# lbl1.pack(side=TOP)

# -------------------- LABEL GRID(row=, column=) SYSTEM -------------------------

#lbl1 = Label(root, text="Label Pertama Saya",font=("times new roman", 15, 'bold'))
#lbl1.grid(row=0, column=0)

# -------------------- LABEL PLACE(x=, y=) SYSTEM -------------------------

#lbl1 = Label(root, text="Label Pertama Saya",font=("times new roman", 15, 'bold'))
#lbl1.place(x=100, y=100)

root.mainloop()
