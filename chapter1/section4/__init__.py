from Tkinter import *
import ttk
from chapter1.section4 import problem1
from chapter1.section4 import problem2
from chapter1.section4 import problem3

def load_section(tree, frame):
  tree.insert("ch1", "end", "ch1.4", text="Section 4")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
