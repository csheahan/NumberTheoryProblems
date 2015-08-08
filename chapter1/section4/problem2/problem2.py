'''
Problem:
  Find the first n Lucas Numbers

Constraints:
  n - must be a positive integer
'''

lucas_numbers = [1, 3, 4, 7, 11, 18, 29, 47, 76, 123]

def problem(n):
  if (n <= 0):
    raise ValueError("n must be a positive integer")

  global lucas_numbers

  if (n < len(lucas_numbers)):
    return lucas_numbers[:n]
  else:
    toCalc = len(lucas_numbers)

    while (toCalc < n):
      lucas_numbers.append(lucas_numbers[-2] + lucas_numbers[-1])
      toCalc += 1

    return lucas_numbers
