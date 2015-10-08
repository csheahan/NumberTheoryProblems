from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section4.problem1.problem1

def load_problem(tree, frame):
  tree.insert("ch1.4", "end", "ch1.4.1", text="Problem 1", tags=["ch1.4.1"])
  tree.tag_bind("ch1.4.1", '<1>',
    functools.partial(problem_one_view, frame))

def problem_one_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the first n terms of the Fibonacci sequence"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_one_display_answer)

def problem_one_display_answer(frame, alpha):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section4.problem1.problem1.problem(int(alpha.get()))

    answerLabelText = "The first " + alpha.get() + " Fibonacci numbers are: "

    for number in answer:
      answerLabelText += str(number) + ", "

    answerLabelText = answerLabelText[:-2]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)