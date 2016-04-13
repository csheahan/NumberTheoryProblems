'''
Problem:
  Find q and r given a and b of the modified divison algorithm: a = b*q+r, where
  -b/2 < r <= b/2

Constraints:
  a - must be a positive integer
  b - must be a positive integer
'''

def solve(a, b):
  if (a <= 0):
    raise ValueError("a must be a positive integer")
  elif (b <= 0):
    raise ValueError("b must be a positive integer")

  # Try low q
  q = int(a / b)
  r = a % b

  if (r <= b / 2):
    return (q, r)

  # Return high q
  q += 1
  r -= b

  return (q, r)
