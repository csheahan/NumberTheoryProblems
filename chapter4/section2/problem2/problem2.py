'''
Problem:
  Solve linear congruences using the method given in Exercise 4.

Constraints:
  a - positive integer
  b - positive integer
  p - prime
'''

import math
from chapter3.section1.problem1 import problem1 as isNotPrime
from chapter3.section4.problem1 import problem1 as gcd

def solve(a, b, p):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")
  if (isNotPrime.solve(p)):
    raise ValueError("p must be prime")
  if (gcd.solve(a, p) != 1):
    raise ValueError("(a, p) must be 1")

  i = a
  j = int(math.floor(p / i))
  a_x = p - j * i
  new_b = (-b * j) % p

  while(a_x > 1):
    i = a_x
    j = int(math.floor(p / i))
    a_x = p - j * i
    new_b = (-new_b * j) % p

  return new_b