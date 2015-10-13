from Tkinter import *
import ttk
import chapter3.section3.problem1

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.3", text="Section 3")
  chapter3.section3.problem1.load_problem(tree, frame)