from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section3.problem1.problem1

def load_problem_one(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.1", text="Problem 1", tags=["ch1.3.1"])
  tree.tag_bind("ch1.3.1", '<1>',
    functools.partial(problem_one_view, tree, frame))

def problem_one_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = u"List the moves in the tower of Hanoi puzzle"

  prompt = Label(frame, text=problemText)
  prompt.grid(row=0)

  answer = chapter1.section3.problem1.problem1.problem()

  answerText = "The following valid moves in the tower of Hanoi puzzle: "

  for part in answer:
    answerText += part + ", "

  answerText = answerText[:-2]

  answerLabel = Label(frame, text=answerText)
  answerLabel.grid(row=1)
