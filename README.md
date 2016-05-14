Number Theory Problems
======================

- [Problem Index][index]
- [Documentation][documentation]
- [What this project is][what]

### Index ###

- Chapter 1: The Integers
  - Section 1: Numbers and Sequences
    - [Problem 1][1.1.1] - Given a number a, find 2 numbers p,q such that the
                           following equation is satisfied: `|a - p/q| <= 1/q^2`
    - [Problem 2][1.1.2] - Find the spectrum sequence of a number
    - [Problem 3][1.1.3] - Find the first n Ulam numbers
  - Section 3: Mathematical Induction
    - [Problem 1][1.3.1] - List the moves in the Tower of Hanoi puzzle
    - [Problem 2][1.3.2] - Cover a chessboard missing 1 square with L-shaped
                           pieces
    - [Problem 3][1.3.3] - Given a fraction p\q, express p\q as an Egyptian
                           fraction
  - Section 4: The Fibonacci Numbers
    - [Problem 1][1.4.1] - Find the first n terms of the Fibonacci sequence
    - [Problem 2][1.4.2] - Find the first n Lucas numbers
    - [Problem 3][1.4.3] - Find the Zeckendorf representation of an integer
  - Section 5: Divisibility
    - [Problem 1][1.5.1] - Decide if an integer x is divisible by an integer y
    - [Problem 2][1.5.2] - Find q,r given a,b of the formula `a = b * q + r`
    - [Problem 3][1.5.3] - Find q,r given a,b of the formula `a = b * q + r`,
                           where `-b/2 < r <= b/2`
    - [Problem 4][1.5.4] - Compute the Collatz sequence for a positive integer
- Chapter 3: Primes and Greatest Common Divisors
  - Section 1: Prime Numbers
    - [Problem 1][3.1.1] - Determine if a number is prime via trial division
    - [Problem 2][3.1.2] - Use the sieve of Eratosthenes to find all primes not
                           exceeding a positive integer
    - [Problem 3][3.1.3] - Calculate the number of primes not exceeding an
                           integer using a recursive sequence
    - [Problem 4][3.1.4] - Given a,b find the smalles prime `a * n + b` where
                           `a != b`
    - [Problem 5][3.1.5] - Find the lucky numbers less than a positive integer
  - Section 3: Greatest Common Divisors
    - [Problem 1][3.3.1] - Calculate the GCD of 2 integers
    - [Problem 2][3.3.2] - List the Farey series of order n
  - Section 4: The Euclidean Algorithm
    - [Problem 1][3.4.1] - Calculate the GCD of 2 integers via the Euclidean
                           algorithm
    - [Problem 2][3.4.2] - Calculate the GCD of 2 integers via the
                           least-remainder algorithm
    - [Problem 3][3.4.3] - Calculate the GCD of 2 integers without using
                           division
    - [Problem 4][3.4.4] - Calculate the GCD of a list of integers
    - [Problem 5][3.4.5] - Calculate the Bezout coefficients for 2 positive
                           integers
    - [Problem 6 (Not Implemented)][3.4.6]
    - [Problem 7 (Not Implemented)][3.4.7]
  - Section 5: The Fundamental Theorem of Arithmetic
    - [Problem 1][3.5.1] - Find all divisors of a number via it's prime
                           factorization
    - [Problem 2][3.5.2] - Find the GCD of 2 numbers via their prime
                           factorization
    - [Problem 3][3.5.3] - Find the LCM of 2 numbers via their prime
                           factorization
    - [Problem 4][3.5.4] - Find the number of zeros at the end of n!
    - [Problem 5][3.5.5] - Find the prime factorization of n!
    - [Problem 6][3.5.6] - Find the number of powerful numbers less than a
                           positive integer
  - Section 7: Linear Diophantine Equations
    - [Problem 1][3.7.1] - Find all the solutions of a diophantine equation,
                           given a, b, and c where `ax+by=c`
    - [Problem 2][3.7.2] - Find all the positive solutions of a diophantine
                           equation, given a, b, and c where `ax+by=c`
    - [Problem 3][3.7.3] - Find all the solutions of a diophantine equation,
                           given a, b, c, and d where `ax+by+cz=d`
    - [Problem 4][3.7.4] - Given a, b, find all positive n s.t. the linear
                           diophantine equation `ax+by=n` has no positive
                           solutions
