import chapter3.section1

def load_chapter_three(tree, frame):
  tree.insert("", "end", "ch3", text="Chapter 3")
  chapter3.section1.load_section_one(tree, frame)