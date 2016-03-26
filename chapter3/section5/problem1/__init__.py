from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section5.problem1.problem1

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.1", text="Problem 1", tags=["ch3.5.1"])
  tree.tag_bind("ch3.5.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find all of the positive divisors of a positive integer from "
  problemText += "its prime factorization."
  promptText = "Enter a positive integer a:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_one_display_answer
  )

def problem_one_display_answer(frame, a):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section5.problem1.problem1.problem(int(a.get()))

    answerText = "The divisors of " + a.get() + " are: "

    for divisor in answer:
      answerText += str(divisor) + ", "

    answerText = answerText[:-2]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
