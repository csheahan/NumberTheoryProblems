'''
Problem:
  Given a set of more than two integers, find their greatest common divisor.

Constraints:
  integers - must be of length greater than 2
'''

import chapter3.section4.problem3.problem3

def problem(integers):
  if (len(integers) < 2):
    raise ValueError("There must a set of more the 2 integers")

  gcd = chapter3.section4.problem3.problem3.problem(integers[0], integers[1])

  for i in xrange(2, len(integers)):
    gcd = chapter3.section4.problem3.problem3.problem(gcd, integers[i])

  return gcd