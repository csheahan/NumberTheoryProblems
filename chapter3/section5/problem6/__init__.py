from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section5.problem6.problem6

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.6", text="Problem 6", tags=["ch3.5.6"])
  tree.tag_bind("ch3.5.6", '<1>',
    functools.partial(problem_six_view, frame))

def problem_six_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the number of powerful numbers less than a positive "
  problemText += "integer n."
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_six_display_answer
  )

def problem_six_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section5.problem6.problem6.problem(int(n.get()))

    answerText = "The number of powerful numbers less than " + n.get() + " is: "
    answerText += str(len(answer)) + ". Those numbers are "

    for num in answer:
      answerText += str(num) + ", "

    answerText = answerText[:-2]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
