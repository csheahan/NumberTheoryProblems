'''
Problem:
  Given a positive integer n, list the Farey series of order n.

Constraints:
  n - must be a positive integer
'''

import chapter3.section3.problem1

def problem(n):
  fractions = []

  fractions.append((0, 1))

  for h in xrange(1, n):
    for k in xrange(n, h, -1):
      if chapter3.section3.problem1.problem1.problem(h, k) == 1:
        fractions.append((h, k))

  fractions.append((1, 1))

  return fractions

