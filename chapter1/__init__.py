import chapter1.section1

def load_chapter_one(tree, frame):
  tree.insert("", "end", "ch1", text="Chapter 1")
  chapter1.section1.load_section_one(tree, frame)

