from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section3.problem1 import problem1 as problem1

def load_problem(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.1", text="Problem 1", tags=["ch1.3.1"])
  tree.tag_bind("ch1.3.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = u"List the moves in the tower of Hanoi puzzle"

  prompt = Label(frame, text=problemText)
  prompt.grid(row=0)

  answer = problem1.solve()

  answerText = "The following valid moves in the tower of Hanoi puzzle: "

  for part in answer:
    answerText += part + ", "

  answerText = answerText[:-2]

  answerLabel = Label(frame, text=answerText)
  answerLabel.grid(row=1)
