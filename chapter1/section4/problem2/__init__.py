from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section4.problem2.problem2

def load_problem_two(tree, frame):
  tree.insert("ch1.4", "end", "ch1.4.2", text="Problem 2", tags=["ch1.4.2"])
  tree.tag_bind("ch1.4.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the first n Lucas numbers"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_two_display_answer)

def problem_two_display_answer(frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section4.problem2.problem2.problem(int(alpha.get()))

    answerLabelText = "The first " + alpha.get() + " Lucas numbers are: "

    for number in answer:
      answerLabelText += str(number) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that n is a positive "
    errorText += "integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
