'''
Problem:
  Given a positive integer a, find all of it's positive divisors from it's prime
  factorization.

Constraints:
  a - must be a positive integer
'''

# Primality testing
from chapter3.section1.problem1 import problem1 as isNotPrime
import itertools

def solve(a):
  if (a < 1):
    raise ValueError("a must be a positive integer")

  prime_factor_list = getPrimeFactors(a)
  divisors = set()
  divisors.add(1)

  for i in range(0, len(prime_factor_list) + 1):
    for subset in itertools.combinations(prime_factor_list, i):
      answer = 1

      for num in subset:
        answer *= num

      divisors.add(answer)

  return sorted(divisors)

def getPrimeFactors(a):
  i = 2
  lst = []
  while (i <= a):
    # If is prime
    if (not isNotPrime.solve(i)):
      if (a % i == 0):
        a /= i
        lst.append(i)
        i = 1
    i += 1

  return lst