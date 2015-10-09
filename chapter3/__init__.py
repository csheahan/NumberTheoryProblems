import chapter3.section1
import chapter3.section3

def load_chapter_three(tree, frame):
  tree.insert("", "end", "ch3", text="Chapter 3")
  chapter3.section1.load_section_one(tree, frame)
  chapter3.section3.load_section_three(tree, frame)