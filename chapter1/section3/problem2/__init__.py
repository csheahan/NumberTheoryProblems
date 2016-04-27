from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section3.problem2 import problem2

def load_problem(tree, frame):
  tree.insert("ch1.3", "end", "ch1.3.2", text="Problem 2", tags=["ch1.3.2"])
  tree.tag_bind("ch1.3.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Cover a 2^n X 2^n chessboard that is missing one square"
  problemText += "using L-shaped pieces"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_two_display_answer
    )

def problem_two_display_answer(frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = problem2.solve(int(alpha.get()))
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
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
