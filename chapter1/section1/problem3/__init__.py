from Tkinter import *
import ttk
import functools
import helpers
from chapter1.section1.problem3 import problem3 as problem3

def load_problem(tree, frame):
  tree.insert("ch1.1", "end", "ch1.1.3", text="Problem 3", tags=["ch1.1.3"])
  tree.tag_bind("ch1.1.3", "<1>",
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the first n Ulam numbers"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_three_display_answer
    )

def problem_three_display_answer(frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = problem3.solve(int(alpha.get()))

    answerLabelText = "The first " + alpha.get() + " Ulam numbers are: "

    for ele in answer:
      answerLabelText += str(ele) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)