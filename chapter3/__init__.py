import chapter3.section1 as section1
import chapter3.section3 as section3
import chapter3.section4 as section4
import chapter3.section5 as section5
import chapter3.section7 as section7

def load_chapter(tree, frame):
  tree.insert("", "end", "ch3", text="Chapter 3")
  section1.load_section(tree, frame)
  section3.load_section(tree, frame)
  section4.load_section(tree, frame)
  section5.load_section(tree, frame)
  section7.load_section(tree, frame)
