from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section4.problem3.problem3

def load_problem(tree, frame):
  tree.insert("ch3.4", "end", "ch3.4.3", text="Problem 3", tags=["ch3.4.3"])
  tree.tag_bind("ch3.4.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate (a, b) without using division."
  promptAText = "Enter an integer a:"
  promptBText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptAText,
    promptBText,
    problem_three_display_answer
  )

def problem_three_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section4.problem3.problem3.problem(
      int(b.get()),
      int(a.get())
    )

    answerText = "(" + a.get() + ", " + b.get() + ") = " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
