import chapter4.section1 as section1

def load_chapter(tree, frame):
  tree.insert("", "end", "ch4", text="Chapter 4")
  section1.load_section(tree, frame)