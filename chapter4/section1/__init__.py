from Tkinter import *
import ttk
from chapter4.section1 import problem1
from chapter4.section1 import problem2

def load_section(tree, frame):
  tree.insert("ch4", "end", "ch4.1", text="Section 1")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)