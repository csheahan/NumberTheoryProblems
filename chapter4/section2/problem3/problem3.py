'''
Problem:
  Given an integer a relatively prime to a positive integer m > 2, find the
  inverse of a modulo m.

Constraints:
  a - integer
  m - m is a positive integer > 2
'''

def solve(a, m):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (m < 3):
    raise ValueError("m must be a integer > 2")

  for i in xrange(1, m):
    if ((a * i) % m == 1):
      return i

  return None