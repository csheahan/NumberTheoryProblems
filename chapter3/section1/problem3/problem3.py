'''
Problem:
  Given a positive integer n, use Exercise 24 to find pi(n)

Constraints:
  n - must be a positive integer
'''

def solve(n):
  if (n < 1):
    raise ValueError(u"pi must be a positive integer")
  elif (n == 2 or n == 1):
    return 0
  elif (n == 3):
    return 1

  return pi(n)

def pi(n):
  global pi_array
  primesLessThan = sieve(n ** .5)
  r = len(primesLessThan)

  # answer = pi(root(n) - 1)
  answer = r - 1

  # answer = pi(root(n) - 1)  + n
  answer += n

  # Do inclusion exclusion
  includeExclude = -1
  for i in xrange(1, r + 1):
    part = 0

    if (i == 1):
      for prime in primesLessThan:
        part += (n / prime)
    else:
      pi_array = []
      subset(primesLessThan, i, 0, [0] * i, 0)

      for arr in pi_array:
        denom = 1

        for prime in arr:
          denom *= prime

        part += (n / denom)

    answer += includeExclude * part
    includeExclude *= -1

  return answer

def subset(arr, n, count, subarr, pos):
  global pi_array

  subarr[count] = arr[pos]
  count += 1

  if (count == n):
    pi_array.append(subarr)
    return subarr

  for i in xrange(pos + 1, len(arr)):
    subset(arr, n, count, list(subarr), i)

  if ((count == 1) and (pos < len(arr) - 1)):
    subset(arr, n, 0, [0] * n, pos + 1)

def sieve(n):
  if (n == 1):
    return []

  n = int(n)

  booleanSieve = [True for i in xrange(n)]

  booleanSieve[0] = False
  booleanSieve[1] = False

  for prime in xrange(2, n):
    if (booleanSieve[prime]):
      sieveNum = prime + prime

      while (sieveNum < n):
        booleanSieve[sieveNum] = False
        sieveNum += prime

  return [x for x in xrange(n) if booleanSieve[x]]
