from tkinter import *

class MyApplication(Tk):
    def __init__(self):
        super().__init__()

        self.count = 0
        self.renderCountScreen()

    def renderCountScreen(self):
        
        self.lable_counter = Label(master= self, text=str(self.count), font= 'Calibri 100 bold', background= 'lavender')
        self.lable_counter.pack()

        self.increase_button = Button(master= self, text= "Increase", command=self.increase, height=2, width=10, background='black', foreground='yellow', font='Arial 11 bold')
        self.increase_button.pack(side='left', padx = 20, pady= 30)

        self.decrease_button = Button(master= self, text='Decrease', command=self.decrease, height=2, width=10, background='black', foreground='yellow', font='Arial 11 bold')
        self.decrease_button.pack(side='right', padx=20, pady= 30)

        self.reset_button = Button(master= self, text= "Reset", command= self.reset, height=1, width=5, background='red', foreground='black', font='Arial 12 bold')
        self.reset_button.pack(side='bottom', pady= 40)


    def increase(self):
        self.count += 1
        self.lable_counter.config(text=str(self.count))

    def decrease(self):
        if self.count <= 0:
            self.count = 0
        else:
            self.count -= 1
        self.lable_counter.config(text= str(self.count))

    def reset(self):
        self.count = 0
        self.lable_counter.config(text= str(self.count))



if __name__ == "__main__":
    container = MyApplication()
    container.geometry('350x400')
    container.title("Digital Tasbih")
    container.configure(background= 'lavender')

    container.mainloop()