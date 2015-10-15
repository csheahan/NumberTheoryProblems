from Tkinter import *
import ttk
import chapter3.section4.problem1
import chapter3.section4.problem2
import chapter3.section4.problem3
import chapter3.section4.problem4

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.4", text="Section 4")
  chapter3.section4.problem1.load_problem(tree, frame)
  chapter3.section4.problem2.load_problem(tree, frame)
  chapter3.section4.problem3.load_problem(tree, frame)
  chapter3.section4.problem4.load_problem(tree, frame)
