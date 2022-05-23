from tkinter import*
# import tkinter as tk


root = Tk()

root.title("My First GUI")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def click():
    lbl.config(text=str(entry.get()))


entry = Entry(root, width='50', font=('arial', 15), bg='blue')
entry.place(x=0, y=10, relwidth=1)

text_box = Text(root, font=('arial', 15))
text_box.place(x=0, y=80, relwidth=0.50, relheight=0.35)

MyButton = Button(root, text='Click Disini', font=(
    'arial', 15, 'bold'), command=click, fg='gold', bg='black')
MyButton.place(x=300, y=350)

lbl = Label(root, text="", font=('times new roman', 15, 'bold'))
lbl.place(x=300, y=450)

root.mainloop()
