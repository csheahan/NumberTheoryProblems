from Tkinter import *
import ttk
from chapter3.section3 import problem1 as problem1
from chapter3.section3 import problem2 as problem2

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.3", text="Section 3")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)