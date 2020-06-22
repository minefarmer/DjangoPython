import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext

# not used much  8 
# normally used 24
# 
# win = tk.Tk()
# win.title('python gui')

# labelframe = ttk.LabelFrame(win, text='Labels')
# labelframe.grid(column=0, row=0, padx=20, pady=40)
# ttk.Label(labelframe, text='Label1------------- soooooo loooooooooongeeeeeeeee').grid(column=0, row=0)
# ttk.Label(labelframe, text='Label2').grid(column=0, row=1)
# ttk.Label(labelframe, text='Label3').grid(column=0, row=2)
# ttk.Label(labelframe, text='Label4').grid(column=0, row=3)

# for c in labelframe.winfo_children():
#     c.grid_configure(padx=8, pady=4)

# win.mainloop()


win = tk.Tk()
win.title('python gui')

monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)

label1 = ttk.Label(monty, text='Enter a name! ')
label1.grid(column=0, row=0)

name = tk.StringVar()
textb = ttk.Entry(monty, width=12, textvariable=name)
textb.grid(column=0, row=1)
textb.focus()
label2 = ttk.Label(monty, text='Choose anumber: ')
label2.grid(column=1, row=0)

number = tk.StringVar()
cbox = ttk.Combobox(monty, width=12, textvariable=number)
cbox['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
cbox.current(0)
cbox.grid(column=1, row=1)

def clickMe():
    if chvar1.get() == 1:
        label1.configure(foreground='red')
    elif chvar1.get() == 0:
        label1.configure(foreground='black')
    if chvar2.get() == 1:
        label2.configure(foreground='gold')
    elif chvar2.get() == 0:
        label2.configure(foreground='black')


action = ttk.Button(monty, text='click me', command=clickMe)
action.grid(column=2, row=1)

chvar1 = tk.IntVar()
checkB1 = tk.Checkbutton(monty, text='Disable', variable=chvar1, command=clickMe)
checkB1.grid(column=0, row=2)
chvar2 = tk.IntVar()
checkB2 = tk.Checkbutton(monty, text='Unchecked', variable=chvar2, command=clickMe)
checkB2.grid(column=1, row=2)
chvar3 = tk.IntVar()
checkB3 = tk.Checkbutton(monty, text='togg', variable=chvar3, command=clickMe)
checkB3.grid(column=2, row=2)
scr = scrolledtext.ScrolledText(monty, width=30, height=3, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)
# scr.grid(column=0, columnspan=3)



win.mainloop()