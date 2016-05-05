from Tkinter import *
import ttk
from chapter4.section1 import problem1
from chapter4.section1 import problem2
from chapter4.section1 import problem3
from chapter4.section1 import problem4

def load_section(tree, frame):
  tree.insert("ch4", "end", "ch4.1", text="Section 1")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)