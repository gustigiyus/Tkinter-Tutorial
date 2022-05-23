from tkinter import*
# import tkinter as tk


root = Tk()

root.title("Radio Button")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def get_gender():
    print(gender.get())


# Variable
gender = StringVar()

pria = Radiobutton(root, text='Laki-Laki', font=('arial', 15, 'bold'),
                   value='laki-laki', variable=gender).place(x=100, y=50)
gender.set('laki-laki')

wanita = Radiobutton(root, text='Perempuan', font=('arial', 15, 'bold'),
                     value='perempuan', variable=gender).place(x=250, y=50)

entry = Entry(root, width='50', textvariable=gender,
              font=('arial', 15), bg='blue')
entry.place(x=0, y=10, relwidth=1)
 
btn = Button(root, text='Pilih Gender', font=(
    'arial', 15, 'bold'), command=get_gender).place(x=100, y=100)

root.mainloop()
