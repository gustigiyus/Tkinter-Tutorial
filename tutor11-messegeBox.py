from tkinter import*
# import tkinter as tk
from tkinter import messagebox

root = Tk()

root.title("Radio Button")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def messege1():
    messagebox.showerror('Show Error', 'Data yang anda inputkan salah')


def messege2():
    messagebox.showinfo('Show Info', 'Data anda berhasil di input')


def messege3():
    messagebox.showwarning('Show Warning', 'Ini peringatan untuk anda')


btn = Button(root, text='Button Detail 1', cursor='hand2',
             bg='lightblue', command=messege1)
btn.place(x=100, y=100)

btn = Button(root, text='Button Detail 2', cursor='hand2',
             bg='lightblue', command=messege2)
btn.place(x=200, y=100)

btn = Button(root, text='Button Detail 3', cursor='hand2',
             bg='lightblue', command=messege3)
btn.place(x=300, y=100)

root.mainloop()
