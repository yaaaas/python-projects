Task : Code a program that will be able to evaluate whether a number is prime or not.

Program flow

isPrime() : This approach is ideal for large numbers. There is the probability of encountering a carmichael number such as 561 but there are only about 2000 of these numbers for the first 25 billion numbers in the number series. The probability is around 8x10^-8 that you'll encounter a carmichael number
1. User is prompted for a number to evaluate
2. The number is then checked to see if it is 1,2 or 3. If the input falls into one of these categories, the program automatically returns true.
3. THe number is then checked to see if it obeys Fermat's Little Theorem, that is that for a prime number p and a random number x ( x is a positive number ) , the result of the equation x^p - x will be divisible by p. The user is then informed that the number is a prime number
4. If the number is evaluated to be a composite, the corresponding error message will be printed.

Sample Output

isPrime()/isPrime2() sample output

Case 1 : Composite Number

```
Please enter your integer to be evaluated:  34
34 is not a prime!
```

Case 2 : Prime Number
```
Please enter your integer to be evaluated:  1234567
1234567 is not a prime!
```
