from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section7.problem1 import problem1

def load_problem(tree, frame):
  tree.insert("ch3.7", "end", "ch3.7.1", text="Problem 1", tags=["ch3.7.1"])
  tree.tag_bind("ch3.7.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find all the solutions of a diophantine equation given its "
  problemText += "coefficients such that ax+by=c."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"
  promptcText = "Enter an integer c:"

  helpers.generate_three_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    promptcText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, a, b, c):
  helpers.clear_row(frame, 2)

  try:
    answer = problem1.solve(int(a.get()), int(b.get()), int(c.get()))

    if (answer[0] is None):
      answerText = "There is no answer because gcd(" + a.get() + ", " + b.get()
      answerText += ") = " + str(answer[1]) + " does not divide " + c.get()
    else:
      answerText = "x = " + answer[0] + ", y = " + answer[1]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 7)
