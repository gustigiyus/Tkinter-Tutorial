from tkinter import*
# import tkinter as tk

from tkinter import ttk


root = Tk()

root.title("Radio Button")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def get_data():
    print(mycombo.get())


mycombo = ttk.Combobox(root, font='arial', width=25,
                       state='readonly', justify='center')
mycombo['value'] = ('Select Option', 'Python', 'Java', 'C++', 'HTML', 'CSS')
mycombo.set('Select Option')
mycombo.place(x=100, y=100)

btn = Button(root, text='Course Detail', cursor='hand2',
             bg='lightblue', command=get_data)
btn.place(x=100, y=150)

root.mainloop()
