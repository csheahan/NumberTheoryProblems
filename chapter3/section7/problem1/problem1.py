'''
Problem:
  Given the coefficients of a linear diophantine equation in two variables,
  find all its solutions.

Constraints:
  a - integer
  b - integer
'''

import chapter3.section4.problem1.problem1
import chapter3.section4.problem5.problem5

def problem(a, b, c):
  # d = gcd(a,b)
  d = chapter3.section4.problem1.problem1.problem(a, b)

  if (c % d != 0):
    return (None, d)

  # The bezout coefficients are m,n from the equation am*bn=gcd(a,b)
  bezout_coefficients = chapter3.section4.problem5.problem5.problem(a, b)
  knot_coefficients = (
    bezout_coefficients[0] * (c / d),
    bezout_coefficients[1] * (c / d)
  )

  x = str(knot_coefficients[0]) + " + " + str(b / d) + "n"
  y = str(knot_coefficients[1]) + " + " + str(a / d) + "n"

  return (x, y)