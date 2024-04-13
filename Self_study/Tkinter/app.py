import tkinter as tk
from tkinter import *

def convert():
    mile_input = entry_Int.get()
    km_output = mile_input * 1.61
    output_string.set(f"KM: {km_output}")

#window creation
window = tk.Tk()
window.title('1st APP')
window.geometry('600x300') #'WidthxHeight'
window.configure(background="salmon")
window.resizable(width=True, height= False)

# text add
title_lable = tk.Label(
    master = window,
    font = "Arial 34 bold", 
    text= "Miles to KM converter", 
    background= "salmon", 
    foreground= "black")
title_lable.pack()

#input field
input_frame = tk.Frame(master= window)
entry_Int = tk.IntVar()
entry = tk.Entry(master= input_frame, textvariable=entry_Int)
button = tk.Button(master=input_frame, text="Convert", command= convert, activebackground= "green") 
##don't call the fuction here, just set it in the variable and it will be called automatically by the button
entry.pack(side='left', padx=1)
button.pack(side='right')
input_frame.pack(pady=50)

#output
output_string = tk.StringVar()
output_label = tk.Label(
    master= window, 
    text= "This is the output", 
    font="Calibri 30 italic bold", 
    textvariable= output_string, 
    background="salmon", 
    foreground="black")
output_label.pack()

#run
window.mainloop()