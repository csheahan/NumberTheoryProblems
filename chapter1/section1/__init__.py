from Tkinter import *
import ttk
import functools
import chapter1.section1.problem1
import chapter1.section1.problem2
import helpers

def load_section_one(tree, frame):
  tree.insert("ch1", "end", "ch1.1", text="Section 1")
  load_problem_one(tree, frame)
  load_problem_two(tree, frame)

def load_problem_one(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.1", text="Problem 1", tags=["ch1.1.1"])
  tree.tag_bind("ch1.1.1", '<1>',
    functools.partial(problem_one_view, tree, frame))

def problem_one_view(tree, frame, event):
  helpers.clear_frame(frame)

  prompt = Label(frame, text=u"Given a number \u03B1, find rational number " +
    u"p/q such that |\u03B1 - p/q| \u2264 1/q^2")
  prompt.grid(row=0, columnspan=3)

  entryLabel = Label(frame, text=u"Enter an \u03B1:")
  entryLabel.grid(row=1, column=0)
  alpha = Entry(frame)
  alpha.grid(row=1, column=1)
  submitButton = Button(frame,
    text="submit",
    command=functools.partial(problem_one_display_answer, tree, frame, alpha))
  submitButton.grid(row=1, column=2)

def problem_one_display_answer(tree, frame, alpha):
  helpers.clear_row(frame, 2)

  answer = chapter1.section1.problem1.problem(int(alpha.get()))

  answerText = Label(frame, text=u"With an \u03B1 of " +
    unicode(int(alpha.get())) + u" we have the inequality " +
    unicode(answer[0][2]) + u" \u2264 " + unicode(answer[0][3]) +
    u" where p=" + unicode(answer[0][0]) + u" and q=" +
    unicode(answer[0][1]))
  
  answerText.grid(row=2, columnspan=3)

def load_problem_two(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.2", text="Problem 2", tags=["ch1.1.2"])
  tree.tag_bind("ch1.1.2", "<1>",
    functools.partial(problem_two_view, tree, frame))

def problem_two_view(tree, frame, event):
  helpers.clear_frame(frame)

  prompt = Label(frame, text=u"Given a number \u03B1, find its spectrum " +
    u"sequence")
  prompt.grid(row=0, columnspan=3)

  entryLabel = Label(frame, text=u"Enter an \u03B1:")
  entryLabel.grid(row=1, column=0)
  alpha = Entry(frame)
  alpha.grid(row=1, column=1)
  submitButton = Button(frame,
    text="submit",
    command=functools.partial(problem_two_display_answer, tree, frame, alpha))
  submitButton.grid(row=1, column=2)

def problem_two_display_answer(tree, frame, alpha):
  helpers.clear_row(frame, 2)

  answer = chapter1.section1.problem2.problem(float(alpha.get()))

  answerLabelText = u"With an \u03B1 of " + unicode(float(alpha.get()))
  answerLabelText += u", we have a spectrum sequnce of ["

  for ele in answer:
    answerLabelText += unicode(ele) + u", "

  answerLabelText = answerLabelText[:-2]
  answerLabelText += u"]"

  answerText = Label(frame, text=answerLabelText)
  answerText.grid(row=2, columnspan=3)
