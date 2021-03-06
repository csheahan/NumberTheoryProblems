from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section5.problem3 import problem3

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.3", text="Problem 3", tags=["ch3.5.3"])
  tree.tag_bind("ch3.5.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the least common multiple of two positive integers a and "
  problemText += "b from their prime factorizations."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    problem_three_display_answer
  )

def problem_three_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = problem3.solve(int(a.get()), int(b.get()))

    answerText = "[" + a.get() + ", " + b.get() + "] = " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
