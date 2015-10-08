from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section1.problem3.problem3

def load_problem_three(tree, frame):
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
    answer = chapter3.section1.problem3.problem3.problem(int(n.get()))

    answerText = u"\u03C0(" + unicode(n.get()) + u") = " 
    answerText += unicode(str(answer))
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = u"An error has occurred. Please ensure that \u03C0 is a "
    errorText += u"positive integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)