import chapter1.section1
import chapter1.section3
import chapter1.section4
import chapter1.section5

def load_chapter_one(tree, frame):
  tree.insert("", "end", "ch1", text="Chapter 1")
  chapter1.section1.load_section_one(tree, frame)
  chapter1.section3.load_section_three(tree, frame)
  chapter1.section4.load_section_four(tree, frame)
  chapter1.section5.load_section_five(tree, frame)
