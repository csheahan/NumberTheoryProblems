from chapter1 import section1 as section1
from chapter1 import section3 as section3
from chapter1 import section4 as section4
from chapter1 import section5 as section5

def load_chapter(tree, frame):
  tree.insert("", "end", "ch1", text="Chapter 1")
  section1.load_section(tree, frame)
  section3.load_section(tree, frame)
  section4.load_section(tree, frame)
  section5.load_section(tree, frame)
