from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section1.problem2.problem2

def load_problem_two(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.2", text="Problem 2", tags=["ch1.1.2"])
  tree.tag_bind("ch1.1.2", "<1>",
    functools.partial(problem_two_view, tree, frame))

def problem_two_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = u"Given a number \u03B1, find its spectrum sequence."
  promptText = u"Enter a real number \u03B1:"

  helpers.generate_prompt_and_input(tree,
    frame,
    problemText,
    promptText,
    problem_two_display_answer
    )

def problem_two_display_answer(tree, frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section1.problem2.problem2.problem(float(alpha.get()))

    answerLabelText = u"With an \u03B1 of " + unicode(float(alpha.get()))
    answerLabelText += u", we have a spectrum sequnce of ["

    for ele in answer:
      answerLabelText += unicode(ele) + u", "

    answerLabelText = answerLabelText[:-2]
    answerLabelText += u"]"

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = u"An error has occurred. Please ensure that \u03B1 is a"
    errorText += u" real number"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
