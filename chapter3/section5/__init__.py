from Tkinter import *
import ttk
import chapter3.section5.problem1
import chapter3.section5.problem2
import chapter3.section5.problem3
import chapter3.section5.problem4
import chapter3.section5.problem5
import chapter3.section5.problem6

def load_section(tree, frame):
  tree.insert("ch3", "end", "ch3.5", text="Section 5")
  chapter3.section5.problem1.load_problem(tree, frame)
  chapter3.section5.problem2.load_problem(tree, frame)
  chapter3.section5.problem3.load_problem(tree, frame)
  chapter3.section5.problem4.load_problem(tree, frame)
  chapter3.section5.problem5.load_problem(tree, frame)
  chapter3.section5.problem6.load_problem(tree, frame)