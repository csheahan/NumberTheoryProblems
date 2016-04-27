from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section5.problem3 import problem3

def load_problem(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.3", text="Problem 3", tags=["ch1.5.3"])
  tree.tag_bind("ch1.5.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Enter an a and b in the modified division algorithm to find "
  problemText += "the quotient and remainder: a = b * q + r, where -b/2 < r <= "
  problemText += "b/2"
  promptaText = "Enter a positive integer a:"
  promptbText = "Enter a positive integer b:"

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

    answerLabelText = "The quotient is " + str(answer[0]) + " and the "
    answerLabelText += "remainder is " + str(answer[1]) + ", or in other "
    answerLabelText += "words, " + a.get() + " = " + b.get() + " * "
    answerLabelText += str(answer[0]) + " + " + str(answer[1])

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
