from Tkinter import *
import ttk
import chapter3.section5.problem1

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.5", text="Section 5")
  chapter3.section5.problem1.load_problem(tree, frame)