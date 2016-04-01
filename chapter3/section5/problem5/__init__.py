from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section5.problem5.problem5

def load_problem(tree, frame):
  tree.insert("ch3.5", "end", "ch3.5.5", text="Problem 5", tags=["ch3.5.5"])
  tree.tag_bind("ch3.5.5", '<1>',
    functools.partial(problem_five_view, frame))

def problem_five_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Find the prime factorization of n!, where n is a positive "
  problemText += "integer."
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_five_display_answer
  )

def problem_five_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section5.problem5.problem5.problem(int(n.get()))

    answerText = "The prime factorization of n! is "

    for tup in answer:
      answerText += str(tup[0]) + "^" + str(tup[1]) + " + "

    answerText =  answerText[:-3]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)
