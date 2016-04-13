'''
Problem:
  Find q and r given a and b of the divison algorithm: a = b*q+r

Constraints:
  a - must be an integer
  b - must be an integer
'''

def solve(a, b):
  if (isinstance(a, float)):
    raise ValueError("a must be an integer")
  elif (isinstance(b, float)):
    raise ValueError("b must be an integer")

  q = int(a / b)
  r = a - (b * q)
  return (q, r)