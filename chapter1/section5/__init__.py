from Tkinter import *
import ttk
from chapter1.section5 import problem1 as problem1
from chapter1.section5 import problem2 as problem2
from chapter1.section5 import problem3 as problem3
from chapter1.section5 import problem4 as problem4

def load_section(tree, frame):
  tree.insert("ch1", "end", "ch1.5", text="Section 5")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)
