from tkinter import*
# import tkinter as tk
from tkinter import messagebox

root = Tk()

root.title("Menu Tkinter")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def data_submenu():
    messagebox.showinfo('Info', 'Selamat anda berhasil!!!!')


MyMenu = Menu(root)
SubMenu = Menu(MyMenu, tearoff=0)

MyMenu.add_cascade(label='File', menu=SubMenu)
SubMenu.add_command(label='Save', command=data_submenu)
SubMenu.add_command(label='Download')
SubMenu.add_command(label='Exit')

root.config(menu=MyMenu)

root.mainloop()
