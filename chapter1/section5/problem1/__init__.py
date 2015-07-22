from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section5.problem1.problem1

def load_problem_one(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.1", text="Problem 1", tags=["ch1.5.1"])
  tree.tag_bind("ch1.5.1", '<1>',
    functools.partial(problem_one_view, tree, frame))

def problem_one_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Decide if an integer x is divisble by an integer y"
  promptXText = "Enter a positive integer x:"
  promptYText = "Enter a positive integer y:"

  prompt = Label(frame, text=problemText)
  prompt.grid(row=0, columnspan=5)

  xlabel = Label(frame, text=promptXText)
  xlabel.grid(row=1, column=0)

  xprompt = Entry(frame)
  xprompt.grid(row=1, column=1)

  ylabel = Label(frame, text=promptYText)
  ylabel.grid(row=1, column=2)

  yprompt = Entry(frame)
  yprompt.grid(row=1, column=3)

  submitButton = Button(frame,
    text="submit",
    command=functools.partial(problem_one_display_answer,
      tree,
      frame,
      xprompt,
      yprompt)
    )
  submitButton.grid(row=1, column=4)


def problem_one_display_answer(tree, frame, x, y):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section5.problem1.problem1.problem(
      int(x.get()),
      int(y.get())
    )
    answerLabelText = ""

    if (answer):
      answerLabelText = x.get() + " is divisble by " + y.get()
    else:
      answerLabelText = x.get() + " is not divisble by " + y.get()

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that x and y are "
    errorText += "integers"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
