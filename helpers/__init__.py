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

def generate_prompt_and_input(tree,
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
      command=functools.partial(problemFunction, tree, frame, prompt))
    submitButton.grid(row=1, column=2)
