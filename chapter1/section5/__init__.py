from Tkinter import *
import ttk
import chapter1.section5.problem1
import chapter1.section5.problem2
import chapter1.section5.problem3
import chapter1.section5.problem4

def load_section_five(tree, frame):
  tree.insert("ch1", "end", "ch1.5", text="Section 5")
  chapter1.section5.problem1.load_problem_one(tree, frame)
  chapter1.section5.problem2.load_problem_two(tree, frame)
  chapter1.section5.problem3.load_problem_three(tree, frame)
  chapter1.section5.problem4.load_problem_four(tree, frame)