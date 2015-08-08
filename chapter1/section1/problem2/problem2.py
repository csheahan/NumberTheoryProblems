# -*- coding: utf-8 -*-

import math

'''
Probelem:
  Given a number α, find its spectrum sequence

Constraints:
  α - must be a real number
'''

def problem(alpha):
  answer = []

  for i in xrange(1, 11):
    element = alpha * i
    element = int(math.floor(element))
    answer.append(element)

  return answer
