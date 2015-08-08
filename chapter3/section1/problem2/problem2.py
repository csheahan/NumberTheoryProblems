'''
Problem:
  Given a positive integer n, use the sieve of Eratosthenes to find all primes
  not exceeding it, or in other words, less than it.

Constraints:
  n - must be a positive integer
'''

def problem(n):
    if (n < 1):
      raise ValueError("n must be a positive integer")
    elif (n == 1):
      return []

    booleanSieve = [True for i in range(n)]

    booleanSieve[0] = False
    booleanSieve[1] = False

    for prime in xrange(2, n):
      if (booleanSieve[prime]):
        sieveNum = prime + prime

        while (sieveNum < n):
          booleanSieve[sieveNum] = False
          sieveNum += prime

    return [x for x in xrange(n) if booleanSieve[x]]