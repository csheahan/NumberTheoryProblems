'''
Problem:
  Find the Collatz sequence for a positive integer n

Constraints:
  n - must be a positive integer  
'''

import chapter1.section4.problem1.problem1

def problem(n):
  if (n <= 0):
    raise ValueError("n must be a positive integer")

  if (n == 1):
    return [1]

  answer = []

  while (n > 1):
    answer.append(n)

    if (n % 2 == 0):
      n = n / 2
    else:
        n = (3 * n + 1) / 2

  answer.append(n)

  return answer