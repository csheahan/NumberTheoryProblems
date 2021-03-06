from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section5.problem4 import problem4

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.4", text="Problem 4", tags=["ch3.5.4"])
  tree.tag_bind("ch3.5.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the number of zeros at the end of the decimal expansion "
  problemText += "of n!"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem4.solve(int(n.get()))

    answerText = "The number of zeros at the end of the decimal expansion of "
    answerText += n.get() + "! is " + str(answer)

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
