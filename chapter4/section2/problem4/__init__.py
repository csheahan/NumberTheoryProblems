# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import functools
import helpers
from chapter4.section2.problem4 import problem4

def load_problem(tree, frame):
  tree.insert("ch4.2", "end", "ch4.2.4", text="Problem 4", tags=["ch4.2.4"])
  tree.tag_bind("ch4.2.4", '<1>', functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Solve for x in the equation `ax ≡ b mod m` given a, b, and m "
  problemText += "using inverses."
  promptaText = "Enter a positive integer a:"
  promptbText = "Enter a positive integer b:"
  promptmText = "Enter an modulus m:"

  helpers.generate_three_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    promptmText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, a, b, m):
  helpers.clear_row(frame, 2)

  try:
    answer = problem4.solve(int(a.get()), int(b.get()), int(m.get()))

    answerText = "x ≡ %d mod %s" % (answer, m.get())

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
