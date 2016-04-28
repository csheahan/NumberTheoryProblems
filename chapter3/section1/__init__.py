from Tkinter import *
import ttk
from chapter3.section1 import problem1
from chapter3.section1 import problem2
from chapter3.section1 import problem3
from chapter3.section1 import problem4
from chapter3.section1 import problem5

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.1", text="Section 1")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)
  problem5.load_problem(tree, frame)