# -*- coding: utf-8 -*-

from Tkinter import *
import ttk
import functools
import helpers
from chapter4.section2.problem2 import problem2

def load_problem(tree, frame):
  tree.insert("ch4.2", "end", "ch4.2.2", text="Problem 2", tags=["ch4.2.2"])
  tree.tag_bind("ch4.2.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Solve for x in the equation `ax ≡ b mod p` given a, b, and p "
  problemText += "using an iterative method."
  promptaText = "Enter a positive integer a:"
  promptbText = "Enter a positive integer b:"
  promptpText = "Enter an modulus p:"

  helpers.generate_three_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    promptpText,
    problem_two_display_answer
  )

def problem_two_display_answer(frame, a, b, p):
  helpers.clear_row(frame, 2)

  try:
    answer = problem2.solve(int(a.get()), int(b.get()), int(p.get()))

    answerText = "The solution derived from iteration is "
    answerText += "x ≡ %d mod %s" % (answer, p.get())

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
