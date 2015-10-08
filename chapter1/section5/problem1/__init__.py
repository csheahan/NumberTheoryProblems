from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section5.problem1.problem1

def load_problem_one(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.1", text="Problem 1", tags=["ch1.5.1"])
  tree.tag_bind("ch1.5.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Decide if an integer x is divisble by an integer y"
  promptXText = "Enter an integer x:"
  promptYText = "Enter an integer y:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptXText,
    promptYText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, x, y):
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
    answerText.grid(row=2, columnspan=5)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that x and y are "
    errorText += "integers"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=5)
