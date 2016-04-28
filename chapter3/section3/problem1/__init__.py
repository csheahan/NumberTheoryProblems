from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section3.problem1 import problem1

def load_problem(tree, frame):
  tree.insert("ch3.3", "end", "ch3.3.1", text="Problem 1", tags=["ch3.3.1"])
  tree.tag_bind("ch3.3.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate (m, n)"
  promptMText = "Enter an integer m:"
  promptNText = "Enter an integer n:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptMText,
    promptNText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, m, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem1.solve(int(m.get()), int(n.get()))

    answerText = "(m, n) = " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
