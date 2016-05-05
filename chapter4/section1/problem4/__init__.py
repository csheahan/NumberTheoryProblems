from Tkinter import *
import ttk
import functools
import helpers
from chapter4.section1.problem4 import problem4

def load_problem(tree, frame):
  tree.insert("ch4.1", "end", "ch4.1.4", text="Problem 4", tags=["ch4.1.4"])
  tree.tag_bind("ch4.1.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Perform modular exponentiation, e.g. solve b^N mod m"
  promptbText = "Enter a b:"
  promptnText = "Enter a N:"
  promptmText = "Enter an modulus m:"

  helpers.generate_three_prompt_and_input(
    frame,
    problemText,
    promptbText,
    promptnText,
    promptmText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, b, n, m):
  helpers.clear_row(frame, 2)

  try:
    answer = problem4.solve(int(b.get()), int(n.get()), int(m.get()))

    answerText = "%s^%s mod %s = %d" % (b.get(), n.get(), m.get(), answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
