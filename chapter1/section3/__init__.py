from Tkinter import *
import ttk
import chapter1.section3.problem1

def load_section_three(tree, frame):
  tree.insert("ch1", "end", "ch1.3", text="Section 3")
  chapter1.section3.problem1.load_problem_one(tree, frame)
