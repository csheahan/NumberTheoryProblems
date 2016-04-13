'''
Problem:
  Decide whether an integer is divisible by a given integer.

Constraints:
  x - must be an integer
  y - must be an integer
'''

def solve(x, y):
  if (isinstance(x, float)):
    raise ValueError("x must be an integer")
  elif (isinstance(y, float)):
    raise ValueError("y must be an integer")

  if (x % y == 0):
    return True

  return False