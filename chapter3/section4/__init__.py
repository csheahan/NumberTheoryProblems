from Tkinter import *
import ttk
from chapter3.section4 import problem1
from chapter3.section4 import problem2
from chapter3.section4 import problem3
from chapter3.section4 import problem4
from chapter3.section4 import problem5

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.4", text="Section 4")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)
  problem5.load_problem(tree, frame)
