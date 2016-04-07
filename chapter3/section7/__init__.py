from Tkinter import *
import ttk
import chapter3.section7.problem1

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.7", text="Section 7")
  chapter3.section7.problem1.load_problem(tree, frame)