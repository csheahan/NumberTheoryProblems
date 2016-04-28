from Tkinter import *
import ttk
import functools
import helpers
from chapter3.section7.problem3 import problem3

def load_problem(tree, frame):
  tree.insert("ch3.7", "end", "ch3.7.3", text="Problem 3", tags=["ch3.7.3"])
  tree.tag_bind("ch3.7.3", '<1>',
    functools.partial(problem_three_view, frame))

def problem_three_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find all the positive solutions of a diophantine equation "
  problemText += "given its coefficients such that ax+by+cz=d."
  promptaText = "Enter an integer a:"
  promptbText = "Enter an integer b:"
  promptcText = "Enter an integer c:"
  promptdText = "Enter an integer d:"

  helpers.generate_four_prompt_and_input(
    frame,
    problemText,
    promptaText,
    promptbText,
    promptcText,
    promptdText,
    problem_three_display_answer
  )

def problem_three_display_answer(frame, a, b, c, d):
  helpers.clear_row(frame, 3)

  try:
    answer = problem3.solve(int(a.get()),
                            int(b.get()),
                            int(c.get()),
                            int(d.get()))

    if (answer is None):
      answerText = "There are either infinite solutions or no solutions"
    else:
      answerText = "\n".join(answer)
      answerText += ("\nIn other words, " +
                     a.get() + "(" + answer[0][3:] + ") + " +
                     b.get() + "(" + answer[1][3:] + ") + " +
                     c.get() + "(" + answer[2][3:] + ") = " +
                     d.get())

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=3, columnspan=7)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 7, 3)
