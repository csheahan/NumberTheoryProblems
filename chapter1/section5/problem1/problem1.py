'''
Problem:
  Decide whether an integer is divisible by a given integer.

Constraints:
  x - must be an integer
  y - must be an integer
'''

###############################################################################
# problem - Decide if an integer x is divisble by an integer y
#           
# @param x - x parameter to use
# @param y - y parameter to use
# 
# @return True if y divides x, false otherwise
###
def problem(x, y):
  if (x % y == 0):
    return True

  return False