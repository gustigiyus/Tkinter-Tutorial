from tkinter import*
# import tkinter as tk


root = Tk()

root.title("My First GUI")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def click():
    lbl = Label(root, text='Tutor ke 2 Button',
                font=('times new roman', 20, 'bold'))
    lbl.pack()


MyButton = Button(root, text='Click Disini', font=(
    'arial', 15, 'bold'), command=click, fg='gold', bg='black')
MyButton.pack(padx=50, pady=50)

root.mainloop()
