'''
Problem:
  Given two integers, find their greatest common divisor using the modified
  Euclidean algorithm given in the preamble to Exercise 14.

Constraints:
  None
'''

def problem(a, b):
  # Ensure a is the higher number
  if a < b:
    temp = a
    a = b
    b = temp

  # a = b * q + e * r, r >= 0 and e = +- 1
  while (True):
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

      if (r > b / 2):
        q += 1
        r = b * q - a

      a = b
      b = r
