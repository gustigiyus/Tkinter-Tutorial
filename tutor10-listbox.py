from tkinter import*
# import tkinter as tk

root = Tk()

root.title("Radio Button")
root.geometry("700x700+0+0")
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')
# root.resizable(False, False)


def get_data():
    cursor = listbox1.curselection()
    for item in cursor:
        print(listbox1.get(item))


course = ['Python', 'Java', 'C++', 'HTML', 'CSS']
listbox1 = Listbox(root, font=('arial', 15, 'bold'), selectmode=MULTIPLE)
listbox1.place(x=100, y=100)

for i in course:
    listbox1.insert(END, i)

btn = Button(root, text='Course Detail', cursor='hand2',
             bg='lightblue', command=get_data)
btn.place(x=100, y=380)

root.mainloop()
