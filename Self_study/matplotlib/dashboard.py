# from data import *
# from tkinter import *
# import tkinter as tk
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# # Creating the window
# window = Tk()
# window.title('Dashboard')
# window.geometry('960x540')
# window.state('zoomed')
# window.configure(bg="aqua")


# # frames

# #side bar
# side_bar = Frame(window, bg='#EE7AE9')
# side_bar.pack(side='left', fill='y')

# main_frame = Frame(window)
# main_frame.pack()

# ## upper frame inside the main frame
# upper_frame = Frame(main_frame)
# upper_frame.pack(side= 'top', fill='both', expand=True)

# lower_frame = Frame(main_frame)
# lower_frame.pack(side='bottom', fill='both', expand=True)


# # labels
# # side bar label
# side_bar_lable = Label(side_bar, text="Dashboard", font='times 24 bold', bg ='#EE7AE9')
# side_bar_lable.pack()



# ## Making the colour scheme
# plt.rcParams["axes.prop_cycle"] = plt.cycler(
#     color = ["#DA70D6", "#FF83FA", "#EE7AE9", "#CD69C9", "#8B4789"]
# )


# #### Craating the graphs and charts with Matplotlib

# # Chart-1: Bar chart for sales data-
# fig1, ax1 = plt.subplots()
# ax1.bar(sales_data.keys(), sales_data.values())
# ax1.set_title('Sales Data')
# ax1.set_xlabel('Product')
# ax1.set_ylabel('Sales')
# # plt.show()


# # Chart-2: Horizontal bar chart of inventory data
# fig2, ax2 = plt.subplots()
# ax2.barh(list(inventory_data.keys()), inventory_data.values())
# ax2.set_title("Inventory Data")
# ax2.set_xlabel("Inventory")
# ax2.set_ylabel("Product")
# # plt.show()


# # Chart 3: Pie chart of product data
# fig3, ax3 = plt.subplots()
# ax3.pie(product_data.values(), labels = product_data.keys(), autopct = '%1.1f%%')
# ax3.set_title("Product Data")


# # Chart 4: Line chart of sales by year
# fig4, ax4 = plt.subplots()
# ax4.plot(sales_year_data.keys(), sales_year_data.values())
# ax4.set_title("Sales By Year")
# ax4.set_xlabel("Years")
# ax4.set_ylabel("Sales")


# # Chart 5: Area chart of inventory by month
# fig5, ax5 = plt.subplots()
# ax5.fill_between(inventory_month_data.keys(), inventory_month_data.values())
# ax5.set_title("Inventory Data")
# ax5.set_xlabel("Months")
# ax5.set_ylabel("Products in Inventory")



# ### Importing the graphs and charts in the main interface

# canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
# canvas1.draw()
# canvas1.get_tk_widget().pack(side='left', fill="both", expand=True)

# canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
# canvas2.draw()
# canvas2.get_tk_widget().pack(side='left', fill="both", expand= True)

# canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
# canvas3.draw()
# canvas3.get_tk_widget().pack(side='right', fill="both", expand=True)

# canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
# canvas4.draw()
# canvas4.get_tk_widget().pack(side='left', fill='both', expand=True)

# canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
# canvas5.draw()
# canvas5.get_tk_widget().pack(side='right', fill="both", expand=True)


# window.mainloop()












from data import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 'data.py' contains the required dictionaries for the charts:
# sales_data, inventory_data, product_data, sales_year_data, inventory_month_data

class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Dashboard')
        self.root.geometry('960x540')
        self.root.state('zoomed')
        self.root.configure(bg="aqua")

        self.create_color_scheme()
        self.create_frames()
        self.create_labels()
        self.create_charts()

    def create_color_scheme(self):
        # Creating color scheme for charts
        plt.rcParams["axes.prop_cycle"] = plt.cycler(
            color=["#DA70D6", "#FF83FA", "#EE7AE9", "#CD69C9", "#8B4789"]
        )

    def create_frames(self):
        # Creating frames
        self.side_bar = tk.Frame(self.root, bg='#EE7AE9')
        self.side_bar.pack(side='left', fill='y')

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')

        self.upper_frame = tk.Frame(self.main_frame)
        self.upper_frame.pack(side='top', fill='both', expand=True)

        self.lower_frame = tk.Frame(self.main_frame)
        self.lower_frame.pack(side='bottom', fill='both', expand=True)

    def create_labels(self):
        # Creating labels
        self.side_bar_label = tk.Label(self.side_bar, text="Dashboard", font='times 24 bold', bg='#EE7AE9')
        self.side_bar_label.pack()

    def create_charts(self):
        # Chart-1: Bar chart for sales data
        fig1, ax1 = plt.subplots()
        ax1.bar(sales_data.keys(), sales_data.values())
        ax1.set_title('Sales Data')
        ax1.set_xlabel('Product')
        ax1.set_ylabel('Sales')
        self.canvas1 = FigureCanvasTkAgg(fig1, self.upper_frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side='left', fill="both", expand=True)

        # Chart-2: Horizontal bar chart for inventory data
        fig2, ax2 = plt.subplots()
        ax2.barh(list(inventory_data.keys()), inventory_data.values())
        ax2.set_title("Inventory Data")
        ax2.set_xlabel("Inventory")
        ax2.set_ylabel("Product")
        self.canvas2 = FigureCanvasTkAgg(fig2, self.upper_frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side='left', fill="both", expand=True)

        # Chart-3: Pie chart for product data
        fig3, ax3 = plt.subplots()
        ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
        ax3.set_title("Product Data")
        self.canvas3 = FigureCanvasTkAgg(fig3, self.upper_frame)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack(side='right', fill="both", expand=True)

        # Chart-4: Line chart for sales by year
        fig4, ax4 = plt.subplots()
        ax4.plot(list(sales_year_data.keys()), list(sales_year_data.values()))
        ax4.set_title("Sales By Year")
        ax4.set_xlabel("Years")
        ax4.set_ylabel("Sales")
        self.canvas4 = FigureCanvasTkAgg(fig4, self.lower_frame)
        self.canvas4.draw()
        self.canvas4.get_tk_widget().pack(side='left', fill='both', expand=True)

        # Chart-5: Area chart for inventory by month
        fig5, ax5 = plt.subplots()
        ax5.fill_between(list(inventory_month_data.keys()), list(inventory_month_data.values()))
        ax5.set_title("Inventory By Month")
        ax5.set_xlabel("Months")
        ax5.set_ylabel("Inventory")
        self.canvas5 = FigureCanvasTkAgg(fig5, self.lower_frame)
        self.canvas5.draw()
        self.canvas5.get_tk_widget().pack(side='right', fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()







