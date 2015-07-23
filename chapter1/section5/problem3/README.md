Chapter 1 Section 5 Problem 3
=============================

- [Thoughts][thoughts]

### Thoughts ###

Another fairly simple problem once you learn the trick. It can be intuitively
explained like this: first, get b * q such that a - b * q is positive. According
to the definition of the division algorithm, r < b. Thus, r is some positive
number such that a = b * q + r. However, we want -b/2 < r <= b/2. Thus, if r > 
b/2, then we know that r - b > -b/2. Therefore, we simply move that b to b * q,
and we satisfy the condition for r.

[thoughts]: #thoughts
