'''
Problem:
  Given the coefficients of a linear diophantine equation in two variables,
  find all its solutions.

Constraints:
  a - integer
  b - integer
'''

from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section4.problem5 import problem5 as bezout

def solve(a, b, c):
  # d = gcd(a,b)
  d = gcd.solve(abs(a), abs(b))

  if (c % d != 0):
    return (None, d)

  # The bezout coefficients are m,n from the equation am*bn=gcd(a,b)
  bezout_coefficients = bezout.solve(a, b)
  knot_coefficients = (
    bezout_coefficients[0] * (c / d),
    bezout_coefficients[1] * (c / d)
  )

  x = str(knot_coefficients[0]) + " + " + str(b / d) + "n"
  y = str(knot_coefficients[1]) + " + " + str(a / d) + "n"

  return (x, y)