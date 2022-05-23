from tkinter import*
# import tkinter as tk


root = Tk()

root.title("Radio Button")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def check_get_value():
    print(chk_var.get())


# Variable
chk_var = IntVar()

chk_button = Checkbutton(
    root, text='Terima dan lanjutkan peryaratan', variable=chk_var, onvalue=1, offvalue=0, font=('arial', 20, 'bold')).place(x=50, y=50)
chk_var.set('0')

btn = Button(root, text='Pilih Gender', font=(
    'arial', 15, 'bold'), command=check_get_value).place(x=150, y=100)

root.mainloop()
