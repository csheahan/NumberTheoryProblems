'''
Problem:
  Find the number of powerful numbers less than a positive integer n.

Constraints:
  n - must be a positive integer
'''

# Primality
import chapter3.section1.problem1.problem1
# Sieve
import chapter3.section1.problem2.problem2

def problem(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")

  # Get a list of primes < n to check the divisions
  # Use a sieve to find all primes less than n
  primes = chapter3.section1.problem2.problem2.problem(n)

  # Add n if n is prime
  if (not chapter3.section1.problem1.problem1.problem(n)):
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
