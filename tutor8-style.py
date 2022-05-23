from tkinter import*
# import tkinter as tk


root = Tk()

root.title("Radio Button")
root.geometry("600x600+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)

title = Label(root, text="Latihan Style Dekstop", font=(
    'arial', 18, 'bold'), bg='white', fg='red', bd=4, relief=RIDGE).place(x=0, y=0, relwidth=1)

name = Entry(root, font=(
    'arial', 18, 'bold'), borderwidth=3, relief=SUNKEN)
name.place(x=0, y=50, relwidth=1)

btn = Button(root, text='Course Detail', cursor='hand2')
btn.place(x=0, y=100, relwidth=0.12)

root.mainloop()
