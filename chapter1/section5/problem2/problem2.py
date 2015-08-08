'''
Problem:
  Find q and r given a and b of the divison algorithm: a = b*q+r

Constraints:
  a - must be an integer
  b - must be an integer
'''

def problem(a, b):
  q = int(a / b)
  r = a - (b * q)
  return (q, r)