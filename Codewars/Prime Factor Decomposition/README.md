Task: Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :  "(p1**n1)(p2**n2)...(pk**nk)" with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240
```
"(2**5)(5)(7**2)(11)"
```

Program Flow
1. Program initialises a list prime which contains every prime factor up to 200
2. A while loop is initialised while n is not equal to 1. W
3. The program divides the evaluated number by each factor in the list prime, starting from 2, until n is equal to 1. It uses modulo to check if the number is indeed a factor.
4. These factors are then stored in a 
