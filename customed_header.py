import tkinter as tk 
from tkinter import PhotoImage
import tkcalendar as cal

root = tk.Tk()
width = 600
height = 400

x = int(0.5*(root.winfo_screenwidth() - width))
y = int(0.5*(root.winfo_screenheight() - height))

background_color = "#313131"
header_color = "#393939"
font_color = "#fafafa"
image = PhotoImage("question.png")
root.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
root.overrideredirect(True)
root.config(background = background_color)

#Define functions here 
def hover_btn(event):
    global title_btn
    title_btn["background"] = "#ff0000"

def unhover_btn(event):
    global title_btn
    title_btn["background"] = header_color

def minimize_window():
    root.overrideredirect(False)
    root.iconify()
    
def hover_minize(event):
    minimize_btn["background"] = "#676767"

def unhover_minize(event):
    minimize_btn["background"] = header_color

def show_screen(event):
    root.deiconify()
    root.overrideredirect(True)

def get_pos(event):
    xpos = root.winfo_x()
    ypos = root.winfo_y()
    epos_x = event.x_root
    epos_y = event.y_root
 
    xpos = xpos - epos_x
    ypos = ypos - epos_y

    def move(event):
        root.geometry("+{0}+{1}".format(event.x_root+xpos, event.y_root+ypos))
    
    title_frame.bind("<B1-Motion>", move)
    title_lbl.bind("<B1-Motion>", move)

def get_cal():
    # global cal_lbl
    my_date = cal.get_date()
    my_date = my_date.strftime("%d-%B-%Y")
    calVar.set(my_date)
    # cal_lbl.config(text = cal.get_date())

# def update_cal(*args):
#     # my_date = calVar.get()
#     # my_date = my_date.strftime("%d-%B-%Y")
#     cal_lbl.config(text = calVar.get())

title_frame = tk.Frame(root, background = header_color, width = width, border = 0, borderwidth = 0,
                      relief = "flat")
title_frame.pack(side = "top", fill = "x", anchor= "nw") #, expand = 1 --> do not use this
title_frame.bind("<Map>", show_screen)
title_frame.bind("<Button-1>", get_pos)

title_lbl = tk.Label(title_frame, text = "Simple Calendar App", font = ("Consolas, 11"), fg = font_color, bg = header_color)
title_lbl.pack(side = "left", padx = 5, anchor = "center")
title_lbl.bind("<Button-1>", get_pos)

title_btn = tk.Button(title_frame, text = "\u00D7", fg = font_color, bg = header_color, font = ("Consolas, 13"),
                      command = root.quit, bd = 0, relief = "flat", activebackground= "#ff0000")
title_btn.pack(side = "right", padx = 0, ipadx = 10, anchor = "ne")
title_btn.bind("<Enter>", hover_btn)
title_btn.bind("<Leave>", unhover_btn)
minimize_btn = tk.Button(title_frame, text = "-", fg = font_color, bg = header_color, font = ("Consolas, 13"),
                         relief = "flat", bd = 0, command = minimize_window)
minimize_btn.pack(side = "right", ipadx = 5, anchor = "e")
minimize_btn.bind("<Enter>", hover_minize)
minimize_btn.bind("<Leave>", unhover_minize)
# minimize_btn.bind("<Map>", show_screen)

# ---------------------------------------------------------------------------------------------------------------
body_frame = tk.Frame(root, bg = background_color, width = width, relief = "flat")
body_frame.pack(side ="top", expand = 1, anchor = "n", fill = "both", pady = 5)
cal = cal.DateEntry(body_frame, selectmode = "day", year = 2021, month = 9, day =1)
cal.grid(row =0, column =0, sticky = "nw", padx = 10)

cal_btn = tk.Button(body_frame, text = "Get Date", fg = font_color, bg = "#ff0000", relief = "flat", 
                    command = get_cal, bd = 0, font = ("Consolas, 10"))
cal_btn.grid(row=0, column =1, sticky = "nw")

calVar = tk.StringVar()
cal_lbl = tk.Label(body_frame, text ="", textvariable= calVar, bg = background_color, fg = font_color,
                    font = ("Consolas, 11"), bd = 0)
cal_lbl.grid(row=1, column = 0, columnspan = 3,pady = 10, sticky = "w", padx=10)

# calVar.trace('w', update_cal)

root.mainloop()