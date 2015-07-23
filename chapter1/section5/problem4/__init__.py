from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section5.problem4.problem4

def load_problem_four(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.4", text="Problem 4", tags=["ch1.5.4"])
  tree.tag_bind("ch1.5.4", '<1>',
    functools.partial(problem_four_view, tree, frame))

def problem_four_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Compute the Collatz sequence for a positive integer n"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(tree,
    frame,
    problemText,
    promptText,
    problem_four_display_answer)

def problem_four_display_answer(tree, frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section5.problem4.problem4.problem(int(n.get()))

    answerLabelText = "The Collatz sequence of " + n.get() + " is: "

    for num in answer:
      answerLabelText += str(num) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that n is a positive "
    errorText += "integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)