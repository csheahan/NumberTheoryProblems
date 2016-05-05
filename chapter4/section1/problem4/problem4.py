'''
Problem:
  Solve for c in the equation b^N mod m = c

Constraints:
  b - positive integer
  N - positive integer
  c - positive integer
'''

def solve(b, n, mod):
  if (b < 1):
    raise ValueError("b must be a positive integer")
  if (n < 1):
    raise ValueError("n must be a positive integer")
  if (mod < 1):
    raise ValueError("mod must be a positive integer")

  pow_table = [1]
  mod_table = [b]

  while (pow_table[-1] * 2 < n):
    pow_table.append(pow_table[-1] * 2)
    mod_table.append((mod_table[-1] ** 2) % mod)

  res = 1

  for i, power in reversed(list(enumerate(pow_table))):
    if (power <= n):
      n -= power
      res *= mod_table[i]
      res %= mod

  return res
