from Tkinter import *
import ttk
from chapter4.section2 import problem1
from chapter4.section2 import problem2
from chapter4.section2 import problem3
from chapter4.section2 import problem4

def load_section(tree, frame):
  tree.insert("ch4", "end", "ch4.2", text="Section 2")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)