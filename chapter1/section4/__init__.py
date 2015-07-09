from Tkinter import *
import ttk
import chapter1.section4.problem1
import chapter1.section4.problem2

def load_section_four(tree, frame):
  tree.insert("ch1", "end", "ch1.4", text="Section 4")
  chapter1.section4.problem1.load_problem_one(tree, frame)
  chapter1.section4.problem2.load_problem_two(tree, frame)
