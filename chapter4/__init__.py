from chapter4 import section1
from chapter4 import section2

def load_chapter(tree, frame):
  tree.insert("", "end", "ch4", text="Chapter 4")
  section1.load_section(tree, frame)
  section2.load_section(tree, frame)