from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section1.problem3.problem3

def load_problem_three(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.3", text="Problem 3", tags=["ch1.1.3"])
  tree.tag_bind("ch1.1.3", "<1>",
    functools.partial(problem_three_view, tree, frame))

def problem_three_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the first n Ulam numbers"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(tree,
    frame,
    problemText,
    promptText,
    problem_three_display_answer
    )

def problem_three_display_answer(tree, frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section1.problem3.problem3.problem(int(alpha.get()))

    answerLabelText = "The first " + alpha.get() + " Ulam numbers are: "

    for ele in answer:
      answerLabelText += str(ele) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = u"An error has occurred. Please ensure that n is a"
    errorText += u" positive integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
