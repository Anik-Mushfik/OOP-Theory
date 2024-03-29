import tkinter as tk
from tkinter import ttk

#window creation
window = tk.Tk()
window.title('1st APP')
window.geometry('600x300') #'WidthxHeight'
window.configure(background="red")

# text add
title_lable = ttk.Label(master = window,text= "This is a converter", font = "Arial 34 bold", background= "black", foreground= "yellow")
title_lable.pack()

#input field
input_frame = ttk.Frame(master= window)
entry = ttk.Entry(master= input_frame)
button = ttk.Button(master=input_frame, text="Click to DIE")
entry.pack(side='left', padx=30)
button.pack(side='left')
input_frame.pack(pady=30)
#run
window.mainloop()