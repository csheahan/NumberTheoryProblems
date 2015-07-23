'''
Problem:
  Find q and r given a and b of the divison algorithm: a = b*q+r

Constraints:
  a - must be an integer
  b - must be an integer
'''

###############################################################################
# problem - Calculate the quotient and remainder of the division algorithm
#           given an a and b parameter where a=bq+r
#           
# @param a - a parameter to use
# @param b - b parameter to use
# 
# @return A tuple of the form (q, r)
###
def problem(a, b):
  q = int(a / b)
  r = a - (b * q)
  return (q, r)