'''
Problem:
  Find the first n terms of the Fibonacci sequence

Constraints:
  n - must be a positive integer
'''

fibonacci_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def solve(n):
  if (n <= 0):
    raise ValueError("n must be a positive integer")

  global fibonacci_sequence

  if (n < len(fibonacci_sequence)):
    return fibonacci_sequence[:n]
  else:
    toCalc = len(fibonacci_sequence)

    while (toCalc < n):
      fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])
      toCalc += 1

    return fibonacci_sequence
