import tkinter as tk 
from tkinter import ttk

# 
# 
# 
# 
# 

# win = tk.Tk()
# win.title('Python tkinter ')

# aLabel = ttk.Label(win, text='File name: ')
# aLabel.grid(column=0, row=0)

# def clickMe():
#     file_name = name.get()
#     with open(file_name) as file:
#         f = file.read()
        
#     action.configure(text=f)
#     aLabel.configure(foreground='green')

# action = ttk.Button(win, text='click me', command=clickMe)
# action.grid(column=1, row=1)

# name = tk.StringVar()

# textbox = ttk.Entry(win, width=12, textvariable=name)
# textbox.grid(column=0, row=1)

# win.mainloop()

##########################################
win = tk.Tk()
win.title('copy .... past')

aLabel = ttk.Label(win, text= 'enter file name!!!')
aLabel.grid(column=0, row=0)

def clickMe():
    file_name1 = name.get()
    with open(file_name1) as file:
        f1 = file.read()
        


    action.configure()







action = ttk.Button(win, text='click to copy', command=clickMe)
action.grid(column=1, row=1)
name = tk.StringVar()
name1 = tk.StringVar()
Textbox = ttk.Entry(win, width=12, textvariable=name)
Textbox.grid(column=0, row=1)
Textbox2 = ttk.Entry(win, width=12, textvariable=name1).grid(column=0, row=2)



win.mainloop()