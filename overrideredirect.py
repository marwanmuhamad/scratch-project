import tkinter as tk  

root = tk.Tk()
width = 300 
height = 300 
x = int(0.5*(root.winfo_screenwidth() - width))
y = int(0.5*(root.winfo_screenheight() - height))
root.geometry("{0}x{1}+{2}+{3}".format(width, height, x, y))
root.overrideredirect(True)
print(root.winfo_screenwidth())
print(root.winfo_screenheight())

def get_pos(event):
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    print(root.winfo_x(), root.winfo_y())
    startx = event.x_root
    starty = event.y_root
    print(event.x_root, event.y_root)

    ywin = ywin - starty
    xwin = xwin - startx

    def move_win(event):
        # print(event)
        root.geometry(f"+{event.x_root + xwin}+{event.y_root + ywin}")

    # startx = event.x_root
    # starty = event.y_root

    title_frame.bind("<B1-Motion>", move_win)
    title_lbl.bind("<B1-Motion>", move_win)

def min_window():
    root.overrideredirect(False)
    root.iconify()

def callback(event):
    # print(event)
    root.deiconify()
    root.overrideredirect(True)

def screen_appear(event):
    # print(event)
    # root.deiconify()
    root.overrideredirect(True)

title_frame = tk.Frame(root, width=300, bg = "#56ba65", relief = "flat", height = 10)
title_frame.pack(fill = "x", expand = 1, side = "top", anchor = "ne")

title_frame.bind("<Button-1>", get_pos)
title_frame.bind("<Map>", screen_appear)

title_lbl = tk.Label(title_frame, text = "Simple App", fg = "#ffffff",bg = "#56ba65", font = ("Roboto, 11"))
title_lbl.pack(side = "left", padx = 5)
title_lbl.bind("Button-1", get_pos)

close_btn = tk.Button(title_frame, text = "\u00d7", command = root.quit, relief = "flat", 
                        bd = 0, bg = "#fabc12", fg = "#ffffff", font = ("Roboto, 11"))
close_btn.pack(side = "right", padx = 0, ipadx = 3)

min_btn = tk.Button(title_frame, text = "\u0336", command = min_window, relief = "flat", 
                        bd = 0, bg = "#fabc12", fg = "#ffffff", font = ("Roboto, 11"))
min_btn.pack(side = "right", padx = 1, ipadx = 5)






root.mainloop()

