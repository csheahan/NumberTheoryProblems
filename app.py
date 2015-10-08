# Load GUI libraries
import Tkinter
from Tkinter import *
import ttk

# Work with weird Tkinter installs
Tkinter.wantobjects = False

import chapter1
import chapter3

# Class containing tk instance
class App:
  # Constructor
  def __init__(self, master):
    frame = Frame(master)
    frame.pack(side=LEFT)
    rightSide = Frame(master)
    rightSide.pack(side=LEFT)

    tree = ttk.Treeview(frame)
    chapter1.load_chapter_one(tree, rightSide)
    chapter3.load_chapter_three(tree, rightSide)
    tree.pack()

# Make tk root widget
root = Tk()

app = App(root)

root.mainloop()
root.destroy()
