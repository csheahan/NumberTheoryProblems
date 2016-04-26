from Tkinter import *
import ttk
import functools
import helpers
from chapter4.section1.problem1 import problem1

def load_problem(tree, frame):
  tree.insert("ch4.1", "end", "ch4.1.1", text="Problem 4", tags=["ch4.1.1"])
  tree.tag_bind("ch4.1.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the least nonnegative residue of an integer with a fixed "
  problemText += "modulus"
  promptaText = "Enter an integer a:"
  promptmText = "Enter an modulus m:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptmText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, a, m):
  helpers.clear_row(frame, 2)

  try:
    answer = problem1.solve(int(a.get()), int(m.get()))

    answerText = "The least nonnegative residue is %d" % answer
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
