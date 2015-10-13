'''
Problem:
  Given two positive integers m and n and their lists of positive divisors,
  find (m, n).

Constraints:
  m - must be a positive integer
  n - must be a positive integer
'''

def problem(m, n):
  mDivisors = getDivisors(m)
  nDivisors = getDivisors(n)

  gcd = 0

  for i in mDivisors:
    if i in nDivisors and gcd < i:
      gcd = i

  return gcd

def getDivisors(n):
  if n == 1:
    return [1]

  divisors = []

  for i in xrange(1, n + 1):
    if n % i == 0:
      divisors.append(i)

  return divisors
