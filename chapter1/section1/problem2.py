# -*- coding: utf-8 -*-

import math

'''
Probelem:
  Given a number α, find its spectrum sequence

Constraints:
  α - must be a real number

Observation:
  None needed, this is a simple sequence generation
'''

###############################################################################
# problem - find a spectrum sequence of a given number
# 
# @param real alpha - α parameter to use
# 
# @return A list of integers in the spectrum sequence of α
###
def problem(alpha):
  answer = []

  for i in xrange(1, 11):
    element = alpha * i
    element = int(math.floor(element))
    answer.append(element)

  return answer
