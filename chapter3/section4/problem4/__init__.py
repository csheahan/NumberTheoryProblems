from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section4.problem4 import problem4 as problem4

def load_problem(tree, frame):
  tree.insert("ch3.4", "end", "ch3.4.4", text="Problem 4", tags=["ch3.4.4"])
  tree.tag_bind("ch3.4.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate (a, b, c, ..., n)"
  promptText = "Enter multiple integers delimeted by spaces (e.g. \"1 2 3\"):"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, a):
  helpers.clear_row(frame, 2)
  integers = []

  try:
    answerText = "("
    stringFrom = a.get().split()

    for item in stringFrom:
      integers.append(int(item))
      answerText += item + ", "

    answer = problem4.solve(integers)

    answerText = answerText[:-2]
    answerText += ") = " + str(answer)

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
