from Tkinter import *
import ttk
import functools
import helpers
from chapter4.section1.problem3 import problem3

def load_problem(tree, frame):
  tree.insert("ch4.1", "end", "ch4.1.3", text="Problem 3", tags=["ch4.1.3"])
  tree.tag_bind("ch4.1.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Perform modular multiplication when the modulus is less than "
  problemText += "half of the word size of the computer."
  promptText = "Enter a multiplication problem in the form `num*num`:"
  promptmText = "Enter an modulus m:"

  helpers.generate_two_prompt_and_input(
    frame,
    problemText,
    promptText,
    promptmText,
    problem_three_display_answer
  )

def problem_three_display_answer(frame, a, m):
  helpers.clear_row(frame, 2)

  try:
    answer = problem3.solve(a.get(), int(m.get()))

    answerText = "%s mod %s = %d" % (a.get(), m.get(), answer)
    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=5)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 5)
