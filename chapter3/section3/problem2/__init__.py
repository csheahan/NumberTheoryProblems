from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section3.problem2 import problem2

def load_problem(tree, frame):
  tree.insert("ch3.3", "end", "ch3.3.2", text="Problem 2", tags=["ch3.3.2"])
  tree.tag_bind("ch3.3.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "List the Farey series of order n."
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_two_display_answer
  )

def problem_two_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem2.solve(int(n.get()))

    answerText = "The Farey series of order n is: "

    for fraction in answer:
      answerText += "(" + str(fraction[0]) + "/" + str(fraction[1]) + "), "

    answerText = answerText[:-2]
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
