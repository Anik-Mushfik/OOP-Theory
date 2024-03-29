import tkinter as tk
from tkinter import ttk

def die():
    print("You will die soon!")

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
button = ttk.Button(master=input_frame, text="Click to DIE", command= die) 
#don't call the fuction here, just set it in the variable and it will be called automatically by the button
entry.pack(side='left', padx=30)
button.pack(side='right')
input_frame.pack(pady=50)

#output
output_label = ttk.Label(master= window, text= "This is the output", font="Calibri 20 italic", background="green", foreground="blue")
output_label.pack()

#run
window.mainloop()