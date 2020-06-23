import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext

win = tk.Tk()
win.title('python GUI')

def msgbox():
    mBox.showinfo('python is the best', 'thjs is msgbox')
def msgbox2():
    mBox.showwarning('', 'this is a warning')
def msgbox3():
    mBox.showerror('python error', 'a python GUI using tkinter \n Error ')
def msgbox4():
    answer = mBox.askyesno('python message dual choice Box', 'Are You Sure? ')
    print(answer)
menubar = Menu(win)
win.configure(menu=menubar)
filemenu = Menu(menubar, tearoff=0)
helpmenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='New')
helpmenu.add_command(label='About', command=msgbox)
helpmenu.add_command(label='warning', command=msgbox2)
helpmenu.add_command(label='Error', command=msgbox3)
helpmenu.add_command(label='Yesno', command=msgbox4)
menubar.add_cascade(label='File', menu=filemenu)
menubar.add_cascade(label='Help', menu=helpmenu)
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')
# spin = tk.Spinbox(win, from_ = 0, to=10, width=10, bd=8, command=_spin)
spin = tk.Spinbox(win, values=(1, 2, 3, 4, 5, 6, 42, 50, 100, 90), width=10, bd=8, command=_spin)
spin.grid(column=0, row=0)
scr = scrolledtext.ScrolledText(win, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, row=1, sticky='WE', columnspan=3)




win.mainloop()