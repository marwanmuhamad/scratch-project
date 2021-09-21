import tkinter as tk 

root = tk.Tk()  

width = 400 
height = 400
x = int(0.5*(root.winfo_screenwidth() - width))
y = int(0.5*(root.winfo_screenheight() - height))
root.geometry("{}x{}+{}+{}".format(width, height, x, y))
root.title("Apps with Menu")

# Define variables:
label = tk.StringVar()
label.set("")

#click command:
def file_command():
    label.set("")
    label.set("You clicked the file menu!")
def file_new():
    hide_all_frames()
    file_new_frame.pack(fill = "both", expand = 1)
#   my_label = tk.Label(file_new_frame, text = "", textvariable=label, bg = "#ff0000")
#   my_label.pack()

def cut_command():
    hide_all_frames()
    edi_cut_frame.pack(fill = "both", expand = 1)
    # label.set("")
    # label.set("You clicked the cut menu!")

def copy_command():
    label.set("")
    label.set("You clicked the copy menu!")
    
def find_command():
    label.set("")
    label.set("You clicked the find menu!")

def find_next_command():
    label.set("")
    label.set("You clicked the find next menu!")

# Hide all frames:
def hide_all_frames():
    file_new_frame.pack_forget()
    edi_cut_frame.pack_forget()

# Define menu 
my_menu = tk.Menu(root,relief = "flat", bd = 0)
root.configure(menu = my_menu)

# Create menu items
file_menu = tk.Menu(my_menu, relief = "flat", bd = 0, tearoff=0)
my_menu.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "New...", command = file_new)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = root.quit)

# Create an edit menu item 
edit_menu = tk.Menu(my_menu, relief = "flat", bd = 0, tearoff=0)
my_menu.add_cascade(label = "Edit", menu = edit_menu) 
edit_menu.add_command(label = "cut", command = cut_command)
# edit_menu.add_separator()
edit_menu.add_command(label = "copy", command = copy_command)

# Create an option menu item 
option_menu = tk.Menu(my_menu, relief = "flat", bd = 0, tearoff=0)
my_menu.add_cascade(label = "Options", menu = option_menu) 
option_menu.add_command(label = "Find", command = find_command)
# option_menu.add_separator()
option_menu.add_command(label = "Find Next", command = find_next_command)

# Create some frames:
file_new_frame = tk.Frame(root, width = width, height = height, bg = "#ff0000")
edi_cut_frame = tk.Frame(root, width = width, height = height, bg = "#0000ff")









root.mainloop()