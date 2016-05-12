'''
Problem:
  Solve linear congruences using the method given in the text.

Constraints:
  a - positive integer
  b - positive integer
  m - positive integer
'''

import helpers
from chapter3.section4.problem1 import problem1 as gcd
from chapter3.section4.problem5 import problem5 as bezout

def solve(a, b, m):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  if (b < 1):
    raise ValueError("b must be a positive integer")
  if (m < 1):
    raise ValueError("m must be a positive integer")

  d = gcd.solve(a, m)

  if (b % d != 0):
    raise ValueError("(a, m) = %d must divide b" % d)

  bezout_co = helpers.bezout(a, m, bezout.solve(a, m))
  naught_co = (bezout_co[0] * (b / d), bezout_co[1] * (b / d))

  if (d > 1):
    mult = m / d

    sols = []

    for i in xrange(0, d):
      sols.append((naught_co[0] + mult * i) % m)

    return sols
  else:
    return [naught_co[0] % m]