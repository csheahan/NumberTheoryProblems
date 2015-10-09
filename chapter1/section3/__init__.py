from Tkinter import *
import ttk
import chapter1.section3.problem1
import chapter1.section3.problem2
import chapter1.section3.problem3

def load_section(tree, frame):
  tree.insert("ch1", "end", "ch1.3", text="Section 3")
  chapter1.section3.problem1.load_problem(tree, frame)
  chapter1.section3.problem2.load_problem(tree, frame)
  chapter1.section3.problem3.load_problem(tree, frame)
