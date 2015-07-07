'''
Problem:
  Given a rational number p/q, express p/q as an Egyption fraction.

Constraints:
  p - must be a positive integer and p < q
  q - must be a positive integer and q > p
'''

import fractions

###############################################################################
# problem - Give an Egyptian fraction representation for a fraction p/q
# 
# @param p - denomenator of the fraction
# @param q - numerator of the fraction
# 
# @return A list of Tuples representing a series of unit fractions
###
def problem(p, q):
  if (p <= 0):
    raise ValueError("p must be a positive integer")
  elif (q <= 0):
    raise ValueError("q must be a positive integer")
  elif (q < p):
    raise ValueError("q must be greater than p")

  answer = []

  current = fractions.Fraction(p, q)

  guessDenom = 1
  guess = fractions.Fraction(1, guessDenom)
  
  while (current != 0):\

    while (guess > current):
      guessDenom += 1
      guess = fractions.Fraction(1, guessDenom)

    current -= guess

    answer.append((1, guessDenom))

  return answer
