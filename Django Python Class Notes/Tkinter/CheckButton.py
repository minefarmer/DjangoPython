import tkinter as tk 
from tkinter import ttk

# 
# 
# 
# 
# 

# win = tk.Tk()

# win.title('python check button')


# chvar = tk.IntVar()

# check1 = tk.Checkbutton(win, text='Enable', variable=chvar, state='disabled')
# check1.select()
# check1.grid(column=0, row=0)
# chvar2 = tk.IntVar()
# check2 = tk.Checkbutton(win, text='Disable', variable=chvar2)
# check2.deselect()
# check2.grid(column=1, row=0)

# win.mainloop()








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


win.mainloop()