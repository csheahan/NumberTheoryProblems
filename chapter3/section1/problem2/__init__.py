from Tkinter import *
import ttk
import functools
import helpers
import chapter3.section1.problem2.problem2

def load_problem(tree, frame):
  tree.insert("ch3.1", "end", "ch3.1.2", text="Problem 2", tags=["ch3.1.2"])
  tree.tag_bind("ch3.1.2", '<1>',
    functools.partial(problem_two_view, frame))

def problem_two_view(frame, event):
  helpers.clear_frame(frame)

  problemText = "Use the sieve of Eratosthenes to find all primes not exceeding"
  problemText += " a positive integer n"
  promptText = "Enter a positive integer n:"

  helpers.generate_prompt_and_input(
    frame,
    problemText,
    promptText,
    problem_two_display_answer
  )

def problem_two_display_answer(frame, n):
  helpers.clear_row(frame, 2)

  try:
    answer = chapter3.section1.problem2.problem2.problem(int(n.get()))

    answerText = "The primes less than " + n.get() + " are: "

    for prime in answer:
      answerText += str(prime) + ", "

    answerText = answerText[:-2]

    answerLabel = Label(frame, text=answerText)

    answerLabel.grid(row=2, columnspan=3)
  except Exception as e:
    helpers.handle_error_with_message(e, frame, 3)