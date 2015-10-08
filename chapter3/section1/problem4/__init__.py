from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section1.problem4.problem4

def load_problem(tree, frame):
  tree.insert("ch3.1", "end", "ch3.1.4", text="Problem 4", tags=["ch3.1.4"])
  tree.tag_bind("ch3.1.4", '<1>',
    functools.partial(problem_four_view, frame))

def problem_four_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Given positive integers a and b not divisible by the same "
  problemText += "prime, find the smallest prime a * n + b"
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    problem_four_display_answer
  )

def problem_four_display_answer(frame, a, b):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section1.problem4.problem4.problem(
      int(a.get()),
      int(b.get())
    )

    answerText = "The smallest prime number in the arithmetic progression a "
    answerText += "* n + b is: " + str(answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except:
    helpers.clear_row(frame, 2)

    errorText = "An error has occurred. Please ensure that a and b are "
    errorText += "positive integers"

    errorLabel = Label(frame, text=errorText)
    errorLabel.grid(row=2, columnspan=5)
