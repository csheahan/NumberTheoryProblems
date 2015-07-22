from Tkinter import *
import ttk
import chapter1.section5.problem1

def load_section_five(tree, frame):
  tree.insert("ch1", "end", "ch1.5", text="Section 5")
  chapter1.section5.problem1.load_problem_one(tree, frame)