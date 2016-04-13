from Tkinter import *
import ttk
from chapter1.section1 import problem1 as problem1
from chapter1.section1 import problem2 as problem2
from chapter1.section1 import problem3 as problem3

def load_section(tree, frame):
  tree.insert("ch1", "end", "ch1.1", text="Section 1")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
