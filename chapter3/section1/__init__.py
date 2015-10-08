from Tkinter import *
import ttk
import chapter3.section1.problem1
import chapter3.section1.problem2
import chapter3.section1.problem3
import chapter3.section1.problem4

def load_section_one(tree, frame):
  tree.insert("ch3", "end", "ch3.1", text="Section 1")
  chapter3.section1.problem1.load_problem_one(tree, frame)
  chapter3.section1.problem2.load_problem_two(tree, frame)
  chapter3.section1.problem3.load_problem_three(tree, frame)
  chapter3.section1.problem4.load_problem_four(tree, frame)