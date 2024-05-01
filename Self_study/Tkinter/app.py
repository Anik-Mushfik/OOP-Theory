# import tkinter as tk
# from tkinter import *

# def convert():
#     mile_input = entry_Int.get()
#     km_output = mile_input * 1.61
#     output_string.set(f"KM: {km_output}")

# #window creation
# window = tk.Tk()
# window.title('1st APP')
# window.geometry('600x300') #'WidthxHeight'
# window.configure(background="salmon")
# window.resizable(width=True, height= False)

# # text add
# title_lable = tk.Label(
#     master = window,
#     font = "Arial 34 bold", 
#     text= "Miles to KM converter", 
#     background= "salmon", 
#     foreground= "black")
# title_lable.pack()

# #input field
# input_frame = tk.Frame(master= window)
# entry_Int = tk.IntVar()
# entry = tk.Entry(master= input_frame, textvariable=entry_Int)
# button = tk.Button(master=input_frame, text="Convert", command= convert, activebackground= "green") 
# ##don't call the fuction here, just set it in the variable and it will be called automatically by the button
# entry.pack(side='left', padx=1)
# button.pack(side='right')
# input_frame.pack(pady=50)

# #output
# output_string = tk.StringVar()
# output_label = tk.Label(
#     master= window, 
#     text= "This is the output", 
#     font="Calibri 30 italic bold", 
#     textvariable= output_string, 
#     background="salmon", 
#     foreground="black")
# output_label.pack()

# #run
# window.mainloop()







import tkinter as tk

class ConverterApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('1st APP')
        self.window.geometry('600x300') #'WidthxHeight'
        self.window.configure(background="salmon")
        self.window.resizable(width=True, height= False)

        self.title_label = tk.Label(
            master = self.window,
            font = "Arial 34 bold", 
            text= "Miles to KM converter", 
            background= "salmon", 
            foreground= "black")
        self.title_label.pack()

        self.input_frame = tk.Frame(master= self.window)
        self.entry_Int = tk.IntVar()
        self.entry = tk.Entry(master= self.input_frame, textvariable=self.entry_Int)
        self.button = tk.Button(master=self.input_frame, text="Convert", command=self.convert, activebackground= "green") 
        self.entry.pack(side='left', padx=1)
        self.button.pack(side='right')
        self.input_frame.pack(pady=50)

        self.output_string = tk.StringVar()
        self.output_label = tk.Label(
            master= self.window, 
            text= "This is the output", 
            font="Calibri 30 italic bold", 
            textvariable= self.output_string, 
            background="salmon", 
            foreground="black")
        self.output_label.pack()

    def convert(self):
        mile_input = self.entry_Int.get()
        km_output = mile_input * 1.61
        self.output_string.set(f"KM: {km_output}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ConverterApp()
    app.run()

