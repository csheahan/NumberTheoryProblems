'''
Problem:
  Given the coefficients of a linear diophantine equation in three variables,
  find all its solutions.

Constraints:
  a - integer
  b - integer
  c - integer
  d - integer
'''

from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section4.problem5 import problem5 as bezout

# ax+by+cz=d
def solve(a, b, c, d):
  p = gcd.solve(a, b)
  a_prime = a / p
  b_prime = b / p
  c_prime = c / p

  (u_knot, v_knot) = linear_diophantine(a_prime, b_prime, c)
  (z_knot, t_knot) = linear_diophantine(c, p, d)
  (x_knot, y_knot) = linear_diophantine(a_prime, b_prime, t_knot)

  x = "x = " + str(x_knot) + " + " + str(b_prime) + "k - " + str(u_knot) + "m"
  y = "y = " + str(y_knot) + " - " + str(a_prime) + "k - " + str(v_knot) + "m"
  z = "z = " + str(z_knot) + " + " + str(p) + "m"

  return (x, y, z)

def linear_diophantine(a, b, c):
  bezout_coefficients = bezout.solve(a, b)
  knot_coeffs = (
    bezout_coefficients[0] * (c),
    bezout_coefficients[1] * (c)
  )

  if (knot_coeffs[0] * a + knot_coeffs[1] * b != c):
    knot_coeffs = (knot_coeffs[1], knot_coeffs[0])

    if (knot_coeffs[0] * a + knot_coeffs[1] * b != c):
      raise ValueError("Something went wrong calculating the linear dio")

  return knot_coeffs

