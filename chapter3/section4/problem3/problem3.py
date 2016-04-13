'''
Problem:
  Given two positive integers, find their greatest common divisor using no
  divisions

Constraints:
  a - must be a positive integer
  b - must be a positive integer
'''

def solve(a, b):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")

  while b != 0:
    temp = b
    b = a % b
    a = temp

  return a
