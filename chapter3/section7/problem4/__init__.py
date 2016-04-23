from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section7.problem4 import problem4 as problem4

def load_problem(tree, frame):
  tree.insert("ch3.7", "end", "ch3.7.4", text="Problem 4", tags=["ch3.7.4"])
  tree.tag_bind("ch3.7.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "find all positive integers n for which ax+by=n has no "
  problemText += "positive solutions given a, b."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = problem4.solve(int(a.get()), int(b.get()))

    answerText = "When n = "

    for n in answer:
      answerText += str(n) + ", "

    answerText = answerText[:-2]
    answerText += " there are no positive solutions."

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 7)
