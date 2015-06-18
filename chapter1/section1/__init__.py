from Tkinter import *
import ttk
import chapter1.section1.problem1
import chapter1.section1.problem2

def load_section_one(tree, frame):
  tree.insert("ch1", "end", "ch1.1", text="Section 1")
  chapter1.section1.problem1.load_problem_one(tree, frame)
  chapter1.section1.problem2.load_problem_two(tree, frame)
