from tkinter import*
#import tkinter as tk

root = Tk()  # Memasukan Fungsi TK() kedalam variable root

root.title("My First GUI")  # Judul root GUI
root.geometry("500x500+0+0")  # Ukuran GUI
root.wm_iconbitmap('Tkinter_Tutorial/mario.ico')  # Icon GUI
root.resizable(False, False)  # Untuk Disable Resize dari GUI

root.mainloop()  # Untuk menjalankan program GUI
