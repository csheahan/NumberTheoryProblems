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

import helpers
from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section4.problem5 import problem5 as bezout

# ax+by+cz=d
def solve(a, b, c, d):
  p = gcd.solve(a, b)
  a_prime = a / p
  b_prime = b / p
  c_prime = c / p

  (u_naught, v_naught) = linear_diophantine(a_prime, b_prime, c)
  (z_naught, t_naught) = linear_diophantine(c, p, d)
  (x_naught, y_naught) = linear_diophantine(a_prime, b_prime, t_naught)

  x = "x = " + str(x_naught) +" + "+ str(b_prime) +"k - "+ str(u_naught) +"m"
  y = "y = " + str(y_naught) +" - "+ str(a_prime) +"k - "+ str(v_naught) +"m"
  z = "z = " + str(z_naught) +" + "+ str(p) +"m"

  return (x, y, z)

def linear_diophantine(a, b, c):
  bezout_coefficients = helpers.bezout(a, b, bezout.solve(a, b))
  naught_coeffs = (bezout_coefficients[0] * (c), bezout_coefficients[1] * (c))

  return naught_coeffs

