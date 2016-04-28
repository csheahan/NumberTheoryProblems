from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section1.problem1 import problem1

def load_problem(tree, frame):
  tree.insert("ch3.1", "end", "ch3.1.1", text="Problem 1", tags=["ch3.1.1"])
  tree.tag_bind("ch3.1.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Given a positive integer n, determine if it is prime via "
  problemText += "trial division."
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem1.solve(int(n.get()))

    answerText = n.get() + " is "

    if (answer):
      answerText += "not "

    answerText += "a prime number"

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)