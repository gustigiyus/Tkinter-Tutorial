from tkinter import*
# import tkinter as tk
from tkinter import messagebox
from tkinter import font

root = Tk()

root.title("Menu Tkinter")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)

myFrame = Frame(root, bd=4, relief=RIDGE)
myFrame.place(x=200, y=50, width=200, height=250)

scroll_x = Scrollbar(myFrame, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y = Scrollbar(myFrame, orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)


myList = Listbox(myFrame, font=('arial', 14, 'bold'),
                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
myList.pack()

scroll_y.config(command=myList.yview)
scroll_x.config(command=myList.xview)

for i in range(0, 21):
    myList.insert(END, f'Python Version Data Set:{i}')

root.mainloop()
