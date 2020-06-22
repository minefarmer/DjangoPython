import tkinter as tk 
from tkinter import ttk

# radio button  58
# 
# 
# 
# 





win = tk.Tk()

win.title('python check button')

# first label
label = ttk.Label(win, text='Enter a name')
label.grid(column=0, row=0)

# text Box
name = tk.StringVar()
textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)

# check button
chvar = tk.IntVar()
chb1 = tk.Checkbutton(win, text='Disable', variable=chvar, state='disabled')
chb1.grid(column=0, row=2)
chb1.grid(column=0, row=2, sticky=tk.W)

# second label

label2 = ttk.Label(win, text='Choose a number')
label2.grid(column=1, row=0)

number = tk.StringVar()
numberChoose = ttk.Combobox(win, width=12, textvariable=number)
numberChoose['values'] = (1, 2, 3, 4, 5, 6, 47, 8, 9, 10)
numberChoose.grid(column=1, row=1)
numberChoose.current(0)

chvar2 = tk.IntVar()
chb2 = tk.Checkbutton(win, text='Unchecked', variable=chvar2)
chb2.grid(column=1, row=2, sticky=tk.W)



def clickMe():
    
    action.configure(text='** i have been clicked ' + name.get() + ' ' + number.get())
    label2.configure(foreground='gold')
    label.configure(background='green')
action = ttk.Checkbutton(win, text='click me', command=clickMe)
action.grid(column=2, row=1)


color1 = 'Blue'
color2 = 'Gold'
color3 = 'Red'



def radcall():
    radsel = radvar.get()
    if radsel == 1: win.configure(background=color1)
    elif radsel == 2: win.configure(background=color2)
    elif radsel == 3: win.configure(background=color3)
    
    
    
radvar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=color1, variable=radvar, value=1, command=radcall)
rad1.grid(column=0, row=5, sticky=tk.W)
rad2 = tk.Radiobutton(win, text=color2, variable=radvar, value=2, command=radcall)
rad2.grid(column=1, row=5, sticky=tk.W)
rad3 = tk.Radiobutton(win, text=color3, variable=radvar, value=3, command=radcall)
rad3.grid(column=2, row=5)


win.mainloop()