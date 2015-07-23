from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section3.problem3.problem3

def load_problem_three(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.3", text="Problem 3", tags=["ch1.3.3"])
  tree.tag_bind("ch1.3.3", '<1>',
    functools.partial(problem_three_view, tree, frame))

def problem_three_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Given a rational number p/q, such that p < q and p and q are "
  problemText += "positive integers, express p/q as an Egyption fraction"
  ppromptText = "Enter a positive integer p:"
  qpromptText = "Enter a positive integer q:"

  helpers.generate_two_prompt_and_input(
    tree,
    frame,
    problemText,
    ppromptText,
    qpromptText,
    problem_three_display_answer
  )


def problem_three_display_answer(tree, frame, p, q):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section3.problem3.problem3.problem(
      int(p.get()),
      int(q.get()))

    answerLabelText = str(p.get()) + "/" + str(q.get()) + " = "

    for tup in answer:
      answerLabelText += str(tup[0]) + "/" + str(tup[1]) + " + "

    answerLabelText = answerLabelText[:-3]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=5)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occured. Please ensure that p and q are "
    errorText += "positive integers and that p < q"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=5)
