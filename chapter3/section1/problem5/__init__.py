from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section1.problem5 import problem5 as problem5

def load_problem(tree, frame):
  tree.insert("ch3.1", "end", "ch3.1.5", text="Problem 5", tags=["ch3.1.5"])
  tree.tag_bind("ch3.1.5", '<1>',
    functools.partial(problem_five_view, frame))

def problem_five_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the lucky numbers less than a positive integer n"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_five_display_answer
  )

def problem_five_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem5.solve(int(n.get()))

    answerText = "The lucky numbers less than " + n.get() + " are: "

    for prime in answer:
      answerText += str(prime) + ", "

    answerText = answerText[:-2]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)