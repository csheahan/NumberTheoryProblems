from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section4.problem1 import problem1

def load_problem(tree, frame):
  tree.insert("ch3.4", "end", "ch3.4.1", text="Problem 1", tags=["ch3.4.1"])
  tree.tag_bind("ch3.4.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate (a, b) via the Euclidean algorithm"
  promptAText = "Enter an integer a:"
  promptBText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptAText,
    promptBText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = problem1.solve(int(b.get()), int(a.get()))

    answerText = "(" + a.get() + ", " + b.get() + ") = " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
