from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section5.problem4 import problem4

def load_problem(tree, frame):
  tree.insert("ch1.5", "end", "ch1.5.4", text="Problem 4", tags=["ch1.5.4"])
  tree.tag_bind("ch1.5.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Compute the Collatz sequence for a positive integer n"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_four_display_answer)

def problem_four_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = problem4.solve(int(n.get()))

    answerLabelText = "The Collatz sequence of " + n.get() + " is: "

    for num in answer:
      answerLabelText += str(num) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)