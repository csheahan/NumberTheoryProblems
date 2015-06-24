# -*- coding: utf-8 -*-

'''
Probelem:
  Given a number α, find rational number p/q such that |α - p/q| ≤ 1/q^2

Constraints:
  α - must be an integer
  p - must be an integer
  q - must be an integer s.t. q != 0
'''

###############################################################################
# problem - finds a rational number p/q such that |α - p / q| ≤ 1/q^2
#
# @param int alpha - α parameter to use
#
# @return a list of tuples (p, q, lhs, rhs) that follows the inequality where
#         p = p
#         q = q
#         lhs = |α - p/q|
#         rhs = 1/q^2
###
def problem(alpha):
  answers = []

  q = alpha
  p = q * alpha
  lhs = abs(alpha - float(p) / q)
  rhs = 1 / (float(q) * q)
  answers.append((p, q, lhs, rhs))

  return answers
