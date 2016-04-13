'''
Problem:
  Given the coefficients of a linear diophantine equation in two variables, find
  all its positive solutions.

Constraints:
  a - integer
  b - integer
'''

from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section4.problem5 import problem5 as bezout

def solve(a, b, c):
  if (b < 0):
    return None

  # d = gcd(a,b)
  d = gcd.solve(abs(a), abs(b))

  if (c % d != 0):
    return None

  # returns m,n where am+by=gcd(a,b)
  bezout_coefficients = bezout.solve(a, b)

  b1 = float(-(bezout_coefficients[1] * c)) / abs(b)
  b2 = float((bezout_coefficients[0] * c)) / abs(a)

  return int(max(b1, b2)) - int(min(b1, b2))