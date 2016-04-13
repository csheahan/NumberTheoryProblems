from Tkinter import *
import ttk
from chapter3.section5 import problem1 as problem1
from chapter3.section5 import problem2 as problem2
from chapter3.section5 import problem3 as problem3
from chapter3.section5 import problem4 as problem4
from chapter3.section5 import problem5 as problem5
from chapter3.section5 import problem6 as problem6

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.5", text="Section 5")
  problem1.load_problem(tree, frame)
  problem2.load_problem(tree, frame)
  problem3.load_problem(tree, frame)
  problem4.load_problem(tree, frame)
  problem5.load_problem(tree, frame)
  problem6.load_problem(tree, frame)