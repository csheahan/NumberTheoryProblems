def clear_frame(frame):
  for widget in frame.winfo_children():
    widget.destroy()

def clear_row(frame, rowNum):
  for widget in frame.winfo_children():
    if (int(widget.grid_info()["row"]) == rowNum):
      widget.destroy()
