import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('scroll text')

label = ttk.Label(win, text='Enter a name: ')
label.grid(column=0, row=0)
label2 = ttk.Label(win, text='Choose a number: ').grid(column=1, row=0)
                                                       
name = tk.StringVar
textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)
number = tk.StringVar()
combobox = ttk.Combobox(win, width=12, textvariable=number)
combobox['values'] = (10, 20, 30, 40, 50, 60)
combobox.current(0)
combobox.grid(column=1, row=1)

colors = ['Blue', 'Gold', 'Red']

radvar = tk.IntVar()

for r in range(3):
    corerad = 'rad' + str(r)
    corerad = tk.Radiobutton(win, text=colors[r], variable=radvar, value=r, command=radcall)



win.mainloop()