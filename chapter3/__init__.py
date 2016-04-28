from chapter3 import section1
from chapter3 import section3
from chapter3 import section4
from chapter3 import section5
from chapter3 import section7

def load_chapter(tree, frame):
  tree.insert("", "end", "ch3", text="Chapter 3")
  section1.load_section(tree, frame)
  section3.load_section(tree, frame)
  section4.load_section(tree, frame)
  section5.load_section(tree, frame)
  section7.load_section(tree, frame)
