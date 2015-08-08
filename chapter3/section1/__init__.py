from Tkinter import *
import ttk
import chapter3.section1.problem1

def load_section_one(tree, frame):
  tree.insert("ch3", "end", "ch3.1", text="Section 1")
  chapter3.section1.problem1.load_problem_one(tree, frame)