from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section4.problem2 import problem2

def load_problem(tree, frame):
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
    answer = problem2.solve(int(alpha.get()))

    answerLabelText = "The first " + alpha.get() + " Lucas numbers are: "

    for number in answer:
      answerLabelText += str(number) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
