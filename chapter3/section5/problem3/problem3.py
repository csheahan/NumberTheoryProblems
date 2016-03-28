'''
Problem:
  Find the least common multiple of two positive integers from their prime
  factorizations.

Constraints:
  a - must be a positive integer
  b - must be a positive integer
'''

import chapter3.section5.problem2.problem2

def problem(a,b):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")

  gcd_via_prime_factors = chapter3.section5.problem2.problem2.problem(a, b)

  # [a, b] = ab/(a, b) where (a, b) is the gcd and [a, b] is the lcm
  lcm = (a * b) / gcd_via_prime_factors

  return lcm