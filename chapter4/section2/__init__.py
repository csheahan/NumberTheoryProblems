from Tkinter import *
import ttk
from chapter4.section2 import problem1

def load_section(tree, frame):
  tree.insert("ch4", "end", "ch4.2", text="Section 2")
  problem1.load_problem(tree, frame)