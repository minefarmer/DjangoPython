import tkinter as tk 
from tkinter import ttk
from tkinter import Menu
from sys import exit
win = tk.Tk()
win.title('python GUI TAB')

tabs = ttk.Notebook(win)

tab1 = ttk.Frame(tabs)

tabs.add(tab1, text='Tab 1')

monty = ttk.LabelFrame(tab1, text=' Monty Python ' )
monty.grid(column=0, row=0, sticky='WE')
label1 = ttk.Label(monty, text='Enter a Name: ')
label1.grid(column=0, row=0)
name = tk.StringVar()
textb = ttk.Entry(monty, width=12, textvariable=name)
textb.grid()
tab2 = ttk.Frame(tabs)
tabs.add(tab2, text='Tab 2')
monty2 = ttk.LabelFrame(tab2, text=' Monty Python2')
monty2.grid(column=0, row=0, sticky='WE')
label2 = ttk.Label(monty2, text='Choose a number: ')
label2.grid(column=0, row=0)
number = tk.StringVar()
cbox = ttk.Combobox(monty, width=12, textvariable=number)
cbox.grid(column=0, row=1)
cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cbox.current(0)

def exit():
    exit(0)

#  file menu
menubar = Menu(win)
win.config(menu=menubar)
filemenu = Menu(menubar)
filemenu.add_command(label='New File')
filemenu.add_command(label='New Window')
menubar.add_cascade(label ='File', menu=filemenu)

#  help menu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About')
helpmenu.add_command(label='Exit', command=exit)
helpmenu.add_command(label='Welcome')
menubar.add_cascade(label='Help', menu=helpmenu)



tabs.pack()



win.mainloop()
