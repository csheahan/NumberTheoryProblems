'''
Problem:
  Solve linear congruences using inverses.

Constraints:
  a - positive integer
  b - positive integer
  m - positive integer
'''

from chapter4.section2.problem3 import problem3 as inverse

def solve(a, b, m):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")
  if (m < 1):
    raise ValueError("m must be a positive integer")

  a_bar = inverse.solve(a, m)

  if (a_bar is None):
    raise ValueError("Ensure that (a, m) = 1")
  else:
    return (b * a_bar) % m