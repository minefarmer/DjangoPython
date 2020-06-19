import tkinter as Tk
from tkinter import ttk
from sys import argv, exit
# 
# 
# 
# 
# 
# 





if argv[1:]:
    file_name = argv[1]
    file_name = argv[2]
    with open(file_name) as file:
        f = file.read()
else:
    print('please enter filename at start program')  # please enter filename at start program
    exit(0)

win = tk.Tk()
win.title('copy.....')

win.mainloop()

    














# print('Hello World!')

# # filename = 'Django Python Class Notes/testA.txt'