from Tkinter import *
import ttk
import chapter3.section4.problem1

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.4", text="Section 4")
  chapter3.section4.problem1.load_problem(tree, frame)
