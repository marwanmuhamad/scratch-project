import tkinter as tk 

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

root.title("Desktop Application")
root.geometry("%sx%s" %(width, height))

# Add functions 
def new_file():
    pass  


my_menu = tk.Menu(root)
my_menu.configure(relief = "flat", background = "#313131", border = 1, borderwidth = 0,  
                    activeborderwidth= 0, type = "normal")
root.config(menu = my_menu, background = "#313131")


file_menu = tk.Menu(my_menu, relief = "flat", tearoff= 0, background = "#313131", bd = 0, borderwidth = 0, 
                    activeborderwidth= 0, foreground = "#ffffff", type = "normal")
my_menu.add_cascade(label = "File", menu = file_menu, hidemargin= True, state = "normal", columnbreak = 0)
file_menu.add_command(label = "New File", command = new_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)





root.mainloop()