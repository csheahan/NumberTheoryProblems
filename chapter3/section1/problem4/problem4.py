'''
Problem:
  Given positive integers a and b not divisible by the same prime, find the 
  smallest prime number in the arithmetic progression a * n + b, where n is a 
  positive integer.

Constraints:
  a - must be a positive integer
  b - must be a positive integer
  a & b - cannot be divisible any similar primes
'''

def problem(a, b):
  if (a < 1):
    raise ValueError("a must be a positive integer")
  elif (b < 1):
    raise ValueError("b must be a positive integer")

  aPrimeDivisors = getPrimeDivisors(a)
  bPrimeDivisors = getPrimeDivisors(b)

  similarPrimes = []

  for prime in aPrimeDivisors:
    if prime in bPrimeDivisors:
      similarPrimes.append(prime)

  if len(similarPrimes) > 0:
    commonFactors = ""
    for prime in similarPrimes:
      commonFactors += str(prime) + ","
    commonFactors = commonFactors[:-1]
    raise ValueError("a and b have common prime factors. Common prime factors: " + commonFactors)

  answer = a * 1 + b

  while (not isPrime(answer)):
    answer += a

  return answer

def getPrimeDivisors(n):
  divisors = []

  if n % 2 == 0:
    divisors.append(2)

  for i in xrange(3, int(n ** .5) + 1, 2):
    if n % i == 0:
      if isPrime(i):
        divisors.append(i)

  return divisors

def isPrime(n):
  if n <= 1:
    return False
  elif n == 2:
    return True
  elif n % 2 == 0:
    return False

  for i in xrange(3, int(n ** .5) + 1, 2):
    if n % i == 0:
      return False

  return True

print problem(9, 8)