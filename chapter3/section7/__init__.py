from Tkinter import *
import ttk
from chapter3.section7 import problem1 as problem1
from chapter3.section7 import problem2 as problem2
from chapter3.section7 import problem3 as problem3

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.7", text="Section 7")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)