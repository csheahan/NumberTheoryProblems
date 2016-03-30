Chapter 3 Section 5 Problem 3
=============================

- [Thoughts][thoughts]
  - [Proof][proofs]
- [Old Thoughts][old_thoughts]

### Thoughts ###

As mentioned before, this is a problem that can be brute forced, but also has a
cool, clever solution. This approach makes use of the "intuition" mentioned in
the old thoughts, of which I will prove works. Also note I am doing this proof
without outside help, thus there is probably and more likely most definitely
a better and more formal way to do this.

#### Proof ####

```
We first start this proof with an observation. Note that 10^x = 2^(x-1) *
5^(x-1). This can be proven for any power of 10 via a simple induction proof.
This observation is important because of our objective: find the number of 0's
at the end the decimal expansion. Each 0 corresponds to a power of 10.

Now, we find out the connection to 5's. It is obvious via the above observation
that the 0's at the end are dependent on the number of 2's and 5's in the prime
factorization of n!. However, we can prove that the number of 2's is irrelevant
and that the bottleneck is the 5's.

From the book, we know that the exponent of a prime p in the prime power
factorization of a factorial number n! is [n/p] + [n/p^2] + ... Thus, we have
[n/2] + [n/4] + ... and [n/5] + [n/25] + ... Because the numerators are always
n, then it can be seen through observation that there will always be at least
more 2's than 5's because [n/2] >= [n/5], [n/2^2] >= [n/5^2], ... Thus, the 5's
are the bottleneck of the powers of 10 because the number of 2's is greater
than or equal to the number of 5's.

Thus, we now need to calculate the number of 5's in the prime power
factorization of n!, which as stated above is [n/p] + [n/p^2] + ... which is
what we observed in our intuition.
```

### Old Thoughts ###

This is an interesting problem, at least when I think about it. I took the
straight forward approach, e.g. calculate n! then test how many 0's are at the
end. However, this doesn't use any of the lessons learnt from the chapter.

Upon observation at the completion of this, I noticed an interesting trend. The
number of 0's at the end of the number corresponds to the number of 5's in the
prime factorization of n!. A couple of examples might illustrate this point:

```
3! will intuitively have 0 0's at the end of the decimal expansion because 3! =
3 * 2 * 1 which has 5's. 3! = 6, thus our intuition is correct.

7! will intuitively have 1 following 0 at the end of the decimal expansion
because 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1 = 7 * 5 * 3^2 * 2^4 which has 1 5. 7! =
5040, thus our intuition is correct.

22! will intuitively have 4 following 0's at the end of the decimal expansion
because 22! = 22 * 21 * 20 * ... * 15 * ... * 10 * ... * 5 * ... * 1 = 21 * ...
 * 5^4 * ... . 22! = 1124000727777607680000, thus our intuition is correct.

Finally, we check 26!. Our prime factorization gets 2 5's from 25 and 1 5 from
20, 15, 10, and 5, so we would intuitively think that 26! has 6 following 0's.
26! = 403291461126605635584000000, so once again our intuition is correct.
```

I'm not 100% comfortable using this observation without proof, however, so I'll
leave the code as-is for now and come back to it later, attempt a proof, and if
I find a satisfiable proof, I'll redo the problem using this prime factorization
method (which would also be so much more efficient) to solve the problem.

[thoughts]: #thoughts
[proofs]: #proof
[old_thoughts]: #oldthoughts
