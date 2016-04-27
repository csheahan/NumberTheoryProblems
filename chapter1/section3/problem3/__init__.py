from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section3.problem3 import problem3

def load_problem(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.3", text="Problem 3", tags=["ch1.3.3"])
  tree.tag_bind("ch1.3.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Given a rational number p/q, such that p < q and p and q are "
  problemText += "positive integers, express p/q as an Egyption fraction"
  ppromptText = "Enter a positive integer p:"
  qpromptText = "Enter a positive integer q:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    ppromptText,
    qpromptText,
    problem_three_display_answer
  )


def problem_three_display_answer(frame, p, q):
  helpers.clear_row(frame, 2)

  try:
    answer = problem3.solve(int(p.get()), int(q.get()))

    answerLabelText = str(p.get()) + "/" + str(q.get()) + " = "

    for tup in answer:
      answerLabelText += str(tup[0]) + "/" + str(tup[1]) + " + "

    answerLabelText = answerLabelText[:-3]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
