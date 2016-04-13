'''
Problem:
  Find the greatest common divisor of two positive integers from their prime
  factorizations.

Constraints:
  a - must be a positive integer
  b - must be a positive integer
'''

from chapter3.section5.problem1 import problem1 as findDivisors

def solve(a,b):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")

  a_prime_factor_list = findDivisors.getPrimeFactors(a)
  b_prime_factor_list = findDivisors.getPrimeFactors(b)

  gcd = 1

  for i in xrange(len(a_prime_factor_list) - 1, -1, -1):
    item = a_prime_factor_list[i]
    if item in b_prime_factor_list:
      gcd *= item
      a_prime_factor_list.pop(i)
      b_prime_factor_list.pop(b_prime_factor_list.index(item))

  return gcd