'''
Problem:
  Given a set of more than two integers, find their greatest common divisor.

Constraints:
  integers - must be of length greater than 2
'''

from chapter3.section4.problem3 import problem3 as gcd

def solve(integers):
  if (len(integers) < 2):
    raise ValueError("There must a set of more the 2 integers")

  curr_gcd = gcd.solve(integers[0], integers[1])

  for i in xrange(2, len(integers)):
    curr_gcd = gcd.solve(curr_gcd, integers[i])

  return curr_gcd