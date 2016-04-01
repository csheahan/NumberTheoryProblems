'''
Problem:
  Find the prime factorization of n!, where n is a positive integer.

Constraints:
  n - must be a positive integer
'''

# Primality
import chapter3.section1.problem1.problem1
# Sieve
import chapter3.section1.problem2.problem2
import math

def problem(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")

  prime_power_factorization = []

  # Use a sieve to find all primes less than n
  primes = chapter3.section1.problem2.problem2.problem(n)

  # Add n if n is prime
  if (not chapter3.section1.problem1.problem1.problem(n)):
    primes.append(n)

  # Use the observation of 3.5.4 to calculate the exponent
  for prime in primes:
    power = 1
    num = 0

    while (prime ** power <= n):
      num += int(math.floor(n / (prime ** power)))
      power += 1

    prime_power_factorization.append((prime, num))

  return sorted(prime_power_factorization, key=lambda tup: tup[0], reverse=True)