'''
Problem:
  Given a pair of positive integers, find Bezout coefficients for them.

Constraints:
  a - must be a positive integer
  b - must be a positive integer
'''

def solve(a, b):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")

  flipped = False

  if (a < b):
    flipped = True
    temp = a
    a = b
    b = temp

  si = [1, 0]
  nextSi = 0
  ti = [0, 1]
  nextTi = 0
  quotient = 0
  remainder = 0

  # Use extended Euclidean algorithm
  while (True):
    quotient = a / b
    remainder = a - quotient * b

    nextSi = si[0] - quotient * si[1]
    si[0] = si[1]
    si[1] = nextSi

    nextTi = ti[0] - quotient * ti[1]
    ti[0] = ti[1]
    ti[1] = nextTi

    if (remainder == 0):
      if (flipped):
        return (si[0], ti[0])

      return (ti[0], si[0])
    else:
      a = b
      b = remainder
