import tkinter as tk
from tkinter import ttk
# 
# 
# 
# 
# 
# 
# 

# class Test():
#     print('hello from class')  # hello from class  
# classistance = Test()

############################################
#  Classes
win = tk.Tk()  # this creates the main window for my work

win.title('python GUI')  # anytime I write dot anything it means this is a ticket into a finction

win.resizable(0, 0)  # not resizable  # comment out or remove if I need it resizeable
# ttk.Label(win, text='A Label!!').grid(column=0, row=0)  # opens win  with "A Label!!" inside of it # example only see next line for bettet way
aLabel = ttk.Label(win, text='A Label!!')
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='** i have been clicked!!!')
    aLabel.configure(foreground='red')





action = ttk.Button(win, text='click me', command=clickMe)
action.grid(column=1, row=0)






win.mainloop()


