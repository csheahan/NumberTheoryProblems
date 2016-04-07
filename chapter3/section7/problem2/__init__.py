from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section7.problem2.problem2

def load_problem(tree, frame):
  tree.insert("ch3.7", "end", "ch3.7.2", text="Problem 2", tags=["ch3.7.2"])
  tree.tag_bind("ch3.7.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find all the positive solutions of a diophantine equation "
  problemText += "given its coefficients such that ax+by=c."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"
  promptcText = "Enter an integer c:"

  helpers.generate_three_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    promptcText,
    problem_two_display_answer
  )

def problem_two_display_answer(frame, a, b, c):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section7.problem2.problem2.problem(
      int(a.get()),
      int(b.get()),
      int(c.get())
    )

    if (answer is None):
      answerText = "There are either infinite solutions or no solutions"
    else:
      answerText = "There are " + str(answer) + " positive solutions"

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 7)
