from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section4.problem5 import problem5 as problem5

def load_problem(tree, frame):
  tree.insert("ch3.4", "end", "ch3.4.5", text="Problem 5", tags=["ch3.4.5"])
  tree.tag_bind("ch3.4.5", '<1>',
    functools.partial(problem_five_view, frame))

def problem_five_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate the Bezout coefficients for positive integers a "
  problemText += "and b."
  promptAText = "Enter an integer a:"
  promptBText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptAText,
    promptBText,
    problem_five_display_answer
  )

def problem_five_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = problem5.solve(int(b.get()), int(a.get()))

    answerText = "The Bezout coefficients of " + a.get() + " and "
    answerText += b.get() + " are " + str(answer[0]) + " and " + str(answer[1])

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
