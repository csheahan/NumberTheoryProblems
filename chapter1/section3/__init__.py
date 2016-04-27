from Tkinter import *
import ttk
from chapter1.section3 import problem1
from chapter1.section3 import problem2
from chapter1.section3 import problem3

def load_section(tree, frame):
  tree.insert("ch1", "end", "ch1.3", text="Section 3")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
