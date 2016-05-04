'''
Problem:
  Use A. K. Head's algorithm for multiplication modulo n where n < w / 2 where
  w is the word size of the computer.

Constraints:
  prob - must match the regex "\d+\*\d+"
  mod - must be less than half of the word size of computer
'''

from chapter4.section1.problem2 import problem2 as platformTools
import math
import re

def solve(prob, mod):
  if (not re.match(r"\d+\*\d+", prob)):
    raise ValueError("The problem must be of the form `nums*nums`")

  word_size = platformTools.getWordSize()

  if (mod >= word_size / 2):
    raise ValueError(("mod must be less than word size. "
                      "mod: %d, word size: %d" % (mod, word_size)))

  nums = prob.split("*")
  nums = map(int, nums)

  x, y = nums

  T = int(math.floor(mod ** .5 + .5))
  t = int(T ** 2 - mod)

  a = int(x / T)
  b = x - a * T
  c = int(y / T)
  d = y - c * T

  z = (a * d + b * c) % mod

  e = int((a * c) / T)
  f = a * c - e * T

  v = (z + e * t) % mod

  g = int(v / T)
  h = v  - g * T

  j = ((f + g) * t) % mod
  k = (j + b * d) % mod

  return (h * T + k) % mod