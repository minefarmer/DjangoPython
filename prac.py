import tkinter as tk
from tkinter import ttk
from sys import argv, exit
# 
# 
# 
# 
# 
# 
# 

# class Test():
#     print('hello world!')  # hello world!
    
# classinstance = Test()









if argv[1:]:
    file_name = argv[1]
    file_name2 = argv[2]
    with open(file_name) as file:
        f = file.read()
else:
    print('please enter filename at start of program')
    exit(0)
    
win = tk.Tk()
win.title('copy.....')

win.mainloop()
    


