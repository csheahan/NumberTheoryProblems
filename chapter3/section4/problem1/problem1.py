'''
Problem:
  Given two integers, use the Euclidean algorithm to find their greatest common
  divisor.

Constraints:
  None
'''

def problem(a, b):
  # Ensure a is the higher number
  if a < b:
    temp = a
    a = b
    b = temp

  # a = b * q + r
  while (True):
    # A base case
    if (a <= 1):
      return 1

    q = 1
    
    while (b * q < a):
      q += 1

    if (b * q == a):
      return b
    else:
      q -= 1
      r = a - b * q
      a = b
      b = r
