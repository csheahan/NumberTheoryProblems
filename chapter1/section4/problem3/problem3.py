'''
Problem:
  Find the Zeckendorf representation of an integer

Constraints:
  n - must be a positive integer
'''

from chapter1.section4.problem1 import problem1 as fib_solver

def solve(n):
  if (n <= 0):
    raise ValueError("n must be a positive integer")

  if (n == 1):
    return [1]

  fibonacci_sequence = fib_solver.fibonacci_sequence

  if (fibonacci_sequence[-1] <= n):
    while (fibonacci_sequence[-1] <= n):
      fibonacci_sequence.append(fibonacci_sequence[-2] + fibonacci_sequence[-1])

  index = 0

  while (fibonacci_sequence[index] <= n):
    index += 1

  index -= 1

  if (fibonacci_sequence[index] == n):
    return [fibonacci_sequence[index]]

  answer = calc_zeckendorf(index, n)

  return answer

def calc_zeckendorf(idx, target):
  fibonacci_sequence = fib_solver.fibonacci_sequence

  if (idx < 0):
    return []
  elif (fibonacci_sequence[idx] > target):
    return calc_zeckendorf(idx - 1, target)

  if (fibonacci_sequence[idx] == target):
    return [fibonacci_sequence[idx]]
  elif (fibonacci_sequence[idx] < target):
    tempIdx = idx

    while (tempIdx >=  0):
      check = calc_zeckendorf(tempIdx - 2, target - fibonacci_sequence[tempIdx])

      if (len(check) > 0):
        check.append(fibonacci_sequence[tempIdx])
        return check

      tempIdx -= 1

    return calc_zeckendorf(idx - 1, target)
  else:
    return []
