from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section3.problem2.problem2

def load_problem_two(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.2", text="Problem 2", tags=["ch1.3.2"])
  tree.tag_bind("ch1.3.2", '<1>',
    functools.partial(problem_two_view, tree, frame))

def problem_two_view(tree, frame, event):
  helpers.clear_frame(frame)

  problemText = "Cover a 2^n X 2^n chessboard that is missing one square"
  problemText += "using L-shaped pieces"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(tree,
    frame,
    problemText,
    promptText,
    problem_two_display_answer
    )

def problem_two_display_answer(tree, frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section3.problem2.problem2.problem(int(alpha.get()))
    longestNum = len(answer[len(answer) - 1][len(answer) - 2]) + 1

    answerLabelText = "A 2^" + alpha.get() + " x 2^" + alpha.get() + " "
    answerLabelText += "chessboard with 1 square missing can be filled by L "
    answerLabelText += "blocks the following way:\n"

    formattedString = "{:<" + str(longestNum) + "}"

    for row in answer:
      for column in row:
        answerLabelText += formattedString.format(column)
      answerLabelText += "\n"

    answerText = Label(frame, text=answerLabelText, font="TkFixedFont")
    answerText.grid(row=2, columnspan=3)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that n is a positive "
    errorText += "integer"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=3)
