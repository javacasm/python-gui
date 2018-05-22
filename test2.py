import tkinter as tk        # 1 imports

win = tk.Tk()               # 2 Create instance
win.title("Python GUI")     # 3 Add a title       
    
win.resizable(0, 0)         # 4 Disable resizing the GUI

from tkinter import ttk    # 3
# Modify adding a Label                                      # 0
aLabel = ttk.Label(win, text="A Label")                      # 2
aLabel.grid(column=0, row=0)                                 # 3


# Button Click Event Callback Function                       # 4
def clickMe():                                               # 5
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')

# Adding a Button                                            # 6
action = ttk.Button(win, text="Click Me!", command=clickMe)  # 7
action.grid(column=1, row=0)                                 # 8

win.mainloop()

