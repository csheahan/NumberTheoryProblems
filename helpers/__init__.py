from Tkinter import *
import ttk
import functools

def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()

def clear_row(frame, rowNum):
  for widget in frame.winfo_children():
    if (int(widget.grid_info()["row"]) == rowNum):
      widget.destroy()

def generate_prompt_and_input(
  frame,
  problemText,
  promptText,
  problemFunction):
    prompt = Label(frame, text=problemText)
    prompt.grid(row=0, columnspan=3)

    entryLabel = Label(frame, text=promptText)
    entryLabel.grid(row=1, column=0)

    prompt = Entry(frame)
    prompt.grid(row=1, column=1)

    submitButton = Button(frame,
      text="submit",
      command=functools.partial(problemFunction, frame, prompt))
    submitButton.grid(row=1, column=2)

def generate_two_prompt_and_input(
  frame,
  problemText,
  promptOneText,
  promptTwoText,
  problemFunction):
    prompt = Label(frame, text=problemText)
    prompt.grid(row=0, columnspan=5)

    entryLabelOne = Label(frame, text=promptOneText)
    entryLabelOne.grid(row=1, column=0)

    promptOne = Entry(frame)
    promptOne.grid(row=1, column=1)

    entryLabelTwo = Label(frame, text=promptTwoText)
    entryLabelTwo.grid(row=1, column=2)

    promptTwo = Entry(frame)
    promptTwo.grid(row=1, column=3)

    submitButton = Button(frame,
      text="submit",
      command=functools.partial(
        problemFunction,
        frame,
        promptOne,
        promptTwo
      )
    )
    submitButton.grid(row=1, column=4)

def handle_error_with_message(err, frame, colspan):
  clear_row(frame, 2)

  errorText = u"An error has occurred. Type:"
  errorText += unicode(type(err))
  errorText += u". Message: "
  errorText += unicode(str(err))

  errorLabel = Label(frame, text=errorText)
  errorLabel.grid(row=2, columnspan=colspan)