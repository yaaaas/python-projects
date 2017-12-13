Task : Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

Program Flow : 
1. The user is prompted for the number of fibonaci numbers he wishes to generate
2. The "zeroth" and first value of the sequence is generated. (This allows us to generate the second element of the fibonaci series, which is also 1 by using 0 as the "zeroth" element)
3. The sequence is then generated using a while loop that increments repeatedly until we've generated the number of fibonaci numbers specified in step 1

Sample output
```
Enter the number of fibonaci numbers you wish to generate:  20
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765
```
