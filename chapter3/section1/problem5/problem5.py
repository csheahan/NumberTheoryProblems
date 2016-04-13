'''
Problem:
  Given a positive integer n, find the lucky numbers less than n

Constraints:
  n - must be a positive integer
'''

def solve(n):
  if (n < 1):
    raise ValueError("a must be a positive integer")

  return sieve(n)

def sieve(n):
  if (n == 1):
    return []

  n = int(n)

  booleanSieve = [True for i in xrange(n)]

  booleanSieve[0] = False

  # Cross out all even numbers
  for i in xrange(2, n, 2):
    booleanSieve[i] = False

  currentLuckyNum = 2
  while(currentLuckyNum < n):
    if (booleanSieve[currentLuckyNum]):
      count = 0

      for i in xrange(0, n):
        if booleanSieve[i]:
          count += 1

          if count == currentLuckyNum:
            booleanSieve[i] = False
            count = 0

    currentLuckyNum += 1

  return [x for x in xrange(n) if booleanSieve[x]]
