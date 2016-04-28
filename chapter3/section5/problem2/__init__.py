from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section5.problem2 import problem2

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.2", text="Problem 2", tags=["ch3.5.2"])
  tree.tag_bind("ch3.5.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the greatest common divisor of two positive integers "
  problemText += "from their prime factorizations."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    problem_two_display_answer
  )

def problem_two_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = problem2.solve(int(a.get()), int(b.get()))

    answerText = "(" + a.get() + ", " + b.get() + ") = " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
