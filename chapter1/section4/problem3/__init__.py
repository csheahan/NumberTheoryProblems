from Tkinter import *
import ttk
import functools
import helpers
import chapter1.section4.problem3.problem3

def load_problem(tree, frame):
  tree.insert("ch1.4", "end", "ch1.4.3", text="Problem 3", tags=["ch1.4.3"])
  tree.tag_bind("ch1.4.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Calculate the Zeckendorf representation of an integer n"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_three_display_answer)

def problem_three_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter1.section4.problem3.problem3.problem(int(n.get()))

    answerLabelText = "The Zeckendorf representation of " + n.get() + " is: "

    for num in answer:
      answerLabelText += str(num) + " + "

    answerLabelText = answerLabelText[:-3]

    answerText = Label(frame, text=answerLabelText)
    answerText.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)