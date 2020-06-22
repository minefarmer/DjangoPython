import tkinter as tk 
from tkinter import ttk

win = tk.Tk()
win.title('python frames')

label = ttk.Label(win, text='Enter a name')
label.grid(column=0, row=0)
name= tk.StringVar()
textbox = ttk.Entry(win, width=12, textvariable=name)
textbox.grid(column=0, row=1)
textbox.focus

labelsFrames = ttk.LabelFrame(win, text='Labels in a frame')
labelsFrames.grid(column=0, row=7, padx=20, pady=40)

# place labels into the container

ttk.Label(labelsFrames, text='Label1').grid(column=0, row=1)
ttk.Label(labelsFrames, text='Label2').grid(column=0, row=2)
ttk.Label(labelsFrames, text='Label3').grid(column=0, row=3)



win.mainloop()