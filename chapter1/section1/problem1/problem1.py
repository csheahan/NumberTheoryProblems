# -*- coding: utf-8 -*-

'''
Probelem:
  Given a number α, find rational number p/q such that |α - p/q| ≤ 1/q^2

Constraints:
  α - must be an integer
  p - must be an integer
  q - must be an integer s.t. q != 0
'''

def problem(alpha):
  answers = []

  q = alpha
  p = q * alpha
  lhs = abs(alpha - float(p) / q)
  rhs = 1 / (float(q) * q)
  answers.append((p, q, lhs, rhs))

  return answers
