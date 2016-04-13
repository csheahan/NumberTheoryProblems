'''
Problem:
  Given a positive integer n, list the Farey series of order n.

Constraints:
  n - must be a positive integer
'''

from chapter3.section3.problem1 import problem1 as gcd

def solve(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")

  fractions = []

  fractions.append((0, 1))

  for h in xrange(1, n):
    for k in xrange(n, h, -1):
      if gcd.solve(h, k) == 1:
        fractions.append((h, k))

  fractions.append((1, 1))

  return fractions

