'''
Problem:
  Given the coefficients a and b, find all positive integers n for which the
  linear diophantine equation ax+by=n has no positive solutions

Constraints:
  a - positive integer
  b - positive integer
'''

from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section7.problem2 import problem2 as positiveNumberDioAnswers

def solve(a, b):
  if (gcd.solve(a, b) != 1):
    raise ValueError("a and b must be relatively prime")
  if (a < 1):
    raise ValueError("a must be positive")
  if (b < 1):
    raise ValueError("b must be positive")

  # Whenever n >= (a-1)(b-1), there is a nonnegative solution -> upper bound
  upper_bound = (a - 1) * (b - 1)

  n_arr = []

  for n in xrange(1, upper_bound):
    if (positiveNumberDioAnswers.solve(a, b, n) == 0):
      n_arr.append(n)

  return n_arr