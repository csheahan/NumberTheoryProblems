Chapter 1 Section 1 Problem 3
=============================

- [Thoughts][thoughts]
- [Approach][approach]

### Thoughts ###

This is an easy problem that whose performance can be improved greatly through
simple techniques such as memoization.

### Approach ###

The approach to this problem is done in 2 parts. First, we memoize the list of
known Ulam numbers to avoid the cost of recomputation. Therefore, if an n less
than the size of the list of known Ulam numbers is requested, we simply give
those numbers without computation, saving time from multiple requests. The 
algorithm we use to determine if a given number is an Ulam number given a list
of all previous Ulam numbers is as follows:

```
set low to point to the first element in our Ulam list
set high to the last element in our Ulam list

while low is pointing to an element lower than high:
  if low + high > num:
    set high the next lower element
  else if low + high < num:
    set low to the next highest element
  else:
    we found a pair where low + high = goal, so do the following
    set low to the next highest element
    set high the next lower element
    if this is not the first match, return false, as this is not an Ulam number

check the number of matches. If it is one, return true, else false
```

It is not terribly difficult to prove that the above algorithm finds all pairs
in a list that equal the trial Ulam number. The approach would be to use
a proof by contradiction, and show that if a pair (i, j) exists in the list such
that i + j = test_number that it must be checked (after assuming that it
wasn't). I may or may not write this proof up, it all depends on if I both
write it and get it in a state where I like the way I approached the proof and
worded it.

[thoughts]: #thoughts
[approach]: #approach
