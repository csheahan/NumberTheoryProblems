'''
Problem:
  Find the number of zeros at the end of the decimal expansion of n!, where n
  is a positive integer.

Constraints:
  n - must be a positive integer
'''

def problem(n):
  if (n < 1):
    raise ValueError("n must be a positive integer")

  n_factorial = factorial(n)

  zeroes = 0
  zero_check = 10

  while(n_factorial % zero_check == 0):
    zeroes += 1
    zero_check *= 10

  return zeroes

def factorial(n):
  num = 1

  for i in xrange(1, n + 1):
    num *= i

  return num