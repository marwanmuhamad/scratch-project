import tkinter as tk 

root = tk.Tk()  

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# x = int(0.5*(root.winfo_screenwidth() - width))
# y = int(0.5*(root.winfo_screenheight() - height))
root.geometry("{}x{}".format(width, height))
root.title("Split Windows App")

# Define functions:
def show_user():
    hide_all_frames()
    user_frm.pack(side = "right", fill = "both", expand = 1, anchor = "se")

def show_stock():
    hide_all_frames()
    stock_frm.pack(side = "right", fill = "both", expand = 1, anchor = "se")


# Remove all frames:
def hide_all_frames():
    frame2.pack_forget()
    user_frm.pack_forget()
    stock_frm.pack_forget()

frame1 = tk.Frame(root, bg = "#12abff", width= int(0.1*width), height=height)
frame1.pack(side = "left", fill = "both", expand = 1, anchor = "nw")

frame2 = tk.Frame(root, bg = "#1276ac", width=int(0.9*width), height=height)
frame2.pack(side = "right", fill = "both", expand = 1, anchor = "se")


user_frm = tk.Frame(root, bg = "#56ca9a", width=int(0.9*width), height=height)
stock_frm = tk.Frame(root, bg = "#56cada", width=int(0.9*width), height=height)

user_btn = tk.Button(frame1, text = "Manage User", width = 25, height = 2, bg = "#fa89ab", fg = "#fafafa",
                 relief = "flat", bd = 0, font = ("Roboto", 11), command = show_user)
user_btn.grid(row = 0, column = 0, pady = 5, padx = 10, columnspan=2, sticky = "w")

stock_btn = tk.Button(frame1, text = "Manage Stock", width = 25, height = 2, bg = "#fa89ab", fg = "#fafafa",
                 relief = "flat", bd = 0, font = ("Roboto", 11), command = show_stock)
stock_btn.grid(row = 1, column = 0, pady = 5, padx = 10, columnspan=2, sticky = "w")








root.mainloop()