import tkinter as tk 
from tkinter import ttk 


root = tk.Tk()
width = 800 
height = 600
x = int(0.5*(root.winfo_screenwidth() - width))
y = int(0.5*(root.winfo_screenheight() - height))
root.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y)) 
root.title("Windows with tabs")
root.configure(background = "#313131")

frame1 = tk.Frame(root, width = width, bd = 0, relief = "flat", bg = "#313131")
frame1.pack(side="top", fill = "x")

lbl1 = tk.Label(frame1, text = "Welcome! this is a simple app", bg = "#313131", fg = "#fafafa")
lbl1.pack(side = "top", anchor="center")
lbl1.config(font = ("Roboto, 13"))

frame2 = tk.Frame(root, width = width, bd = 0, relief = "flat", bg = "#404040")
frame2.pack(side="top", fill = "both", expand = 1)

tablayout = ttk.Notebook(frame2, width = width)
# tablayout.pack()

#tab 1
tab1 = tk.Frame(tablayout)
tab1.pack(fill="both")
for row in range(5):
    for column in range(6):
        if row == 0:
            label4 = tk.Label(tab1, text = "Heading "+str(column), bg = "white", fg = "black", font = ("Roboto, 13"))
            label4.grid(row = row, column = column, sticky="nsew")
            tab1.grid_columnconfigure(column,  weight =1)
        else:
            text_box = tk.Entry(tab1)
            text_box.grid(row = row, column = column, sticky="nsew", padx=1, pady=1)
            tab1.grid_columnconfigure(column,  weight =1)
tablayout.add(tab1, text = "TAB 1")

#tab 2
tab2 = tk.Frame(tablayout)
tab2.pack(fill="both")
# label2 = tk.Label(tab2, text="Some data in tab 2")
# label2.pack()

for row in range(5):
    for column in range(6):
        if row == 0:
            label3 = tk.Label(tab2, text = "Heading "+str(column), bg = "white", fg = "black", font = ("Roboto, 13"))
            label3.grid(row = row, column = column, sticky="nsew")
            tab2.grid_columnconfigure(column,  weight =1)
        else:
            label3 = tk.Label(tab2, text = "Row : "+str(row) + ", Column : "+str(column), bg = "black", fg = "white")
            label3.grid(row = row, column = column, sticky="nsew", padx=1, pady=1)
            tab2.grid_columnconfigure(column,  weight =1)
            
tablayout.add(tab2, text = "TAB 2")

tablayout.pack(fill = "both")


root.mainloop()