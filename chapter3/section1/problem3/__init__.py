from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section1.problem3 import problem3 as problem3

def load_problem(tree, frame):
  tree.insert("ch3.1", "end", "ch3.1.3", text="Problem 3", tags=["ch3.1.3"])
  tree.tag_bind("ch3.1.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = u"Calculate \u03C0 as described in problem 24."
  promptText = u"Enter a positive integer \u03C0:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_three_display_answer
  )

def problem_three_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem3.solve(int(n.get()))

    answerText = u"\u03C0(" + unicode(n.get()) + u") = "
    answerText += unicode(str(answer))
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)