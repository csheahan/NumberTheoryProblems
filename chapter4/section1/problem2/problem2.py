'''
Problem:
  Perform modular addition and subtraction when the modulus is less than half of
  the word size of the computer.

Constraints:
  prob - must match the regex "\d+[+-]\d+"
  mod - must be less than half of the word size of computer
'''

import platform
import re

def solve(prob, mod):
  if (not re.match(r"\d+[+-]\d+", prob)):
    raise ValueError("The problem must be of the form `nums[+-]nums`")

  word_size = getWordSize()

  if (mod >= word_size / 2):
    raise ValueError(("mod must be less than word size. "
                      "mod: %d, word size: %d" % (mod, word_size)))

  if ("+" in prob):
    # addition
    nums = prob.split("+")

    # strings -> ints
    nums = map(int, nums)

    return ((nums[0] % mod) + (nums[1] % mod)) % mod
  elif ("-" in prob):
    # subtraction
    nums = prob.split("-")

    # strings -> ints
    nums = map(int, nums)

    return ((nums[0] % mod) - (nums[1] % mod)) % mod

  raise ValueError("Something is wrong with your problem. No + or - found.")

def getWordSize():
  arch = platform.architecture()
  word_size = arch[0][:arch[0].index("bit")]

  return int(word_size)