- Chapter 4: Congruences
  - Section 1: Introduction to Congruences
    - [Problem 1][4.1.1] - Find r for the equation `a=bm+r,
                           0 <= r < m` given a and m
    - [Problem 2][4.1.2] - Find c for the equation `(a[+-]b) mod m = c, m <
                           word size / 2`
    - [Problem 3][4.1.3] - Find c for the equation `(a*b) mod m = c, m <
                           word size / 2` using Head's algorithm
    - [Problem 4][4.1.4] - Find c for the equation `b^N mod m = c` using modular
                           exponentiation
  - Section 2: Linear Congruences
    - [Problem 1][4.2.1] - Solve linear congruences using the technique in the
                           text
    - [Problem 2][4.2.2] - Solve for x in the equation `ax ≡ b mod p` given a,
                           b, and p using an iterative method
    - [Problem 3][4.2.3] - Find an inverse for a positive integer given a modulo

### Documentation ###

If you wish to contribute, be sure to check out the [docs][docs]

### What it is ###

This is simply a side project to practice 3 things:
- GUI programming: I am interested in being able to make nice, intuitive, and
easy designs to act as front ends to my projects. I'm hoping this project can
bring me one step closer, even if I don't use the tkinter framework again.
- Python programming: Python is a language I've been meaning to play with for a
while. I believe that it has the potential to be that language that I use for
short one-off scripts and quick mock-ups of ideas.
- Number Theory: I took a number theory class this past semester and had a blast
in it. This project is intended to both enhance and reinforce my understanding
of the subject in an environment I enjoy.

[index]: #index
[documentation]: #documentation
[what]: #what-it-is
[1.1.1]: chapter1/section1/problem1
[1.1.2]: chapter1/section1/problem2
[1.1.3]: chapter1/section1/problem3
[1.3.1]: chapter1/section3/problem1
[1.3.2]: chapter1/section3/problem2
[1.3.3]: chapter1/section3/problem3
[1.4.1]: chapter1/section4/problem1
[1.4.2]: chapter1/section4/problem2
[1.4.3]: chapter1/section4/problem3
[1.5.1]: chapter1/section5/problem1
[1.5.2]: chapter1/section5/problem2
[1.5.3]: chapter1/section5/problem3
[1.5.4]: chapter1/section5/problem4
[3.1.1]: chapter3/section1/problem1
[3.1.2]: chapter3/section1/problem2
[3.1.3]: chapter3/section1/problem3
[3.1.4]: chapter3/section1/problem4
[3.1.5]: chapter3/section1/problem5
[3.3.1]: chapter3/section3/problem1
[3.3.2]: chapter3/section3/problem2
[3.4.1]: chapter3/section4/problem1
[3.4.2]: chapter3/section4/problem2
[3.4.3]: chapter3/section4/problem3
[3.4.4]: chapter3/section4/problem4
[3.4.5]: chapter3/section4/problem5
[3.4.6]: chapter3/section4/problem6
[3.4.7]: chapter3/section4/problem7
[3.5.1]: chapter3/section5/problem1
[3.5.2]: chapter3/section5/problem2
[3.5.3]: chapter3/section5/problem3
[3.5.4]: chapter3/section5/problem4
[3.5.5]: chapter3/section5/problem5
[3.5.6]: chapter3/section5/problem6
[3.7.1]: chapter3/section7/problem1
[3.7.2]: chapter3/section7/problem2
[3.7.3]: chapter3/section7/problem3
[3.7.4]: chapter3/section7/problem4
[4.1.1]: chapter4/section1/problem1
[4.1.2]: chapter4/section1/problem2
[4.1.3]: chapter4/section1/problem3
[4.1.4]: chapter4/section1/problem4
[4.2.1]: chapter4/section2/problem1
[4.2.2]: chapter4/section2/problem2
[4.2.3]: chapter4/section2/problem3
[docs]: Docs
