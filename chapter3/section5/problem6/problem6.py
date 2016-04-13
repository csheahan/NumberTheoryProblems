'''
Problem:
  Find the number of powerful numbers less than a positive integer n.

Constraints:
  n - must be a positive integer
'''

# Primality
from chapter3.section1.problem1 import problem1 as isNotPrime
# Sieve
from chapter3.section1.problem2 import problem2 as primesLessThanN

def solve(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")

  # Get a list of primes < n to check the divisions
  # Use a sieve to find all primes less than n
  primes = primesLessThanN.solve(n)

  # Add n if n is prime
  if (not isNotPrime.solve(n)):
    primes.append(n)

  powerful_numbers = [1]

  for i in xrange(2, n):
    powerful = True

    for prime in xrange(2, i + 1):
      if (prime in primes):
        if (i % prime == 0):
          if (i % (prime ** 2) != 0):
            powerful = False
            break

    if (powerful):
      powerful_numbers.append(i)

  return powerful_numbers
