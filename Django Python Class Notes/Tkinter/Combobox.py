import tkinter as tk 
from tkinter import ttk

# 
# 
# 
# 
#

# win = tk.Tk()
# win.title('')

# alabel = ttk.Label(win, text='choose a number: ').grid(column=1, row=0)
# number = tk.StringVar()
# numberbox = ttk.Combobox(win, width=12, textvariable=number)
# numberbox['values'] = (1, 2, 3, 4, 60, 47, 13, 300)
# numberbox.current(0)

# numberbox.grid(column=1, row=1)

# win.mainloop()



###################################################################

win = tk.Tk()
win.title('combobox')

alabel = ttk.Label(win, text='Enter a name: ')
alabel.grid(column=0, row=0)
alabel2 = ttk.Label(win, text='Choose a number')
alabel2.grid(column=1, row=0)



def clickMe():
    action.configure(text='hello {} {}'.format(name.get(), number.get()))
    alabel.configure(foreground='yellow')

action = ttk.Button(win, text='click me', command=clickMe)
action.grid(column=2, row=1)

name = tk.StringVar()
Textbox = ttk.Entry(win, width=12, textvariable=name)
Textbox.grid(column=0, row=1)
number = tk.StringVar()
numberbox = ttk.Combobox(win, width=12, textvariable=number)
numberbox['values'] = (1, 2, 3, 4, 5, 6, 47)
numberbox.current(0)
numberbox.grid(column=1, row=1)


win.mainloop()